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
spec = spec.replace('**Status:** `PRE_CODE_WORK_UNIT_NORMALIZATION_FREEZE`',
                    '**Status:** `PRE_CODE_DISCRETE_WORKLOAD_NORMALIZATION_FREEZE`', 1)
mi = spec.index('**Motivo:** ')
me = spec.index('\n', mi)
new_motive = ('**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`; A1b permanece em auditoria estrutural. '
              'Com `D_i(W)=W`, `B=1` e serviço sem spill entre demandas, o valor contínuo de `required_work` contém graus de liberdade sem efeito científico: a conclusão de uma demanda isolada depende somente de `ceil(C_j)`. O primeiro A1 passa, portanto, a usar workload homogêneo representado por um único inteiro `K_C>=1`, o número de oportunidades exigidas por demanda isolada; apenas `K_C` permanece para calibração técnica cega.')
spec = spec[:mi] + new_motive + spec[me:]

old = r'''Na unidade normalizada do primeiro A1:

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
new = r'''Na unidade normalizada do primeiro A1:

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

### 5.1.2.1. Quociente operacional do workload — CONGELADO

A implementação não executa atualização basal parcial: uma demanda só atualiza `p_i` quando
`remaining_work` chega a zero. Além disso, capacidade não usada na oportunidade de conclusão
não é transferida para a próxima demanda. Nessas regras já congeladas, dois workloads
positivos `C_a` e `C_b` com:

\[
\lceil C_a\rceil=\lceil C_b\rceil
\]

produzem exatamente o mesmo ciclo de conclusão para a mesma sequência de oportunidades.
Portanto o valor fracionário dentro de cada intervalo não é identificável nem operacionalmente
relevante para A1.

Define-se a classe equivalente por:

\[
\boxed{K_C=\lceil C_j\rceil\in\{1,2,3,\ldots\}.}
\]

E escolhe-se o representante canônico de implementação:

\[
\boxed{C_j=K_C.}
\]

Para isolar atenção de heterogeneidade de dificuldade, o primeiro A1 congela também:

```text
REQUIRED_WORK_HETEROGENEITY_REGIME = HOMOGENEOUS_FOR_FIRST_A1
required_capacity_units_j = K_C para toda demanda elegível j
K_C >= 1 inteiro
```

Assim:

\[
\boxed{n^{req}_{ij}=K_C}
\]

para toda demanda isolada do primeiro A1.

Isso **não** afirma que demandas reais tenham dificuldade idêntica. É isolamento experimental:
heterogeneidade de workload fica para robustez/sucessor. O valor de `K_C` ainda não é
escolhido; ele é parâmetro exclusivamente instrumental e poderá ser selecionado apenas pelo
benchmark cego autorizado, nunca por `p`, `EH`, `eta_hat`, `D` coletivo ou qualquer outcome.

