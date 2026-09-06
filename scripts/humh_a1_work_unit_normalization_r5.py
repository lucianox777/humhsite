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

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

spec = specp.read_text(encoding='utf-8')
spec = spec.replace('**Status:** `PRE_CODE_PARAMETER_IDENTIFIABILITY_AND_PROVENANCE_FREEZE`',
                    '**Status:** `PRE_CODE_WORK_UNIT_NORMALIZATION_FREEZE`', 1)
mi = spec.index('**Motivo:** ')
me = spec.index('\n', mi)
new_motive = ('**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`. '
              'A1b permanece em auditoria estrutural. Depois de fechar `D_i(W)=W`, a reparametrização basal identificável e a proveniência numérica, elimina-se agora mais um grau de liberdade puramente computacional: no regime homogêneo do primeiro A1, a unidade de trabalho é definida pela própria capacidade basal por oportunidade, de modo que `B_i=B=1` por normalização de unidade e não por calibração científica.')
spec = spec[:mi] + new_motive + spec[me:]

old = '''O valor numérico de `B` permanece `UNFROZEN_REQUIRED_BEFORE_RUN` e não poderá ser
selecionado com base em outcomes v1.0.x ou em qualquer outcome A1.

`B_i` continua não sendo atenção, não é `P_i_obs` e não pode entrar como outcome ou
resgate explicativo. Heterogeneidade de `B_i` fica reservada para robustez/sucessor
prospectivo, sem reclassificar o primeiro A1.
'''
new = r'''Como o primeiro A1 já congela `B_i=B` para todos os observadores e braços, o valor
absoluto de `B` não contém informação científica: somente a razão entre trabalho exigido e
capacidade por oportunidade afeta a fila.

Escolhe-se, portanto, a própria capacidade homogênea como **unidade de trabalho lógico**:

\[
\boxed{B_i=B=1\ \text{unidade de capacidade por oportunidade}.}
\]

Para qualquer representação anterior com `B>0`, defina:

\[
\widetilde C_j=C_j/B,
\qquad
\widetilde R_j=remaining\_work_j/B.
\]

Então uma oportunidade executa:

\[
q'=\min(1,\widetilde R_j),
\]

e preserva exatamente a sequência de conclusões em **número de oportunidades**, desde que
o workload seja expresso nessa unidade normalizada. Portanto a escolha `B=1` é mudança de
unidade, não alteração de atenção, velocidade física ou capacidade relativa entre braços.

Status:

```text
OBSERVER_CAPACITY_UNIT = 1
OBSERVER_BUFFER_CAPACITY_VALUE = NORMALIZED_NOT_FITTED
B_i = 1 para todo i no primeiro A1
```

`B_i` continua não sendo atenção, não é `P_i_obs` e não pode entrar como outcome ou
resgate explicativo. Heterogeneidade de `B_i` fica reservada para robustez/sucessor
prospectivo, sem reclassificar o primeiro A1.
'''
if old not in spec:
    raise RuntimeError('B pending paragraph not found')
spec = spec.replace(old, new, 1)

# Add normalized workload form after n_req formula discussion.
marker = 'O buffer define **quanto pode ser processado por oportunidade**, não o tamanho máximo\nde tarefa que o observador consegue resolver.\n'
if 'REQUIRED_WORK_UNIT = OBSERVER_CAPACITY_UNIT' not in spec:
    add = r'''

Na unidade normalizada do primeiro A1:

\[
\boxed{B_i=1}
\]

\[
\boxed{C_j=\texttt{required\_capacity\_units}_j>0}
\]

logo:

\[
\boxed{n^{req}_{ij}=\lceil C_j\rceil.}
\]

A regra/distribuição prospectiva de `C_j` continua pendente e poderá ser calibrada somente
pelo caminho técnico cego autorizado; o valor de `B` não é mais parâmetro dessa calibração.

```text
REQUIRED_WORK_UNIT = OBSERVER_CAPACITY_UNIT
OBSERVER_CAPACITY_UNIT = 1
```
'''
    spec = spec.replace(marker, marker + add, 1)

# Align demand record / work quantum language.
spec = spec.replace('```text\nWORK_QUANTUM = 1\n```\n\né unidade abstrata de trabalho lógico, não ms, instrução física, MHz ou %CPU.',
                    '```text\nOBSERVER_CAPACITY_UNIT = 1\nWORK_QUANTUM = 1 observer_capacity_unit\n```\n\né unidade abstrata normalizada de trabalho lógico, não ms, instrução física, MHz ou %CPU.', 1)

