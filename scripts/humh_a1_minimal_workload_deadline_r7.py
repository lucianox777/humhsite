from pathlib import Path
import hashlib, json

root = Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v = root / 'v2.0.0'
specp = v / '01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep = v / '01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
readmep = v / 'README.md'
parent_readmep = root / 'README.md'
lockp = v / '02_dependencias/DEPENDENCIES.lock.json'
sumsp = v / '03_integridade/SHA256SUMS.txt'
rootshap = v / 'HUMH_A0_A1_v2.0.0.sha256'
ATT_SHA = '3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

spec = specp.read_text(encoding='utf-8')
spec = spec.replace('**Status:** `PRE_CODE_DISCRETE_WORKLOAD_NORMALIZATION_FREEZE`',
                    '**Status:** `PRE_CODE_MINIMAL_WORKLOAD_AND_DEADLINE_FREEZE`', 1)
mi = spec.index('**Motivo:** '); me = spec.index('\n', mi)
new_motive = ('**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`; A1b permanece em auditoria estrutural. '
              'A classe de workload já reduzida a `K_C` é agora fechada no menor caso não trivial, `K_C=2`, que exige processamento em mais de uma oportunidade sem introduzir profundidade de fila desnecessária. Como a arquitetura lógica consegue conceder duas oportunidades e concluir a atualização no mesmo ciclo, aplica-se a preferência canônica do §16 e congela-se `L_A=1`. Assim `K_C` e `L_A` deixam de ser parâmetros de tuning.')
spec = spec[:mi] + new_motive + spec[me:]

old = '''O valor de `K_C` ainda não é
escolhido; ele é parâmetro exclusivamente instrumental e poderá ser selecionado apenas pelo
benchmark cego autorizado, nunca por `p`, `EH`, `eta_hat`, `D` coletivo ou qualquer outcome.

```text
REQUIRED_WORK_UNIT = OBSERVER_CAPACITY_UNIT
OBSERVER_CAPACITY_UNIT = 1
REQUIRED_WORK_PARAMETER = K_C
REQUIRED_WORK_NUMERIC_STATUS = UNFROZEN_BLIND_INSTRUMENT_CALIBRATION
```
'''
new = '''O primeiro A1 precisa preservar a distinção entre **capacidade por oportunidade** e
**disponibilidade de oportunidades**. Por isso `K_C=1` seria o caso trivial em que toda
demanda cabe em uma única oportunidade. Entre os inteiros `K_C>1`, o menor caso que exerce
processamento parcial sem acrescentar profundidade instrumental desnecessária é:

\\[
\\boxed{K_C=2.}
\\]

A escolha é feita por **minimalidade estrutural antes de qualquer benchmark**, não por
contraste observado de atenção e não por outcome científico. Valores `K_C>2` ficam para
robustez/sucessor se houver razão prospectiva.

```text
REQUIRED_WORK_UNIT = OBSERVER_CAPACITY_UNIT
OBSERVER_CAPACITY_UNIT = 1
REQUIRED_WORK_PARAMETER = K_C = 2
REQUIRED_WORK_NUMERIC_STATUS = FROZEN_MINIMAL_NONTRIVIAL
K_C_SELECTION_BY_ABENCH0 = FORBIDDEN_NOT_NEEDED
```
'''
if old not in spec: raise RuntimeError('K_C pending block not found')
spec = spec.replace(old,new,1)

# Freeze L_A=1 immediately after deadline definition in §4.1.
anchor = '''`L_A` é comum aos braços e independente de atenção, `EH`, inércia e outcome.
'''
insert = r'''

### L_A do primeiro A1 — CONGELADO

A definição canônica §16 determina que o primeiro A1 deve **preferir `L_A=1` ciclo** quando
a arquitetura comportar uma atualização completa nesse intervalo. A arquitetura aqui
congelada satisfaz essa condição: `B=1`, `K_C=2`, e o scheduler pode conceder duas
opotunidades lógicas no mesmo ciclo; ao completar a segunda, a rotina basal é executada
imediatamente antes da barreira de commit.

Portanto:

\[
\boxed{L_A=1.}
\]

Uma demanda criada em `t` pode concluir em `t` ou em `t+1`; expira somente quando
`current_cycle > t+1`.

```text
FIRST_A1_L_A = 1
L_A_SELECTION = CANONICAL_PREFERENCE_ARCHITECTURE_SUPPORTED
L_GRID = NOT_REQUIRED_FOR_SELECTION
ABENCH0_L_A_ROLE = VALIDATION_ONLY
```

`ABENCH0` continua obrigatório como auditoria cega do instrumento, mas não pode aumentar o
deadline simplesmente para produzir um contraste mais conveniente. Se uma futura
implementação não conseguir executar o contrato lógico acima, ela não é esta construção e
deve voltar à fase pré-run antes de coletar qualquer trajetória científica.
'''
if insert.strip() not in spec:
    spec = spec.replace(anchor, anchor+insert, 1)

