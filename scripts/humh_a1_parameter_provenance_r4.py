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
THEORY_SHA = '3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

spec = specp.read_text(encoding='utf-8')
spec = spec.replace('**Status:** `PRE_CODE_A1B_ASSIGNMENT_AND_ETA_BOUND_FREEZE`',
                    '**Status:** `PRE_CODE_PARAMETER_IDENTIFIABILITY_AND_PROVENANCE_FREEZE`', 1)
old_motive_start = '**Motivo:** '
mi = spec.index(old_motive_start)
me = spec.index('\n', mi)
new_motive = ('**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`. '
              'Em A1b, `D` permanece candidato canônico sob auditoria estrutural. A geração de demanda do primeiro A1 passa a ser fechada em uma requisição exógena por observador por ciclo (`D_i(W)=W`), e a dinâmica basal é reparametrizada apenas para fins numéricos pelos dois graus identificáveis `eta_EH0` e `lambda_state`, sem inventar valores separados de `omega`, `iota_obs` e `kappa` que A1 não identifica. A proveniência permitida para cada número fica congelada antes de qualquer benchmark ou trajetória científica.')
spec = spec[:mi] + new_motive + spec[me:]

# Freeze the canonical preferred demand schedule.
marker = '## 4.2 Atenção coletiva'
if '## 4.1.1 Geração de demanda do primeiro A1 — CONGELADA' not in spec:
    insert = r'''## 4.1.1 Geração de demanda do primeiro A1 — CONGELADA

A definição canônica §11 dá como forma preferencial do primeiro A1 uma requisição
observacional elegível por observador por ciclo lógico. Nesta v2.0.0 essa preferência passa
a ser o contrato executável:

\[
\boxed{D_i(W)=W}
\]

sem ciclos inelegíveis no horizonte primário.

Para cada `observer_id=i` e ciclo `n` é criada exatamente uma demanda:

```text
demand_id = deterministic(observer_id, logical_cycle)
arrival_cycle = n
eligible = true
```

A identidade, conteúdo, `required_work` e deadline dessa demanda são definidos sem consultar
o braço e permanecem idênticos nos braços pareados. O scheduler pode alterar somente as
oportunidades de execução, nunca a geração da demanda.

Status:

```text
FIRST_A1_DEMAND_GENERATION = ONE_ELIGIBLE_REQUEST_PER_OBSERVER_PER_LOGICAL_CYCLE
D_i(W) = W
INELIGIBLE_PRIMARY_CYCLES = NONE
DEMAND_GENERATION_ARM_BLIND = TRUE
```

Esta regra operacionaliza diretamente os §§8–11 da definição canônica e elimina um grau de
liberdade que não precisa ser escolhido numericamente.

---

'''
    spec = spec.replace(marker, insert + marker, 1)

