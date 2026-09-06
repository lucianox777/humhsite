from pathlib import Path
import hashlib, json

root = Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v = root / 'v2.0.0'
specp = v / '01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep = v / '01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
readmep = v / 'README.md'
parent_readme = root / 'README.md'
lockp = v / '02_dependencias/DEPENDENCIES.lock.json'
sumsp = v / '03_integridade/SHA256SUMS.txt'
rootsha = v / 'HUMH_A0_A1_v2.0.0.sha256'

NUCLEUS_SHA = 'baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b'
THEORY_SHA = '3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b'
ATT_SHA = '3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

spec = specp.read_text(encoding='utf-8')

spec = spec.replace('**Status:** `PRE_CODE_A1B_DERIVATIONAL_AUDIT`', '**Status:** `PRE_CODE_A1B_STRUCTURAL_AUDIT`')
old_motivo_start = '**Motivo:** '
line_start = spec.index(old_motivo_start)
line_end = spec.index('\n', line_start)
new_motivo = ('**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`. '
              'A auditoria de A1b foi refinada: `D` continua candidato canônico, mas `D_A` determina apenas a quantidade total de conclusões por observador, não a exposição temporal aos fatores de atualização dependentes do estado coletivo. '
              'Para impedir que ordem física de WebWorkers se torne variável científica, congela-se uma barreira síncrona por ciclo lógico e um regime basal homogêneo para o primeiro A1. A classificação final de `ADIST0` continua anterior a qualquer trajetória científica.')
spec = spec[:line_start] + new_motivo + spec[line_end:]

# Freeze B_i homogeneous for the first A1.
a = spec.index('Observadores diferentes podem possuir `B_i` diferentes.')
b = spec.index('## 5.1.2. Trabalho exigido pela tarefa', a)
new_b = r'''Para a teoria geral, observadores poderiam possuir capacidades auxiliares diferentes.
Entretanto, no **primeiro A1** congela-se prospectivamente:

```text
OBSERVER_BUFFER_HETEROGENEITY_REGIME = HOMOGENEOUS_FROZEN_FOR_FIRST_A1
B_i = B para todo observador i
```

A escolha é de **isolamento experimental**, não uma afirmação ontológica da HUMH: `B_i`
é operacionalização computacional auxiliar e sua heterogeneidade acrescentaria uma segunda
fonte de variação à distribuição de atenção que A1 pretende isolar.

O valor numérico de `B` permanece `UNFROZEN_REQUIRED_BEFORE_RUN` e não poderá ser
selecionado com base em outcomes v1.0.x ou em qualquer outcome A1.

`B_i` continua não sendo atenção, não é `P_i_obs` e não pode entrar como outcome ou
resgate explicativo. Heterogeneidade de `B_i` fica reservada para robustez/sucessor
prospectivo, sem reclassificar o primeiro A1.

'''
spec = spec[:a] + new_b + spec[b:]

# Insert synchronous logical-cycle semantics before channel section.
marker = '# 6. Dois canais de mensuração — separação obrigatória'
insert = r'''## 5.1.14. Barreira síncrona do ciclo lógico — CONGELADA

O tempo científico já é o ciclo lógico e `wall_clock_ms` é diagnóstico. Para que a ordem
física de execução de WebWorkers não altere a trajetória científica, congela-se uma
operacionalização auxiliar de commit síncrono:

```text
LOGICAL_CYCLE_COMMIT = SYNCHRONOUS_SNAPSHOT_BARRIER
OS_INTERLEAVING = DIAGNOSTIC_ONLY
```

Para cada ciclo lógico `n`:

```text
1. congelar o vetor pre-state p_i[n] de todos os observadores;
2. calcular p_bar[n] e EH[n] somente a partir desse snapshot;
3. executar serviço/fila/oportunidades e registrar quantas demandas de cada observador
   completaram validamente no ciclo: k_i[n];
4. para cada observador, aplicar localmente suas k_i[n] atualizações na ordem FIFO,
   usando o mesmo EH[n] e o mesmo p_target do episódio para todas as atualizações desse ciclo;
5. nenhum observador lê p_j já atualizado no mesmo ciclo;
6. publicar simultaneamente todos os p_i[n+1] após a barreira;
7. somente p[n+1] pode influenciar EH[n+1].
```

Se `k_i[n]>1`, a sequência local preserva a regra já congelada de uma atualização por
demanda concluída; somente o **estado coletivo EH** permanece o snapshot de início do
ciclo. Assim o resultado não depende da ordem de mensagens entre threads.

Status:

```text
SCIENTIFIC_CYCLE_SEMANTICS = FROZEN_SYNCHRONOUS_SNAPSHOT
CROSS_OBSERVER_UPDATE_ORDER = NON_SCIENTIFIC
```

Esta regra é `AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION`, necessária para materializar a
formulação discreta em múltiplos observadores. Ela não altera `A_i`, H-A1S ou a teoria.

---

'''
if insert not in spec:
    spec = spec.replace(marker, insert + marker, 1)