# Provenance: add implementation normalization and remove B from ABENCH.
spec = spec.replace('THEORY_CONSTRAINED_NOT_FITTED\n  eta_EH0 in (0,1]',
                    'IMPLEMENTATION_NORMALIZATION\n  observer_buffer_capacity B = 1 unidade por oportunidade\n  WORK_QUANTUM = 1 observer_capacity_unit\n\nTHEORY_CONSTRAINED_NOT_FITTED\n  eta_EH0 in (0,1]', 1)
spec = spec.replace('BLIND_INSTRUMENT_CALIBRATION_ABENCH0\n  observer_buffer_capacity_value\n  required_work rule/range',
                    'BLIND_INSTRUMENT_CALIBRATION_ABENCH0\n  required_work rule/range', 1)

# Frozen/pending lists.
spec = spec.replace('observer_buffer_capacity_heterogeneity_regime = HOMOGENEOUS\nlogical_cycle_commit',
                    'observer_buffer_capacity_heterogeneity_regime = HOMOGENEOUS\nobserver_buffer_capacity_value = NORMALIZED_B_EQUALS_1\nlogical_cycle_commit', 1)
spec = spec.replace('lambda_state_resistance_value\nobserver_buffer_capacity_value\nrequired_work_rule',
                    'lambda_state_resistance_value\nrequired_work_rule', 1)
spec = spec.replace('3. congelar `eta_EH0`, `lambda_state`, `B`, `p_A`, `p_B`, `p_0` e os demais números',
                    '3. preservar `B=1` como normalização de unidade e congelar `eta_EH0`, `lambda_state`, `p_A`, `p_B`, `p_0` e os demais números', 1)

specp.write_text(spec, encoding='utf-8')

trace = json.loads(tracep.read_text(encoding='utf-8'))
trace['status'] = 'V2_0_0_WORK_UNIT_NORMALIZATION_FROZEN_PREPUBLICATION'
trace['scientific_run_authorized'] = False
trace['work_unit_normalization'] = {
    'status': 'FROZEN_IMPLEMENTATION_NORMALIZATION',
    'first_A1_homogeneous_capacity': 'B_i=B for all observers',
    'observer_capacity_unit': 1,
    'observer_buffer_capacity_value': 1,
    'normalized_required_work': 'C_tilde_j=C_j/B',
    'normalized_remaining_work': 'R_tilde_j=remaining_work_j/B',
    'service_per_opportunity': 'q=min(1,R_tilde_j)',
    'isolated_required_opportunities': 'ceil(C_tilde_j)',
    'scientific_role': 'AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION_UNIT_NORMALIZATION',
    'is_attention': False,
    'is_arm_manipulation': False,
    'selected_by_ABENCH0': False,
    'rationale': 'With homogeneous B>0 fixed across observers/arms, absolute B is a work-unit scale; completion ordering in opportunity units depends on C/B, not the absolute scale.',
    'anti_alias': ['A_i != B','P_i_obs != B','B is not CPU speed','B is not thread priority']
}

# Remove B scalar from unfrozen list.
uf = trace.get('unfrozen_required_before_run', [])
trace['unfrozen_required_before_run'] = [x for x in uf if x != 'observer_buffer_capacity_value']

# Recursively align instrument objects.
def walk(obj):
    if isinstance(obj, dict):
        opc = obj.get('observer_processing_capacity')
        if isinstance(opc, dict):
            opc['normalized_value_first_A1'] = 1
            opc['numeric_status'] = 'FROZEN_BY_UNIT_NORMALIZATION'
            opc['selected_by_ABENCH0'] = False
            hr = opc.get('heterogeneity_regime')
            if isinstance(hr, dict):
                hr['status'] = 'FROZEN_HOMOGENEOUS_FOR_FIRST_A1'
                hr['allowed_regimes_for_first_A1'] = ['HOMOGENEOUS']
        np = obj.get('numerics_pending')
        if isinstance(np, list):
            obj['numerics_pending'] = [x for x in np if x not in (
                'observer_buffer_capacity_heterogeneity_regime',
                'observer_buffer_capacity_rule',
                'observer_buffer_capacity_values_or_distribution',
                'observer_buffer_capacity_value')]
        for val in obj.values(): walk(val)
    elif isinstance(obj, list):
        for val in obj: walk(val)
walk(trace)

base = trace.get('first_A1_baseline_regime')
if isinstance(base, dict):
    base['observer_buffer_capacity'] = 'B_i=B=1 normalized observer-capacity unit for all observers; not a fitted numeric parameter'