# Add identifiable reparameterization before 7.1.3.
marker = '### 7.1.3. Ausência explícita de atenção na regra'
if '### 7.1.2.2. Reparametrização identificável da dinâmica basal — CONGELADA' not in spec:
    insert = r'''### 7.1.2.2. Reparametrização identificável da dinâmica basal — CONGELADA

A teoria permanece escrita nas variáveis conceituais:

\[
\eta^{(0)}(h)=\frac{\omega}{1+\iota_{obs}+\kappa h},\qquad h=EH\in[0,1].
\]

Entretanto, no regime homogêneo do primeiro A1, a trajetória `p` não identifica
`omega`, `iota_obs` e `kappa` separadamente. Ela depende apenas de dois compostos:

\[
\boxed{\eta_{EH0}=\frac{\omega}{1+\iota_{obs}}}
\]

\[
\boxed{\lambda_{state}=\frac{\kappa}{1+\iota_{obs}}}
\]

pois:

\[
\boxed{
\eta^{(0)}(h)=\frac{\eta_{EH0}}{1+\lambda_{state}h}
}.
\]

`eta_EH0` e `lambda_state` são marcados como
`AUXILIARY_EXPERIMENTAL_REPARAMETERIZATION`: não substituem `omega`, `iota_obs` ou `kappa`
na ontologia da teoria e não são novas hipóteses científicas. Servem somente para não
atribuir precisão fictícia a uma decomposição que A1 não observa.

No primeiro A1:

```text
INDIVIDUAL_OMEGA_IOTA_KAPPA_DECOMPOSITION = NOT_IDENTIFIED_BY_A1
NUMERIC_BASAL_PARAMETERIZATION = eta_EH0 + lambda_state
```

Para a interpretação de resistência estrutural adotada na teoria, usa-se o domínio:

```text
0 < eta_EH0 <= 1
lambda_state >= 0
```

`lambda_state = 0` permanece admissível como submodelo sem resistência estrutural dependente
de `EH`; ele não pode ser excluído apenas porque torna o outcome `D` derivacional em A1b.
Qualquer valor positivo também deve ser congelado prospectivamente por regra independente de
outcomes.

Com `lambda_state>=0`, o critério de preservação reduz-se a `0<eta_EH0<=1`, pois o maior
valor de `eta0` ocorre em `EH=0`.

---

'''
    spec = spec.replace(marker, insert + marker, 1)

# Add provenance firewall before section 26.
marker = '# 26. Itens de desenho e números ainda NÃO congelados'
if '# 25.1. Proveniência e identificabilidade dos parâmetros — CONGELADA' not in spec:
    insert = r'''# 25.1. Proveniência e identificabilidade dos parâmetros — CONGELADA

Nenhum valor numérico pode ser preenchido apenas por conveniência ou porque produz um efeito
científico mais nítido. Antes de qualquer benchmark, congela-se a classe de proveniência
admissível de cada grupo:

```text
CANONICAL_FIXED
  D_i(W)=W
  deadline inclusivo t_complete <= t+L_A
  uma demanda elegível por observador/ciclo
  massa global A1b igual por ciclo
  barreira síncrona

THEORY_CONSTRAINED_NOT_FITTED
  eta_EH0 in (0,1]
  lambda_state >= 0
  p, p_target in [0,1]
  alvo estacionário por episódio

BLIND_INSTRUMENT_CALIBRATION_ABENCH0
  observer_buffer_capacity_value
  required_work rule/range
  L_grid e L_A
  regras/níveis de oportunidades
  q_H, q_L e proporção instrumental A1b
```

A classe `BLIND_INSTRUMENT_CALIBRATION_ABENCH0` só pode usar saídas autorizadas pelos
§§17–20 da definição de atenção: `D_i`, `U_i`, `A_i`, latências, misses, timing de fila/
serviço e metadados de runtime. É proibido consultar `p_i(t)`, `EH`, `eta_hat`, `D`
coletivo, consenso ou qualquer outcome A1 para escolher esses números.

```text
SYNTHETIC_INTEGRITY_OR_POWER_ONLY
  N / tamanho amostral
  competência AETA0/ACOMP0
  regras inferenciais e margens
```

Esses itens podem usar apenas modelos sintéticos/adversariais prospectivos independentes da
trajetória científica e nunca resultados v1.0.x.

```text
SCIENTIFIC_DESIGN_PRECOMMITTED
  eta_EH0_value
  lambda_state_value
  p_A, p_B, p_0
  episódios A/B e W científico
```

Esses valores alteram a própria dinâmica científica e portanto **não** podem ser escolhidos
por ABENCH0 olhando `A`, nem por piloto que exporte `p/EH/outcome`. Devem ser fixados por
regra matemática/teórica prospectiva ou por grade de sensibilidade fechada antes do run.

Finalmente:

```text
omega_value
individual iota_obs_value
individual kappa_value
```

não são números obrigatórios do primeiro A1 enquanto a implementação utilizar a forma
algebricamente equivalente `eta_EH0/(1+lambda_state*EH)`. A1 não separa esses três
componentes; inventar uma decomposição seria falsa identificação.

Status:

```text
PARAMETER_PROVENANCE_POLICY = FROZEN
OUTCOME_GUIDED_PARAMETER_SELECTION = FORBIDDEN
INDIVIDUAL_BASAL_DECOMPOSITION = NOT_REQUIRED_AND_NOT_IDENTIFIED
```

---

'''
    spec = spec.replace(marker, insert + marker, 1)