# Provenance: K_C and L_A leave blind calibration.
spec = spec.replace('CANONICAL_FIXED\n  D_i(W)=W',
                    'CANONICAL_FIXED\n  D_i(W)=W\n  L_A=1 quando a arquitetura lógica suporta atualização completa no intervalo',1)
spec = spec.replace('IMPLEMENTATION_NORMALIZATION\n  observer_buffer_capacity B = 1 unidade por oportunidade',
                    'IMPLEMENTATION_NORMALIZATION\n  observer_buffer_capacity B = 1 unidade por oportunidade\n  K_C=2 como menor workload inteiro não trivial (>1)',1)
spec = spec.replace('BLIND_INSTRUMENT_CALIBRATION_ABENCH0\n  K_C required opportunities per isolated request\n  L_grid e L_A\n',
                    'BLIND_INSTRUMENT_CALIBRATION_ABENCH0\n',1)

# Frozen / pending and procedure.
spec = spec.replace('required_work_heterogeneity_regime = HOMOGENEOUS_FOR_FIRST_A1\nlogical_cycle_commit',
                    'required_work_heterogeneity_regime = HOMOGENEOUS_FOR_FIRST_A1\nrequired_opportunities_per_request_K_C = 2\nL_A = 1\nlogical_cycle_commit',1)
spec = spec.replace('required_opportunities_per_request_K_C\n','',1)
spec = spec.replace('L_grid\n','',1)
spec = spec.replace('L_A\n','',1)
spec = spec.replace('3. preservar `B=1` e workload homogêneo `C_j=K_C` como normalizações/isolamento, e congelar `K_C`, `eta_EH0`, `lambda_state`, `p_A`, `p_B`, `p_0` e os demais números',
                    '3. preservar `B=1`, `K_C=2` e `L_A=1` já congelados, e congelar `eta_EH0`, `lambda_state`, `p_A`, `p_B`, `p_0` e os demais números',1)
spec = spec.replace('4. verificar que os valores congelados satisfazem o critério analítico `0 < eta0 <= 1`',
                    '4. verificar que os valores basais congelados satisfazem o critério analítico `0 < eta0 <= 1`',1)

specp.write_text(spec,encoding='utf-8')

trace=json.loads(tracep.read_text(encoding='utf-8'))
trace['status']='V2_0_0_MINIMAL_WORKLOAD_AND_LA1_FROZEN_PREPUBLICATION'
trace['scientific_run_authorized']=False
wc=trace.setdefault('workload_contract',{})
wc.update({
    'K_C_value':2,
    'numeric_status_K_C':'FROZEN_MINIMAL_NONTRIVIAL_BEFORE_BENCHMARK',
    'K_C_selection_rule':'smallest positive integer >1; exercises multi-opportunity processing with minimum added queue depth',
    'selected_by_ABENCH0':False,
    'selected_by_scientific_outcomes':False,
    'larger_K_disposition':'SUCCESSOR_OR_ROBUSTNESS_ONLY'
})
trace['first_A1_deadline_freeze']={
    'status':'FROZEN_L_A_EQUALS_1',
    'L_A':1,
    'completion_rule':'t_complete <= t+1',
    'expiry_rule':'current_cycle > deadline_cycle',
    'architecture_support_argument':'B=1; K_C=2; scheduler permits two logical opportunities in one cycle and immediate basal update before synchronous commit barrier.',
    'selection':'CANONICAL_PREFERENCE_ARCHITECTURE_SUPPORTED',
    'L_grid_required_for_selection':False,
    'ABENCH0_role_for_L_A':'VALIDATION_ONLY',
    'canonical_refs':[{
        'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':16,
        'clause_or_statement':'For the first A1, prefer L_A=1 cycle if the architecture supports a complete update in that interval; otherwise determine it only in a separate blind technical pilot.'
    }]
}

# Remove K_C, L_grid, L_A from all pending lists; retain opportunity schedule calibration.
remove={'required_opportunities_per_request_K_C','L_grid','L_A'}
def walk(o):
    if isinstance(o,dict):
        for k,v in list(o.items()):
            if isinstance(v,list) and (k=='numerics_pending' or k=='unfrozen_required_before_run'):
                o[k]=[x for x in v if x not in remove]
            else: walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(trace)
