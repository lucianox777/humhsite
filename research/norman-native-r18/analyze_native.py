#!/usr/bin/env python3
"""Audit native BehaviorSpace output; never infer HUMH hypothesis status."""
import csv, hashlib, json, math, re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
P=json.loads((ROOT/'protocol.json').read_text())
M={
 'beliefs': '[agent-belief] of sort turtles',
 'initial_beliefs': '[initial-belief] of sort turtles',
 'heard': '[heard] of sort turtles',
 'recency': '[recency-list] of sort turtles',
 'evidence_holdings': '[agent-evidence-list] of sort turtles',
 'world_evidence': 'evidence-list',
 'world_truth': 'hypothesis-value',
 'optimal_posterior': 'optimal-posterior',
 'mean_belief': 'mean [agent-belief] of turtles',
 'D': 'mean [abs (agent-belief - mean [agent-belief] of turtles)] of turtles',
 'EH': '1 - abs (2 * mean [agent-belief] of turtles - 1)',
 'unique_evidence_receipts_after_initialization': 'sum [length heard - initial-draws] of turtles'
}
def nl_value(text):
    text=str(text).strip()
    if text.startswith('['):
        tokens=re.findall(r'"(?:\\.|[^"\\])*"|\[|\]|[^\s\[\]]+',text)
        pos=0
        def rec():
            nonlocal pos
            if tokens[pos]=='[':
                pos+=1; out=[]
                while pos<len(tokens) and tokens[pos]!=']': out.append(rec())
                if pos>=len(tokens): raise ValueError('Unclosed NetLogo list')
                pos+=1; return out
            t=tokens[pos]; pos+=1
            return nl_value(t)
        result=rec()
        if pos!=len(tokens): raise ValueError('Trailing NetLogo tokens')
        return result
    if text.startswith('"'): return json.loads(text)
    if text=='true': return True
    if text=='false': return False
    if text=='nobody': return None
    try: return int(text)
    except ValueError:
        try: return float(text)
        except ValueError: return text

def read_table(path):
    with path.open(newline='',encoding='utf-8-sig') as f: rows=list(csv.reader(f))
    matches=[i for i,r in enumerate(rows) if '[step]' in r and M['beliefs'] in r]
    if len(matches)!=1: raise AssertionError(f'Could not locate unique BehaviorSpace header: {path}')
    header=rows[matches[0]]; result=[]
    for row in rows[matches[0]+1:]:
        if len(row)!=len(header) or not row or not row[0].strip().isdigit(): continue
        d=dict(zip(header,row)); entry={'step':int(d['[step]'])}
        for k,expr in M.items(): entry[k]=nl_value(d[expr])
        result.append(entry)
    assert result and len({r['step'] for r in result})==len(result)
    result.sort(key=lambda r:r['step'])
    assert result[0]['step']==0 and result[-1]['step']==P['ticks']
    assert [r['step'] for r in result]==list(range(P['ticks']+1))
    for r in result:
        b=r['beliefs']; assert len(b)==P['model_settings']['number-of-agents']
        assert all(isinstance(x,(int,float)) and math.isfinite(x) and 0<=x<=1 for x in b)
        avg=math.fsum(b)/len(b); D=math.fsum(abs(x-avg) for x in b)/len(b)
        assert math.isclose(r['mean_belief'],avg,abs_tol=1e-10)
        assert math.isclose(r['D'],D,abs_tol=1e-10)
        assert math.isclose(r['EH'],1-abs(2*avg-1),abs_tol=1e-10)
        assert all(len(h)==P['model_settings']['number-of-agents'] for h in [r['heard'],r['recency'],r['evidence_holdings']])
    return result

def audit(results):
    report={'status':'ENGINEERING_ONLY_NOT_CONFIRMATORY','protocol_id':P['id'],
            'source_sha256':json.loads((ROOT/'results/source_manifest.json').read_text())['source_sha256'],
            'pairs':[],'assertions':[],'hypothesis_classification':None}
    def check(cond,name):
        assert cond,name
        report['assertions'].append(name)
    for seed in P['seeds']:
        n=results[f'seed{seed}_NO_COMMUNICATION']; c=results[f'seed{seed}_COMMUNICATION']
        a,b=n[0],c[0]
        for key in ['beliefs','initial_beliefs','heard','recency','evidence_holdings','world_evidence','world_truth','optimal_posterior']:
            check(a[key]==b[key],f'seed{seed}: identical initial {key}')
        for r in n:
            for key in ['beliefs','initial_beliefs','heard','recency','evidence_holdings','world_evidence','world_truth']:
                check(r[key]==a[key],f'seed{seed}: no-channel {key} constant at tick {r["step"]}')
        for r in c:
            check(r['world_evidence']==a['world_evidence'] and r['world_truth']==a['world_truth'],f'seed{seed}: world constant at tick {r["step"]}')
            check(all(set(r['heard'][i]).issuperset(a['heard'][i]) for i in range(len(r['heard']))),f'seed{seed}: evidence monotonic at tick {r["step"]}')
        pair={'seed':seed,'initial_D':a['D'],'no_communication_final_D':n[-1]['D'],
              'communication_final_D':c[-1]['D'],'communication_minus_control_D':c[-1]['D']-n[-1]['D'],
              'initial_EH':a['EH'],'no_communication_final_EH':n[-1]['EH'],
              'communication_final_EH':c[-1]['EH'],'communication_minus_control_EH':c[-1]['EH']-n[-1]['EH'],
              'initial_beliefs':a['beliefs'],'communication_final_beliefs':c[-1]['beliefs'],
              'new_evidence_receipts':c[-1]['unique_evidence_receipts_after_initialization'],
              'no_communication_new_receipts':n[-1]['unique_evidence_receipts_after_initialization']}
        check(pair['no_communication_new_receipts']==0,f'seed{seed}: zero control receipts')
        report['pairs'].append(pair)
    report['assertion_count']=len(report['assertions'])
    report['summary']='Native execution verified. Differences are descriptive causal contrasts for this frozen fixture, not HUMH confirmation.'
    return report

def main():
    out={}
    for seed in P['seeds']:
        for arm in P['arms']:
            name=f'seed{seed}_{arm}'
            out[name]=read_table(ROOT/'results'/f'{name}.csv')
    report=audit(out)
    (ROOT/'results/native_trajectories.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    (ROOT/'results/native_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