# Freeze homogeneous basal-observer regime after the basal update rule.
marker = '### 7.1.3. Ausência explícita de atenção na regra'
idx = spec.index(marker)
end = spec.index('\n---\n\n## 7.2.', idx)
block = spec[idx:end]
if '### 7.1.4. Regime basal do primeiro A1' not in block:
    add = r'''

### 7.1.4. Regime basal do primeiro A1 — HOMOGÊNEO

Para isolar a distribuição de atenção de diferenças basais entre observadores, congela-se
prospectivamente no primeiro A1:

```text
omega_i = omega para todo i
iota_obs_i = iota_obs para todo i
kappa = comum ao sistema
p_i(0) = p_0 comum dentro de cada episódio pareado
B_i = B para todo i
```

Os valores numéricos de `omega`, `iota_obs`, `kappa`, `p_0` e `B` continuam a ser
congelados antes do run por critérios teóricos/técnicos independentes de outcomes.

A homogeneidade é uma escolha de isolamento experimental e **não** afirma que observadores
reais sejam homogêneos. Heterogeneidade basal será hipótese/robustez sucessora se for
investigada.
'''
    spec = spec[:end] + add + spec[end:]

# Replace A1b section 17 with the corrected derivation.
a = spec.index('# 17. Outcome primário de A1b')
b = spec.index('# 18. Gates — lista fechada')
section17 = r'''# 17. Outcome primário de A1b — candidato canônico e auditoria estrutural

A primeira métrica coletiva candidata permanece a divergência interobservador já definida
no núcleo canônico 1.9-A:

\[
\boxed{
D=\frac1N\sum_i|p_i-\bar p|.
}
\]

Ela é distinta de `D_i` (demanda observacional) e de `D_A` (heterogeneidade de atenção).
O núcleo 1.9-A, A4, congela `D` justamente para distinguir estruturas interobservador que
podem compartilhar o mesmo `EH`; A9 usa estados de `EH` semelhante e `D` diferente como
teste adversarial de suficiência estrutural.

Status:

```text
A1B_PRIMARY_OUTCOME_CANDIDATE = STATE_DIVERGENCE_D
CANDIDATE_STATUS = FROZEN_FOR_STRUCTURAL_AUDIT_NOT_YET_AUTHORIZED
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
```

## 17.1. Correção da auditoria: `D_A` não determina sozinho o estado final

Sob o regime homogêneo do primeiro A1 e a barreira síncrona, defina no ciclo `n`:

\[
\eta_n
=
\frac{\omega}
{1+\iota_{obs}+\kappa EH[n]}
\]

e:

\[
r_n=1-\eta_n.
\]

Com `0<eta_n<=1` e alvo comum, a distância de um observador ao atrator depois de
`k_i[n]` conclusões válidas naquele ciclo é multiplicada por `r_n^{k_i[n]}`. Logo:

\[
\boxed{
|p_{target}-p_i[W]|
=
|p_{target}-p_0|
\prod_n r_n^{k_i[n]}.
}
\]

A atenção mede o total de conclusões válidas no horizonte:

\[
A_i=\frac{U_i}{D_i},
\qquad
U_i=\sum_n k_i[n].
\]

Portanto, `A_i` fixa a **contagem total** `U_i`, mas não fixa quais fatores temporais
`r_n` compõem o produto. Quando `EH[n]` varia e `kappa != 0`, a mesma contagem pode ter
efeito diferente em ciclos distintos; reciprocamente, contagens diferentes podem, em
princípio, produzir produtos iguais.

Consequência:

```text
D_A != 0  -/->  D != 0 como identidade algébrica geral da construção
A_bar + D_A não determinam sozinhos D(W)
```

A formulação anterior que tratava `p_i(W)=F^{U_i}(p_0)` com um único mapa escalar fixo era
forte demais: ela ignorava que `eta0` contém `EH`, que é estado coletivo e pode variar
entre ciclos.

## 17.2. Submodelo em que o efeito é derivacional

Se os fatores de atualização forem constantes no horizonte, por exemplo no caso aninhado
`kappa=0` ou em uma condição que torne `EH[n]` efetivamente constante, então:

\[
r_n=r
\]

e:

\[
|p_{target}-p_i[W]|=|p_{target}-p_0|r^{U_i}.
\]

Para `0<r<1`, diferenças em `U_i` produzem deterministicamente diferenças de estado.
Nesse submodelo, usar `D` como evidência confirmatória de A1b seria derivacional.

Portanto a auditoria deve distinguir:

```text
CONSTANT_UPDATE_FACTOR_REGIME -> DERIVATIONALLY_FORCED_FOR_D
STATE_DEPENDENT_UPDATE_FACTOR_REGIME -> NOT_ALGEBRAICALLY_FORCED_BY_D_A_ALONE
```

## 17.3. Controle temporal obrigatório do instrumento A1b

Para que A1b teste distribuição **entre observadores** e não uma alteração do volume global
de recurso ao longo do tempo, os braços pareados devem satisfazer, em cada ciclo lógico:

\[
\boxed{
\sum_i P^{obs}_{i,UNIFORM}(n)
=
\sum_i P^{obs}_{i,HETEROGENEOUS}(n).
}
\]

Status:

```text
A1B_GLOBAL_OPPORTUNITY_MASS = MATCHED_PER_LOGICAL_CYCLE
A1B_ASSIGNMENT_RULE = EXOGENOUS_ARM_RULE_ONLY
A1B_REACTIVE_REALLOCATION = FORBIDDEN
```

A regra específica de distribuição das oportunidades entre observadores e seus níveis
numéricos ainda será congelada antes do run. Ela não pode consultar `p_i`, `EH`, sucesso,
fila, deadline miss, `eta_hat`, `D`, consenso ou qualquer outcome.

Com a barreira síncrona, diferenças de wall-clock, ordem de mensagens ou velocidade de
threads não podem criar um efeito espúrio de distribuição.

## 17.4. Classificação prospectiva atual de ADIST0

O estado correto antes dos valores basais e da regra instrumental final é:

```text
ADIST0.DERIVATIONAL_CONTENT_AUDIT_STRUCTURAL =
    CONDITIONAL_DISCRIMINATIVE

ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL =
    PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE

ADIST0_CONFIRMATORY = NOT_AUTHORIZED
```

`CONDITIONAL_DISCRIMINATIVE` significa que a construção **não contém uma identidade geral**
`D_A -> D`, mas possui subdomínios admissíveis em que um efeito em `D` é derivacional.
A classificação final deve ser repetida depois de congelados `omega`, `iota_obs`, `kappa`,
`B`, `p_0`, `L_A`, `W` e a regra exata de distribuição temporal de oportunidades, sempre
antes da primeira trajetória científica.

## 17.5. Regra anti-resgate

Nenhum parâmetro poderá ser escolhido com o objetivo de converter a classificação final em
`DISCRIMINATIVE`. O regime será congelado por critérios teóricos/técnicos independentes.

Se, depois desse congelamento, `D` cair em regime derivacional:

```text
A1b = MECHANISM_DEMONSTRATION_ONLY [C1]
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
```

Se permanecer não forçado e todos os demais Gates forem satisfeitos, `D` poderá então ser
promovido de **candidato auditado** a outcome primário confirmatório de A1b.

A restrição temporal permanece:

```text
A1B_DERIVATIONAL_AUDIT_FINAL_MUST_PRECEDE_FIRST_SCIENTIFIC_TRAJECTORY
```

---

'''
spec = spec[:a] + section17 + spec[b:]

