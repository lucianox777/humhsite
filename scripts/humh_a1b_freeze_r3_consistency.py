from pathlib import Path
import hashlib, json

root=Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v=root/'v2.0.0'
specp=v/'01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep=v/'01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
lockp=v/'02_dependencias/DEPENDENCIES.lock.json'
rootsha=v/'HUMH_A0_A1_v2.0.0.sha256'
sumsp=v/'03_integridade/SHA256SUMS.txt'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

spec=specp.read_text(encoding='utf-8')
spec=spec.replace('**Status:** `PRE_CODE_A1B_STRUCTURAL_AUDIT`','**Status:** `PRE_CODE_A1B_ASSIGNMENT_AND_ETA_BOUND_FREEZE`',1)
old='**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`. A auditoria de A1b foi refinada: `D` continua candidato canônico, mas `D_A` determina apenas a quantidade total de conclusões por observador, não a exposição temporal aos fatores de atualização dependentes do estado coletivo. Para impedir que ordem física de WebWorkers se torne variável científica, congela-se uma barreira síncrona por ciclo lógico e um regime basal homogêneo para o primeiro A1. A classificação final de `ADIST0` continua anterior a qualquer trajetória científica.'
new='**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`. Em A1b, `D` permanece candidato canônico sob auditoria estrutural. Estão congelados o regime basal/B homogêneo do primeiro A1, a barreira síncrona do ciclo lógico, o critério analítico de admissibilidade de `eta0` e a semântica exógena de estratos HIGH/LOW com massa global de oportunidades pareada por ciclo. Os valores numéricos e a classificação final de `ADIST0` permanecem pendentes e devem ser fechados antes de qualquer trajetória científica.'
if old in spec: spec=spec.replace(old,new,1)
spec=spec.replace('O critério numérico que garante essa condição permanece a congelar prospectivamente.','O critério analítico que garante essa condição está congelado no §7.1.2.1; permanecem pendentes apenas os valores numéricos que deverão satisfazê-lo.',1)
spec=spec.replace('PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE','PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_LEVELS')
spec=spec.replace('4. certificar `0 < eta0 <= 1` em todo estado admissível, sem clamp pós-hoc;\n5. congelar a regra exata A1b mantendo a massa global de oportunidades igual em cada\n   ciclo e variando somente sua distribuição entre observadores;',
                  '4. verificar que os valores congelados satisfazem o critério analítico `0 < eta0 <= 1` em todo estado admissível, sem clamp pós-hoc;\n5. congelar os níveis numéricos A1b (`q_H`, `q_L`, proporção dos estratos e discretização por ciclo) sob a semântica de atribuição já congelada e com massa global de oportunidades igual em cada ciclo;')
specp.write_text(spec,encoding='utf-8')

tr=json.loads(tracep.read_text(encoding='utf-8'))
if 'a1b_derivational_audit' in tr:
    if tr['a1b_derivational_audit'].get('status_final')=='PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE':
        tr['a1b_derivational_audit']['status_final']='PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_LEVELS'
if 'A1b' in tr.get('result_logic',{}):
    if tr['result_logic']['A1b'].get('derivational_audit_final')=='PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE':
        tr['result_logic']['A1b']['derivational_audit_final']='PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_LEVELS'
tracep.write_text(json.dumps(tr,ensure_ascii=False,indent=2),encoding='utf-8')

lock=json.loads(lockp.read_text(encoding='utf-8'))
for item in lock.get('normative_artifacts',[]):
    if item['path'].endswith(specp.name): item['sha256']=sha(specp)
    if item['path'].endswith(tracep.name): item['sha256']=sha(tracep)
lockp.write_text(json.dumps(lock,ensure_ascii=False,indent=2),encoding='utf-8')
rootsha.write_text(f'{sha(specp)}  {specp.name}\n{sha(tracep)}  {tracep.name}\n',encoding='utf-8')
files=sorted(p for p in v.rglob('*') if p.is_file() and p!=sumsp)
sumsp.write_text('\n'.join(f'{sha(p)}  {p.relative_to(v).as_posix()}' for p in files)+'\n',encoding='utf-8')

assert 'O critério numérico que garante essa condição permanece a congelar prospectivamente.' not in spec
assert 'PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE' not in spec
print('SPEC_SHA256',sha(specp)); print('TRACE_SHA256',sha(tracep))
