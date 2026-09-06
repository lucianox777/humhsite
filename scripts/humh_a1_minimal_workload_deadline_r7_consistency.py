from pathlib import Path
import hashlib, json

root=Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v=root/'v2.0.0'
specp=v/'01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep=v/'01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
lockp=v/'02_dependencias/DEPENDENCIES.lock.json'
sumsp=v/'03_integridade/SHA256SUMS.txt'
rootshap=v/'HUMH_A0_A1_v2.0.0.sha256'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

s=specp.read_text(encoding='utf-8')
s=s.replace('### \nUma requisição criada em `t` entra em `U_i` somente se:', '### L_A\nUma requisição criada em `t` entra em `U_i` somente se:',1)
s=s.replace('duas\nopotunidades lógicas','duas\noportunidades lógicas',1)
s=s.replace('- `L_A`, exceto via novo `ABENCH0` cego técnico;', '- `L_A` (agora congelado prospectivamente em `1` pelo §16; nunca selecionado por resultados v1.0.x);',1)
# Remove stale L fields only from §26 pending block.
a=s.index('# 26. Itens de desenho e números ainda NÃO congelados')
b=s.index('# 27. Procedimento autorizado daqui até run-ready',a)
block=s[a:b]
block=block.replace('L_grid\n','').replace('L_A\n','')
s=s[:a]+block+s[b:]
specp.write_text(s,encoding='utf-8')

spec_sha=sha(specp); trace_sha=sha(tracep)
lock=json.loads(lockp.read_text(encoding='utf-8'))
lock['publication_state']='REGENERATED_PRE_PUBLICATION_MINIMAL_WORKLOAD_LA1_R7_CONSISTENT'
for x in lock.get('normative_artifacts',[]):
    if x.get('path','').endswith('HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'): x['sha256']=spec_sha
    if x.get('path','').endswith('HUMH_A0_A1_Traceabilidade_v2.0.0.json'): x['sha256']=trace_sha
lockp.write_text(json.dumps(lock,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rootshap.write_text(f'{spec_sha}  HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md\n{trace_sha}  HUMH_A0_A1_Traceabilidade_v2.0.0.json\n',encoding='utf-8')
ordered=['01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md','01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json','02_dependencias/DEPENDENCIES.lock.json','02_dependencias/HUMH_Definicao_Atencao_Observacional_Efetiva_v1.0.0.md','02_dependencias/teoria.md','03_integridade/verify.py','HUMH_A0_A1_v2.0.0.sha256','README.md','TREE.txt']
sumsp.write_text(''.join(f'{sha(v/rel)}  {rel}\n' for rel in ordered),encoding='utf-8')
print('SPEC_SHA256',spec_sha); print('TRACE_SHA256',trace_sha)