# Ensure ADIST0 subchecks include temporal/cycle controls.
old = '''ADIST0
  .DERIVATIONAL_CONTENT_AUDIT
  .ATTENTION_TO_OBSERVER_ASSIGNMENT_INDEPENDENCE
'''
new = '''ADIST0
  .DERIVATIONAL_CONTENT_AUDIT
  .ATTENTION_TO_OBSERVER_ASSIGNMENT_INDEPENDENCE
  .GLOBAL_OPPORTUNITY_MASS_MATCHED_PER_CYCLE
  .LOGICAL_CYCLE_SNAPSHOT_INVARIANCE
'''
if old in spec:
    spec = spec.replace(old, new, 1)

# Replace section 26-27 with current freeze status.
a = spec.index('# 26. Itens de desenho e números ainda NÃO congelados')
b = spec.index('# 28. Regra automática de rastreabilidade para o código')
sec2627 = r'''# 26. Itens de desenho e números ainda NÃO congelados

Já estão congelados prospectivamente no primeiro A1:

```text
observer_basal_parameter_regime = HOMOGENEOUS
observer_buffer_capacity_heterogeneity_regime = HOMOGENEOUS
logical_cycle_commit = SYNCHRONOUS_SNAPSHOT_BARRIER
A1b_global_opportunity_mass = MATCHED_PER_LOGICAL_CYCLE
```

Permanecem `UNFROZEN_REQUIRED_BEFORE_RUN`:

```text
N
W
basal_eta0_bound_admissibility
omega_value
iota_obs_value
kappa_value
observer_buffer_capacity_value
required_work_rule
required_work_range_or_distribution
p_A
p_B
p_0_or_initialization_value
number_of_target_episodes
A_B_episode_balance_and_order
target_episode_length
target_stationarity_certification
L_grid
regras instrumentais candidatas de ABENCH0
critérios instrumentais de ABENCH0
L_A
number_of_arms
instrumental_contrast_criteria
saturation_avoidance_criteria
attention_to_observer_assignment_rule_A1b
A1b_per_cycle_opportunity_levels
ADIST0_final_derivational_classification
margem de matching de A_bar
diferença mínima de D_A
margem de efeito A1b
regra inferencial A1b
tamanho amostral/poder
```

Nenhum campo pode ser preenchido com base em outcomes científicos da série v1.0.x nem
escolhido para obter uma classificação desejada em `ANBC0` ou `ADIST0`.

A microdinâmica basal continua fechada:

```text
A1A_OBSERVER_MICRODYNAMIC =
  FROZEN_CANONICAL_DISCRETE_WITH_AUXILIARY_COMPLETION_MAPPING
ANBC0 = FAIL_DERIVATIONAL
```

---

# 27. Procedimento autorizado daqui até run-ready

A ordem prospectiva passa a ser:

1. preservar a microdinâmica basal já congelada e `ANBC0=FAIL_DERIVATIONAL`;
2. preservar o regime homogêneo e a barreira síncrona já congelados por isolamento;
3. congelar `omega`, `iota_obs`, `kappa`, `B`, `p_A`, `p_B`, `p_0` e os demais números
   basais por critérios teóricos/técnicos independentes de outcomes A1;
4. certificar `0 < eta0 <= 1` em todo estado admissível, sem clamp pós-hoc;
5. congelar a regra exata A1b mantendo a massa global de oportunidades igual em cada
   ciclo e variando somente sua distribuição entre observadores;
6. repetir `ADIST0.DERIVATIONAL_CONTENT_AUDIT` com o regime completo congelado;
7. aceitar a classificação obtida: se derivacional, A1b fica demonstração de mecanismo;
   se discriminativa, congelar margens, inferência e poder;
8. executar `AETA0`, `ABENCH0`, `AMAN0`, `AISO0` e `AINT0` sem tuning por outcomes;
9. manter `v2.0.0` enquanto o objeto continuar pré-publicação e regenerar hashes a cada
   alteração normativa.

---

'''
spec = spec[:a] + sec2627 + spec[b:]