# Update frozen and pending lists / procedure.
spec = spec.replace('A1b_global_opportunity_mass = MATCHED_PER_LOGICAL_CYCLE\n```',
                    'A1b_global_opportunity_mass = MATCHED_PER_LOGICAL_CYCLE\nfirst_A1_demand_generation = D_i(W)=W\nparameter_provenance_policy = FROZEN\n```', 1)
spec = spec.replace('omega_value\niota_obs_value\nkappa_value\n',
                    'eta_EH0_value\nlambda_state_resistance_value\n', 1)
spec = spec.replace('3. congelar `omega`, `iota_obs`, `kappa`, `B`, `p_A`, `p_B`, `p_0` e os demais números\n   basais por critérios teóricos/técnicos independentes de outcomes A1;',
                    '3. congelar `eta_EH0`, `lambda_state`, `B`, `p_A`, `p_B`, `p_0` e os demais números\n   por suas classes de proveniência prospectivamente autorizadas, sem inventar decomposição separada de `omega/iota_obs/kappa`;', 1)

specp.write_text(spec, encoding='utf-8')

trace = json.loads(tracep.read_text(encoding='utf-8'))
trace['status'] = 'V2_0_0_PARAMETER_IDENTIFIABILITY_AND_PROVENANCE_FROZEN_PREPUBLICATION'
trace['scientific_run_authorized'] = False

trace['demand_generation_contract'] = {
    'status': 'FROZEN_ONE_ELIGIBLE_REQUEST_PER_OBSERVER_PER_LOGICAL_CYCLE',
    'formula': 'D_i(W)=W',
    'ineligible_primary_cycles': 'NONE',
    'demand_id_rule': 'deterministic(observer_id, logical_cycle)',
    'arm_blind': True,
    'paired_identity_required': True,
    'canonical_refs': [
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':8,'clause_or_statement':'D_i is exogenous observational demand.'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':9,'clause_or_statement':'Changing attention arm cannot change number, identity or content of requests.'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':11,'clause_or_statement':'Preferred first A1 demand generation is one eligible request per observer per logical cycle, yielding D_i(W)=W.'}
    ]
}

trace['basal_identifiable_reparameterization'] = {
    'status': 'FROZEN_AUXILIARY_EXPERIMENTAL_REPARAMETERIZATION',
    'canonical_form': 'eta0(EH)=omega/(1+iota_obs+kappa*EH)',
    'eta_EH0': 'omega/(1+iota_obs)',
    'lambda_state': 'kappa/(1+iota_obs)',
    'execution_equivalent_form': 'eta0(EH)=eta_EH0/(1+lambda_state*EH)',
    'individual_decomposition_identified_by_A1': False,
    'individual_omega_iota_kappa_values_required_for_execution': False,
    'admissible_domain': {'eta_EH0':'0 < eta_EH0 <= 1','lambda_state':'lambda_state >= 0'},
    'lambda_zero_is_allowed_nested_submodel': True,
    'anti_rescue': 'lambda_state=0 cannot be excluded merely to avoid a derivational A1b classification.',
    'scientific_role': 'AUXILIARY_EXPERIMENTAL_REPARAMETERIZATION',
    'canonical_refs': [
        {'artifact_id':'HUMH_THEORY_CANONICAL','sha256':THEORY_SHA,'section':'4.2.3-4.2.5','clause_or_statement':'Basal convergence uses eta=omega/(1+iota_obs+iota_ord), with proposed iota_ord=kappa*EH and observer/structural resistances conceptually distinct.'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':37,'clause_or_statement':'Basal attention-free dynamics eta0=omega/(1+iota_obs+kappa*EH).'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':33,'clause_or_statement':'Attention and observer inertia are distinct; A_i is not 1/iota_obs.'}
    ]
}