```text
REQUIRED_WORK_UNIT = OBSERVER_CAPACITY_UNIT
OBSERVER_CAPACITY_UNIT = 1
REQUIRED_WORK_PARAMETER = K_C
REQUIRED_WORK_NUMERIC_STATUS = UNFROZEN_BLIND_INSTRUMENT_CALIBRATION
```
'''
if old not in spec:
    raise RuntimeError('normalized workload block not found')
spec = spec.replace(old, new, 1)

# Clarify demand record field.
spec = spec.replace('required_work = C_j\nremaining_work',
                    'required_work = C_j = K_C\nremaining_work', 1)
spec = spec.replace('`required_work` é `arm-blind`.',
                    '`required_work` é `arm-blind` e, no primeiro A1, constante entre demandas: `required_work=K_C`.', 1)

# Parameter provenance and frozen/pending lists.
spec = spec.replace('BLIND_INSTRUMENT_CALIBRATION_ABENCH0\n  required_work rule/range',
                    'BLIND_INSTRUMENT_CALIBRATION_ABENCH0\n  K_C required opportunities per isolated request', 1)
spec = spec.replace('observer_buffer_capacity_value = NORMALIZED_B_EQUALS_1\nlogical_cycle_commit',
                    'observer_buffer_capacity_value = NORMALIZED_B_EQUALS_1\nrequired_work_heterogeneity_regime = HOMOGENEOUS_FOR_FIRST_A1\nlogical_cycle_commit', 1)
spec = spec.replace('required_work_rule\nrequired_work_range_or_distribution\n',
                    'required_opportunities_per_request_K_C\n', 1)

# Procedure: explicitly carry the single workload integer.
spec = spec.replace('3. preservar `B=1` como normalização de unidade e congelar `eta_EH0`, `lambda_state`, `p_A`, `p_B`, `p_0` e os demais números',
                    '3. preservar `B=1` e workload homogêneo `C_j=K_C` como normalizações/isolamento, e congelar `K_C`, `eta_EH0`, `lambda_state`, `p_A`, `p_B`, `p_0` e os demais números', 1)

specp.write_text(spec, encoding='utf-8')

trace = json.loads(tracep.read_text(encoding='utf-8'))
trace['status'] = 'V2_0_0_DISCRETE_WORKLOAD_NORMALIZATION_FROZEN_PREPUBLICATION'
trace['scientific_run_authorized'] = False
trace['workload_contract'] = {
    'status': 'FROZEN_HOMOGENEOUS_DISCRETE_EQUIVALENCE_CLASS_FIRST_A1',
    'observer_capacity_unit': 1,
    'raw_positive_work_symbol': 'C_j',
    'equivalence_class': 'K_C=ceil(C_j)',
    'representative_execution_value': 'C_j=K_C',
    'K_C_domain': 'positive integers >=1',
    'required_work_heterogeneity_regime': 'HOMOGENEOUS_FOR_FIRST_A1',
    'all_eligible_demands_first_A1': 'required_capacity_units_j=K_C',
    'isolated_required_opportunities': 'n_req_ij=K_C',
    'numeric_status_K_C': 'UNFROZEN_BLIND_INSTRUMENT_CALIBRATION',
    'selected_by_scientific_outcomes': False,
    'scientific_role': 'AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION',
    'derivation': 'With B=1, no partial basal update, FIFO front-job-only service and no spill of unused capacity, completion timing depends on positive C_j only through ceil(C_j).',
    'heterogeneous_workload_disposition': 'SUCCESSOR_OR_ROBUSTNESS_ONLY'
}

# Replace old pending workload fields globally where they represent run numerics.
def transform_list(xs):
    if not isinstance(xs, list):
        return xs
    out = []
    inserted = False
    for x in xs:
        if x in ('required_work_rule','required_work_range_or_distribution'):
            if not inserted:
                out.append('required_opportunities_per_request_K_C')
                inserted = True
            continue
        out.append(x)
    return out

trace['unfrozen_required_before_run'] = transform_list(trace.get('unfrozen_required_before_run', []))

def walk(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get('numerics_pending'), list):
            obj['numerics_pending'] = transform_list(obj['numerics_pending'])
        for k, val in list(obj.items()):
            walk(val)
    elif isinstance(obj, list):
        for val in obj: walk(val)
walk(trace)

pp = trace.get('parameter_provenance_policy')
if isinstance(pp, dict):
    classes = pp.setdefault('classes', {})
    blind = classes.get('BLIND_INSTRUMENT_CALIBRATION_ABENCH0')
    if isinstance(blind, list):
        cleaned=[]
        for x in blind:
            if x in ('required_work_rule_or_range','required_work_rule','required_work_range_or_distribution'):
                continue
            cleaned.append(x)
        if 'required_opportunities_per_request_K_C' not in cleaned:
            cleaned.insert(0,'required_opportunities_per_request_K_C')
        classes['BLIND_INSTRUMENT_CALIBRATION_ABENCH0']=cleaned
    classes['IMPLEMENTATION_NORMALIZATION'] = list(dict.fromkeys(classes.get('IMPLEMENTATION_NORMALIZATION', []) + [
        'observer_buffer_capacity_B_equals_1',
        'WORK_QUANTUM_equals_1_observer_capacity_unit',
        'raw_workload_C_represented_by_integer_equivalence_class_K_C_equals_ceil_C'
    ]))
    classes['EXPERIMENTAL_ISOLATION'] = list(dict.fromkeys(classes.get('EXPERIMENTAL_ISOLATION', []) + [
        'required_work_heterogeneity_regime_HOMOGENEOUS_FOR_FIRST_A1'
    ]))

tracep.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

readmep.write_text('''# HUMH A0/A1 v2.0.0 — estado pré-publicação\n\nA1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` (`ANBC0=FAIL_DERIVATIONAL`).\n\nA1b mantém `D` como candidato auditado, com classificação estrutural `CONDITIONAL_DISCRIMINATIVE` e confirmação ainda não autorizada.\n\nCongelamentos correntes:\n\n- uma demanda elegível por observador/ciclo: `D_i(W)=W`;\n- regime basal homogêneo e ciclo em `SYNCHRONOUS_SNAPSHOT_BARRIER`;\n- capacidade homogênea normalizada: `B_i=1 observer_capacity_unit`;\n- workload do primeiro A1 homogêneo e reduzido exatamente à classe inteira `K_C=ceil(C_j)`, usando `C_j=K_C`; somente `K_C>=1` permanece para calibração cega;\n- basal numérico representado por `eta_EH0` e `lambda_state`;\n- A1b HIGH/LOW pré-atribuído e massa global de oportunidades igual por ciclo;\n- política de proveniência numérica congelada.\n\n`SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n''', encoding='utf-8')

parent_readmep.write_text('''# HUMH — Experimentos de Atenção\n\n`v2.0.0/` é a árvore corrente A0/A1 pré-publicação.\n\n- `ANBC0 = FAIL_DERIVATIONAL`;\n- `A1a = MECHANISM_DEMONSTRATION_ONLY [C1]`;\n- A1b: `D` candidato em auditoria estrutural `CONDITIONAL_DISCRIMINATIVE`;\n- `D_i(W)=W`, regime basal homogêneo e barreira síncrona congelados;\n- `B=1 observer_capacity_unit`; workload homogêneo do primeiro A1 é o inteiro `K_C=ceil(C_j)`;\n- basal numérico reduzido a `eta_EH0` e `lambda_state`;\n- A1b HIGH/LOW fixo e exógeno, níveis ainda pendentes;\n- proveniência dos parâmetros congelada antes de `ABENCH0`;\n- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n\nA teoria exibida pelo site permanece `../../teoria.md`; a cópia em `v2.0.0/02_dependencias/` é a dependência canônica hash-locked.\n''', encoding='utf-8')

spec_sha = sha(specp)
trace_sha = sha(tracep)
lock = json.loads(lockp.read_text(encoding='utf-8'))
lock['publication_state'] = 'REGENERATED_PRE_PUBLICATION_DISCRETE_WORKLOAD_NORMALIZATION_R6'
for a in lock.get('normative_artifacts', []):
    if a.get('path','').endswith('HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'):
        a['sha256'] = spec_sha
    if a.get('path','').endswith('HUMH_A0_A1_Traceabilidade_v2.0.0.json'):
        a['sha256'] = trace_sha
lock['work_unit_normalization'] = 'FROZEN_B_EQUALS_1_OBSERVER_CAPACITY_UNIT'
lock['workload_contract'] = 'FROZEN_HOMOGENEOUS_K_C_EQUALS_CEIL_C_FIRST_A1'
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