spec = spec.replace('ADIST0.DERIVATIONAL_CONTENT_AUDIT_PRENUMERIC = CONDITIONAL_NOT_GLOBALLY_FORCED',
                    'ADIST0.DERIVATIONAL_CONTENT_AUDIT_STRUCTURAL = CONDITIONAL_DISCRIMINATIVE')
spec = spec.replace('ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = PENDING_BASAL_REGIME_AND_ASSIGNMENT_RULE',
                    'ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE')
spec = spec.replace('NEXT = FREEZE_BASAL_OBSERVER_REGIME_AND_COMPLETE_ADIST0_DERIVATIONAL_AUDIT',
                    'NEXT = FREEZE_BASAL_NUMERICS_AND_A1B_ASSIGNMENT_THEN_COMPLETE_ADIST0_DERIVATIONAL_AUDIT')

specp.write_text(spec, encoding='utf-8')

# ---- trace ----
tr = json.loads(tracep.read_text(encoding='utf-8'))
tr['status'] = 'V2_0_0_A1B_STRUCTURAL_AUDIT_CYCLE_SEMANTICS_FROZEN_PREPUBLICATION'
tr['scientific_run_authorized'] = False

tr['first_A1_baseline_regime'] = {
    'status': 'FROZEN_HOMOGENEOUS_FOR_FIRST_A1',
    'omega_i': 'omega common to all observers; numeric value pending',
    'iota_obs_i': 'iota_obs common to all observers; numeric value pending',
    'kappa': 'common system parameter; numeric value pending',
    'initial_state': 'p_i(0)=p_0 common within paired episode; numeric value pending',
    'observer_buffer_capacity': 'B_i=B common to all observers; numeric value pending',
    'scientific_role': 'EXPERIMENTAL_ISOLATION_CHOICE',
    'not_theory_claim_of_real_observer_homogeneity': True,
    'outcome_based_selection_forbidden': True
}