trace['parameter_provenance_policy'] = {
    'status': 'FROZEN_PRE_BENCHMARK',
    'outcome_guided_parameter_selection': 'FORBIDDEN',
    'classes': {
        'CANONICAL_FIXED': ['D_i(W)=W','deadline_inclusive','one_request_per_observer_cycle','A1b_global_opportunity_mass_matched_per_cycle','synchronous_snapshot_barrier'],
        'THEORY_CONSTRAINED_NOT_FITTED': ['eta_EH0_domain','lambda_state_domain','p_domain','stationary_target_semantics'],
        'BLIND_INSTRUMENT_CALIBRATION_ABENCH0': ['observer_buffer_capacity_value','required_work_rule_or_range','L_grid','L_A','opportunity_candidate_rules_and_levels','A1b_q_H','A1b_q_L','A1b_stratum_proportion'],
        'SYNTHETIC_INTEGRITY_OR_POWER_ONLY': ['N_or_sample_size','AETA0_competence','ACOMP0_competence','inferential_rules_and_margins'],
        'SCIENTIFIC_DESIGN_PRECOMMITTED': ['eta_EH0_value','lambda_state_value','p_A','p_B','p_0','target_episode_design','W']
    },
    'ABENCH0_allowed_observables': ['D_i','U_i','A_i','update_latency_distribution','deadline_misses','queue_service_timing','runtime_metadata','hardwareConcurrency'],
    'ABENCH0_forbidden_observables': ['eta_hat','p_i(t)','EH','belief_dispersion','consensus','D_collective','attractor_outcomes','any_A1a_or_A1b_outcome'],
    'v1_outcomes_may_select_parameters': False,
    'canonical_refs': [
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':17,'clause_or_statement':'ABENCH0 is a blind instrumentation benchmark before the scientific run.'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':18,'clause_or_statement':'ABENCH0 allowed outputs are technical/instrumental only.'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':19,'clause_or_statement':'Scientific trajectory/outcome quantities are forbidden in ABENCH0.'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':20,'clause_or_statement':'Candidate grid and deterministic selection criteria must be frozen before ABENCH0.'}
    ]
}

# Replace unfrozen scalar decomposition with identifiable composites.
uf = trace.get('unfrozen_required_before_run', [])
newuf = []
for x in uf:
    if x in ('omega_value','iota_obs_value','kappa_value'):
        continue
    newuf.append(x)
insert_at = 2 if len(newuf) >= 2 else len(newuf)
for name in reversed(['eta_EH0_value','lambda_state_resistance_value']):
    if name not in newuf:
        newuf.insert(insert_at, name)
trace['unfrozen_required_before_run'] = newuf

# Align stale nested B heterogeneity status with the already-frozen first-A1 homogeneous regime.
def walk(obj):
    if isinstance(obj, dict):
        if 'observer_processing_capacity' in obj and isinstance(obj['observer_processing_capacity'], dict):
            opc = obj['observer_processing_capacity']
            hr = opc.get('heterogeneity_regime')
            if isinstance(hr, dict):
                hr['status'] = 'FROZEN_HOMOGENEOUS_FOR_FIRST_A1'
                hr['allowed_regimes_for_first_A1'] = ['HOMOGENEOUS']
                hr['heterogeneous_regime_disposition'] = 'SUCCESSOR_OR_ROBUSTNESS_ONLY'
        for val in obj.values(): walk(val)
    elif isinstance(obj, list):
        for val in obj: walk(val)
walk(trace)