trace['unfrozen_required_before_run']=[x for x in trace.get('unfrozen_required_before_run',[]) if x not in remove]

pp=trace.get('parameter_provenance_policy',{})
classes=pp.get('classes',{}) if isinstance(pp,dict) else {}
if isinstance(classes,dict):
    blind=classes.get('BLIND_INSTRUMENT_CALIBRATION_ABENCH0',[])
    if isinstance(blind,list):
        classes['BLIND_INSTRUMENT_CALIBRATION_ABENCH0']=[x for x in blind if x not in {'required_opportunities_per_request_K_C','L_grid','L_A'}]
    classes['CANONICAL_FIXED']=list(dict.fromkeys(classes.get('CANONICAL_FIXED',[])+['L_A=1_first_A1_architecture_supported']))
    classes['IMPLEMENTATION_NORMALIZATION']=list(dict.fromkeys(classes.get('IMPLEMENTATION_NORMALIZATION',[])+['K_C=2_minimal_nontrivial_multi_opportunity_workload']))

tracep.write_text(json.dumps(trace,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

readmep.write_text('''# HUMH A0/A1 v2.0.0 — estado pré-publicação\n\nA1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` (`ANBC0=FAIL_DERIVATIONAL`). A1b mantém `D` como candidato `CONDITIONAL_DISCRIMINATIVE`.\n\nCongelamentos correntes:\n\n- `D_i(W)=W`;\n- `B_i=1 observer_capacity_unit`;\n- workload homogêneo e mínimo não trivial: `K_C=2`;\n- deadline canônico preferencial suportado pela arquitetura: `L_A=1`;\n- regime basal homogêneo e `SYNCHRONOUS_SNAPSHOT_BARRIER`;\n- basal numérico por `eta_EH0` e `lambda_state`;\n- A1b HIGH/LOW pré-atribuído e massa global de oportunidades igual por ciclo;\n- `ABENCH0` não escolhe mais `K_C` ou `L_A`; nesses itens seu papel é validação cega.\n\n`SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n''',encoding='utf-8')
parent_readmep.write_text('''# HUMH — Experimentos de Atenção\n\n`v2.0.0/` é a árvore corrente A0/A1 pré-publicação.\n\n- `ANBC0 = FAIL_DERIVATIONAL`; A1a = `MECHANISM_DEMONSTRATION_ONLY [C1]`;\n- A1b: `D` candidato `CONDITIONAL_DISCRIMINATIVE`;\n- `D_i(W)=W`, `B=1`, workload homogêneo `K_C=2` e `L_A=1`;\n- regime basal homogêneo e barreira síncrona;\n- basal numérico reduzido a `eta_EH0` e `lambda_state`;\n- A1b HIGH/LOW fixo e exógeno, níveis ainda pendentes;\n- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n\nA teoria exibida pelo site permanece `../../teoria.md`; a cópia em `v2.0.0/02_dependencias/` é a dependência canônica hash-locked.\n''',encoding='utf-8')

spec_sha=sha(specp); trace_sha=sha(tracep)
lock=json.loads(lockp.read_text(encoding='utf-8'))
lock['publication_state']='REGENERATED_PRE_PUBLICATION_MINIMAL_WORKLOAD_LA1_R7'
for a in lock.get('normative_artifacts',[]):
    if a.get('path','').endswith('HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'): a['sha256']=spec_sha
    if a.get('path','').endswith('HUMH_A0_A1_Traceabilidade_v2.0.0.json'): a['sha256']=trace_sha
lock['workload_contract']='FROZEN_K_C_EQUALS_2_MINIMAL_NONTRIVIAL'
lock['deadline_contract']='FROZEN_L_A_EQUALS_1_CANONICAL_PREFERENCE'
lockp.write_text(json.dumps(lock,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rootshap.write_text(f'{spec_sha}  HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md\n{trace_sha}  HUMH_A0_A1_Traceabilidade_v2.0.0.json\n',encoding='utf-8')
ordered=['01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md','01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json','02_dependencias/DEPENDENCIES.lock.json','02_dependencias/HUMH_Definicao_Atencao_Observacional_Efetiva_v1.0.0.md','02_dependencias/teoria.md','03_integridade/verify.py','HUMH_A0_A1_v2.0.0.sha256','README.md','TREE.txt']
sumsp.write_text(''.join(f'{sha(v/rel)}  {rel}\n' for rel in ordered),encoding='utf-8')
print('SPEC_SHA256',spec_sha); print('TRACE_SHA256',trace_sha)