tr['logical_cycle_commit_semantics'] = {
    'status': 'FROZEN_SYNCHRONOUS_SNAPSHOT_BARRIER',
    'kind': 'AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION',
    'scientific_time': 'logical_cycle',
    'pre_state': 'freeze full p_i[n] vector at cycle start',
    'EH_snapshot': 'compute EH[n] from pre-state only',
    'service': 'service queues/opportunities and count k_i[n] valid completions',
    'local_updates': 'per observer FIFO; all completions in cycle use same EH[n] and episode p_target',
    'publish': 'simultaneous p_i[n+1] barrier commit',
    'cross_observer_OS_interleaving': 'DIAGNOSTIC_ONLY',
    'canonical_refs': [
        {'artifact_id':'HUMH_THEORY_CANONICAL','sha256':THEORY_SHA,'section':'4.4.2','clause_or_statement':'Discrete computational formulation p[n+1]=p[n]+eta*(p*-p[n]).'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':25,'clause_or_statement':'Initial A1 uses logical control rather than non-portable OS/WebWorker priority.'},
        {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT_SHA,'section':98,'clause_or_statement':'CPU/event-loop/global load are diagnostic only.'}
    ]
}

tr['a1b_derivational_audit'] = {
    'id': 'ADIST0_DERIVATIONAL_CONTENT_AUDIT',
    'kind': 'GATE_SUBCHECK',
    'parent_gate': 'ADIST0',
    'status_structural': 'CONDITIONAL_DISCRIMINATIVE',
    'status_final': 'PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE',
    'primary_outcome_candidate': {
        'id': 'STATE_DIVERGENCE_D',
        'formula': 'D=(1/N)*sum_i |p_i-p_bar|',
        'status': 'FROZEN_FOR_STRUCTURAL_AUDIT_NOT_YET_AUTHORIZED',
        'canonical_refs': [
            {'artifact_id':'HUMH_NUCLEUS_CANONICAL','sha256':NUCLEUS_SHA,'section':'A4','clause_or_statement':'Defines interobserver divergence D=(1/N) sum_i |p_i-p_bar| and distinguishes it from EH.'},
            {'artifact_id':'HUMH_NUCLEUS_CANONICAL','sha256':NUCLEUS_SHA,'section':'A9','clause_or_statement':'N1b adversarially compares similar EH with different D.'}
        ]
    },
    'corrected_derivation': {
        'eta_n': 'omega/(1+iota_obs+kappa*EH[n]) under homogeneous first-A1 regime',
        'r_n': '1-eta_n',
        'k_i_n': 'number of valid demand completions for observer i in logical cycle n',
        'distance_product': '|p_target-p_i[W]|=|p_target-p_0|*product_n r_n^(k_i[n])',
        'attention_only_fixes_total_count': 'U_i=sum_n k_i[n]; A_i=U_i/D_i',
        'implication': 'A_i and D_A do not determine which time-varying r_n factors are experienced',
        'previous_fixed_map_claim_retracted': True
    },
    'forced_submodel': {
        'condition': 'r_n constant over the horizon, e.g. kappa=0 or effectively constant EH',
        'consequence': '|p_target-p_i[W]|=|p_target-p_0|*r^(U_i)',
        'classification_for_D': 'DERIVATIONALLY_FORCED_FOR_D when 0<r<1'
    },
    'general_state_dependent_case': {
        'condition': 'r_n varies with collective EH[n]',
        'classification': 'NOT_ALGEBRAICALLY_FORCED_BY_D_A_ALONE'
    },
    'instrument_isolation': {
        'per_cycle_global_opportunity_mass': 'MATCHED_BETWEEN_A1B_ARMS',
        'formula': 'sum_i Pobs_i_uniform[n] = sum_i Pobs_i_heterogeneous[n] for every n',
        'assignment': 'EXOGENOUS_ARM_RULE_ONLY',
        'reactive_reallocation': 'FORBIDDEN',
        'wall_clock_order_effect': 'FORBIDDEN_BY_SYNCHRONOUS_BARRIER'
    },
    'confirmatory_authorized': False,
    'final_audit_must_precede_first_scientific_trajectory': True,
    'anti_rescue': 'Parameters cannot be selected to obtain a desired derivational classification.'
}

# ADIST0 subchecks.
sc = tr.setdefault('subchecks_only', {}).setdefault('ADIST0', [])
for x in ['DERIVATIONAL_CONTENT_AUDIT','ATTENTION_TO_OBSERVER_ASSIGNMENT_INDEPENDENCE','GLOBAL_OPPORTUNITY_MASS_MATCHED_PER_CYCLE','LOGICAL_CYCLE_SNAPSHOT_INVARIANCE']:
    if x not in sc: sc.append(x)

# Replace pending list with the current scalar/final design fields.
tr['unfrozen_required_before_run'] = [
    'N','W','basal_eta0_bound_admissibility','omega_value','iota_obs_value','kappa_value',
    'observer_buffer_capacity_value','required_work_rule','required_work_range_or_distribution',
    'p_A','p_B','p_0_or_initialization_value','number_of_target_episodes','A_B_episode_balance_and_order',
    'target_episode_length','target_stationarity_certification','L_grid','ABENCH0_opportunity_candidate_rules',
    'ABENCH0_technical_criteria','L_A','number_of_arms','instrumental_contrast_criteria',
    'saturation_avoidance_criteria','attention_to_observer_assignment_rule_A1b','A1b_per_cycle_opportunity_levels',
    'ADIST0_final_derivational_classification','A1b_Abar_matching_margin','A1b_min_DA_difference',
    'A1b_material_effect_margin','A1b_inference_rule','sample_size_power'
]

if 'A1b' in tr.get('result_logic', {}):
    a1b = tr['result_logic']['A1b']
    a1b['primary_outcome_candidate'] = 'STATE_DIVERGENCE_D'
    a1b['candidate_status'] = 'FROZEN_FOR_STRUCTURAL_AUDIT_NOT_YET_AUTHORIZED'
    a1b['derivational_audit_structural'] = 'CONDITIONAL_DISCRIMINATIVE'
    a1b['derivational_audit_final'] = 'PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE'
    a1b['current_confirmatory_authorization'] = False

tr.setdefault('scientific_sequence', {})['A1b_continuation_condition'] = (
    'Freeze basal numerics and the exogenous A1b assignment rule with per-cycle global opportunity mass matched, '
    'then repeat ADIST0 derivational audit before any scientific trajectory.'
)
tr['next_version'] = (
    'Keep v2.0.0 while unpublished. First-A1 basal regime and synchronous logical-cycle commit are frozen. '
    'Next freeze basal numeric values and the A1b assignment schedule without outcome tuning, then complete ADIST0.'
)
tr.setdefault('prepublication_amendments', []).append({
    'id':'V2_0_0_PREPUBLICATION_A1B_STRUCTURAL_AUDIT_R2',
    'scientific_version_bump':False,
    'changes':[
        'corrected over-strong fixed-map derivation for A1b D candidate',
        'froze homogeneous first-A1 basal and buffer regime for isolation',
        'froze synchronous logical-cycle snapshot/barrier semantics so OS/WebWorker ordering is non-scientific',
        'required per-cycle global opportunity mass matching between A1b arms',
        'classified structural A1b audit as CONDITIONAL_DISCRIMINATIVE with final classification pending frozen numerics and assignment rule'
    ]
})

tracep.write_text(json.dumps(tr, ensure_ascii=False, indent=2), encoding='utf-8')

# Readmes.
readmep.write_text('''# HUMH A0/A1 v2.0.0 — estado pré-publicação\n\nA1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` porque `ANBC0=FAIL_DERIVATIONAL`.\n\n## A1b — auditoria estrutural\n\n`D=(1/N) sum_i |p_i-p_bar|` permanece o primeiro candidato canônico, ainda não autorizado como outcome confirmatório.\n\nCorreção importante: `D_A` fixa a heterogeneidade das contagens totais de atendimento, mas não determina sozinho o produto dos fatores de atualização quando `eta0` varia com `EH[n]`. Logo não existe identidade algébrica geral `D_A -> D`. Em submodelos com fator de atualização constante, porém, um efeito em `D` é derivacional.\n\nEstado:\n\n- `ADIST0.DERIVATIONAL_CONTENT_AUDIT_STRUCTURAL = CONDITIONAL_DISCRIMINATIVE`\n- `ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE`\n- `ADIST0_CONFIRMATORY = NOT_AUTHORIZED`\n- primeiro A1: observadores/buffer basais homogêneos por isolamento; valores numéricos pendentes;\n- ciclo científico: `SYNCHRONOUS_SNAPSHOT_BARRIER`; ordem física de WebWorkers é diagnóstica;\n- A1b deve igualar a massa global de oportunidades em cada ciclo e variar apenas sua distribuição entre observadores.\n\n`scientific_run_authorized = false`\n''', encoding='utf-8')

parent_readme.write_text('''# HUMH — Experimentos de Atenção\n\nO diretório `v2.0.0/` contém a árvore corrente do desenho A0/A1 pré-publicação.\n\nStatus científico corrente:\n\n- `ANBC0 = FAIL_DERIVATIONAL`;\n- `A1a = MECHANISM_DEMONSTRATION_ONLY [C1]`;\n- `ASEP0_CONFIRMATORY = NOT_AUTHORIZED`;\n- A1b: `D` é candidato canônico em auditoria estrutural;\n- `ADIST0` estrutural = `CONDITIONAL_DISCRIMINATIVE`, classificação final ainda pendente;\n- regime do primeiro A1: basal e `B_i` homogêneos por isolamento;\n- ciclo científico: barreira síncrona por snapshot lógico;\n- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n\nA teoria exibida pelo site continua sendo `../../teoria.md`. A cópia em `v2.0.0/02_dependencias/` permanece dependência canônica hash-locked.\n''', encoding='utf-8')

# Update dependency lock normative hashes if present.
lock = json.loads(lockp.read_text(encoding='utf-8'))
for item in lock.get('normative_artifacts', []):
    if item['path'].endswith('HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'):
        item['sha256'] = sha(specp)
    if item['path'].endswith('HUMH_A0_A1_Traceabilidade_v2.0.0.json'):
        item['sha256'] = sha(tracep)
lock['publication_state'] = 'REGENERATED_PRE_PUBLICATION_A1B_STRUCTURAL_AUDIT_R2'
lock['scientific_run_authorized'] = False
lock['A1a_confirmatory_authorized'] = False
lock['A1b_confirmatory_authorized'] = False
lock['A1b_structural_audit'] = 'CONDITIONAL_DISCRIMINATIVE'
lockp.write_text(json.dumps(lock, ensure_ascii=False, indent=2), encoding='utf-8')

# Root two-file manifest.
rootsha.write_text(
    f'{sha(specp)}  {specp.name}\n{sha(tracep)}  {tracep.name}\n', encoding='utf-8'
)

# Rebuild SHA256SUMS excluding itself.
files = sorted(p for p in v.rglob('*') if p.is_file() and p != sumsp)
sumsp.write_text('\n'.join(f'{sha(p)}  {p.relative_to(v).as_posix()}' for p in files) + '\n', encoding='utf-8')

print('SPEC_SHA256', sha(specp))
print('TRACE_SHA256', sha(tracep))
print('ROOT_MANIFEST_SHA256', sha(rootsha))