base = trace.get('first_A1_baseline_regime')
if isinstance(base, dict):
    base['omega_i'] = 'conceptual theory variable; common across observers; not separately identified numerically by A1'
    base['iota_obs_i'] = 'conceptual theory variable; common across observers; not separately identified numerically by A1'
    base['kappa'] = 'conceptual theory variable; common system coefficient; not separately identified numerically by A1'
    base['numeric_execution_parameterization'] = 'eta_EH0 + lambda_state'
    base['individual_decomposition_status'] = 'NOT_IDENTIFIED_BY_A1_AND_NOT_REQUIRED_FOR_EXECUTION'

tracep.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Update package README and parent README.
readmep.write_text('''# HUMH A0/A1 v2.0.0 — estado pré-publicação\n\nA1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` (`ANBC0=FAIL_DERIVATIONAL`).\n\nA1b mantém `D` como candidato auditado, com classificação estrutural `CONDITIONAL_DISCRIMINATIVE` e confirmação ainda não autorizada.\n\nCongelamentos correntes:\n\n- primeiro A1 basal e `B_i` homogêneos por isolamento;\n- ciclo científico em `SYNCHRONOUS_SNAPSHOT_BARRIER`;\n- exatamente uma demanda elegível por observador/ciclo: `D_i(W)=W`;\n- admissibilidade basal e reparametrização identificável: `eta0(EH)=eta_EH0/(1+lambda_state*EH)`, com `0<eta_EH0<=1` e `lambda_state>=0`;\n- `omega`, `iota_obs` e `kappa` continuam conceitos teóricos, mas sua decomposição numérica individual não é identificada nem exigida por A1;\n- A1b usa estratos HIGH/LOW pré-atribuídos, fixos durante `W`, com massa global de oportunidades igual por ciclo;\n- política de proveniência numérica congelada: calibração instrumental só pode usar saídas cegas permitidas por `ABENCH0`;\n- valores científicos e instrumentais ainda pendentes não podem ser escolhidos por outcomes v1.0.x/A1.\n\n`SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n''', encoding='utf-8')

parent_readmep.write_text('''# HUMH — Experimentos de Atenção\n\n`v2.0.0/` é a árvore corrente A0/A1 pré-publicação.\n\n- `ANBC0 = FAIL_DERIVATIONAL`;\n- `A1a = MECHANISM_DEMONSTRATION_ONLY [C1]`;\n- A1b: `D` candidato em auditoria estrutural `CONDITIONAL_DISCRIMINATIVE`;\n- regime basal/B homogêneo e barreira síncrona congelados;\n- demanda primária congelada em `D_i(W)=W`;\n- dinâmica basal numericamente reduzida aos compostos identificáveis `eta_EH0` e `lambda_state`, sem falsa decomposição de `omega/iota_obs/kappa`;\n- semântica A1b HIGH/LOW fixa e exógena congelada, níveis ainda pendentes;\n- proveniência dos parâmetros congelada antes de `ABENCH0`;\n- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n\nA teoria exibida pelo site permanece `../../teoria.md`; a cópia em `v2.0.0/02_dependencias/` é a dependência canônica hash-locked.\n''', encoding='utf-8')

spec_sha = sha(specp)
trace_sha = sha(tracep)

lock = json.loads(lockp.read_text(encoding='utf-8'))
lock['publication_state'] = 'REGENERATED_PRE_PUBLICATION_PARAMETER_IDENTIFIABILITY_AND_PROVENANCE_R4'
for a in lock.get('normative_artifacts', []):
    if a.get('path','').endswith('HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'):
        a['sha256'] = spec_sha
    if a.get('path','').endswith('HUMH_A0_A1_Traceabilidade_v2.0.0.json'):
        a['sha256'] = trace_sha
lock['parameter_identifiability'] = 'FROZEN_ETA_EH0_PLUS_LAMBDA_STATE'
lock['demand_generation'] = 'FROZEN_D_i_EQUALS_W'
lock['parameter_provenance_policy'] = 'FROZEN_PRE_BENCHMARK'
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