pp = trace.get('parameter_provenance_policy')
if isinstance(pp, dict):
    classes = pp.setdefault('classes', {})
    classes['IMPLEMENTATION_NORMALIZATION'] = ['observer_buffer_capacity_B_equals_1','WORK_QUANTUM_equals_1_observer_capacity_unit']
    blind = classes.get('BLIND_INSTRUMENT_CALIBRATION_ABENCH0')
    if isinstance(blind, list):
        classes['BLIND_INSTRUMENT_CALIBRATION_ABENCH0'] = [x for x in blind if x != 'observer_buffer_capacity_value']

tracep.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

readmep.write_text('''# HUMH A0/A1 v2.0.0 — estado pré-publicação\n\nA1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` (`ANBC0=FAIL_DERIVATIONAL`).\n\nA1b mantém `D` como candidato auditado, com classificação estrutural `CONDITIONAL_DISCRIMINATIVE` e confirmação ainda não autorizada.\n\nCongelamentos correntes:\n\n- uma demanda elegível por observador/ciclo: `D_i(W)=W`;\n- regime basal homogêneo e ciclo em `SYNCHRONOUS_SNAPSHOT_BARRIER`;\n- capacidade computacional homogênea normalizada por unidade: `B_i=B=1`; o workload passa a ser medido em `observer_capacity_unit`;\n- dinâmica basal numericamente representada pelos compostos identificáveis `eta_EH0` e `lambda_state`;\n- A1b HIGH/LOW pré-atribuído e massa global de oportunidades igual por ciclo;\n- política de proveniência numérica congelada; `B` não é mais número a calibrar por `ABENCH0`;\n- `required_work`, `L_A`, níveis instrumentais e números científicos continuam pendentes sob seus canais autorizados.\n\n`SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n''', encoding='utf-8')

parent_readmep.write_text('''# HUMH — Experimentos de Atenção\n\n`v2.0.0/` é a árvore corrente A0/A1 pré-publicação.\n\n- `ANBC0 = FAIL_DERIVATIONAL`;\n- `A1a = MECHANISM_DEMONSTRATION_ONLY [C1]`;\n- A1b: `D` candidato em auditoria estrutural `CONDITIONAL_DISCRIMINATIVE`;\n- `D_i(W)=W`, regime basal homogêneo e barreira síncrona congelados;\n- capacidade auxiliar homogênea normalizada em `B=1 observer_capacity_unit`;\n- basal numérico reduzido a `eta_EH0` e `lambda_state`, sem falsa decomposição de `omega/iota_obs/kappa`;\n- A1b HIGH/LOW fixo e exógeno, níveis ainda pendentes;\n- proveniência dos parâmetros congelada antes de `ABENCH0`;\n- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n\nA teoria exibida pelo site permanece `../../teoria.md`; a cópia em `v2.0.0/02_dependencias/` é a dependência canônica hash-locked.\n''', encoding='utf-8')

spec_sha = sha(specp)
trace_sha = sha(tracep)
lock = json.loads(lockp.read_text(encoding='utf-8'))
lock['publication_state'] = 'REGENERATED_PRE_PUBLICATION_WORK_UNIT_NORMALIZATION_R5'
for a in lock.get('normative_artifacts', []):
    if a.get('path','').endswith('HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'):
        a['sha256'] = spec_sha
    if a.get('path','').endswith('HUMH_A0_A1_Traceabilidade_v2.0.0.json'):
        a['sha256'] = trace_sha
lock['work_unit_normalization'] = 'FROZEN_B_EQUALS_1_OBSERVER_CAPACITY_UNIT'
lockp.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

rootshap.write_text(f'{spec_sha}  HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md\n{trace_sha}  HUMH_A0_A1_Traceabilidade_v2.0.0.json\n', encoding='utf-8')

ordered = [
    '01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md',
    '01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json',
    '02_dependencias/DEPENDENCIES.lock.json',
    '02_dependencias/HUMH_Definicao_Atencao_Observacional_Efetiva_v1.0.0.md',
    '02_dependencias/teoria.md',
    '03_integridade/verify.py',
    'HUMH_A0_A1_v2.0.0.sha256',
    'README.md',
    'TREE.txt',
]
sumsp.write_text(''.join(f'{sha(v / rel)}  {rel}\n' for rel in ordered), encoding='utf-8')

print('SPEC_SHA256', spec_sha)
print('TRACE_SHA256', trace_sha)
