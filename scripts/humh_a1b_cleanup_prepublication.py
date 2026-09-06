from pathlib import Path
import hashlib
import json

root = Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v = root / 'v2.0.0'
specp = v / '01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep = v / '01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
readmep = v / 'README.md'
parent_readme = root / 'README.md'
sumsp = v / '03_integridade/SHA256SUMS.txt'
rootsha = v / 'HUMH_A0_A1_v2.0.0.sha256'

spec = specp.read_text(encoding='utf-8')
spec = spec.replace('**Status:** `PRE_CODE_TRACEABILITY_FREEZE`', '**Status:** `PRE_CODE_A1B_DERIVATIONAL_AUDIT`')
old_motivo = ('**Motivo:** a microdinâmica basal foi agora congelada a partir da forma discreta canônica da teoria, com mapeamento experimental explícito de uma conclusão válida para uma atualização. A auditoria `ANBC0` classifica essa construção como `FAIL_DERIVATIONAL`: H-A1S torna-se demonstração do mecanismo nesta implementação e não pode receber interpretação confirmatória. Permanecem não congelados os parâmetros numéricos e o conteúdo próprio de A1b antes de qualquer run científico.')
new_motivo = ('**Motivo:** a microdinâmica basal permanece congelada e `ANBC0=FAIL_DERIVATIONAL`, portanto A1a é somente demonstração de mecanismo nesta implementação. A1b entra agora em auditoria derivacional prospectiva: a divergência interobservador canônica `D` é congelada apenas como candidato primário para essa auditoria, e a classificação final depende do regime basal do observador, da regra de atribuição de atenção e dos números ainda não congelados. Nenhum run científico está autorizado.')
if old_motivo not in spec:
    raise SystemExit('top motivo marker not found')
spec = spec.replace(old_motivo, new_motivo)
spec = spec.replace('ATTENTION_INSTRUMENT = FROZEN_LOGICAL_WORK_BUDGET', 'ATTENTION_INSTRUMENT = FROZEN_OPPORTUNITY_ALLOCATION')

old16 = 'A1b não é consequência automática de H-A1S e possui inferência própria em `ADIST0`.'
new16 = ('A1b não é consequência automática de H-A1S. Entretanto, qualquer outcome coletivo candidato deve primeiro passar por auditoria derivacional dentro de `ADIST0`, para excluir efeito que seja invariância ou consequência matemática automática da construção local.')
if old16 not in spec:
    raise SystemExit('section 16 marker not found')
spec = spec.replace(old16, new16)

a = spec.index('# 17. Outcome primário de A1b')
b = spec.index('# 18. Gates — lista fechada')
section17 = r'''# 17. Outcome primário de A1b — candidato canônico e auditoria derivacional

A primeira métrica coletiva candidata é a divergência interobservador já definida no
núcleo canônico 1.9-A:

\[
\boxed{
D=\frac1N\sum_i|p_i-\bar p|
}
\]

Ela é distinta de `D_i` (demanda observacional) e de `D_A` (heterogeneidade de atenção).
A escolha decorre da linhagem pré-existente: o núcleo usa `D` para distinguir estados
com o mesmo `EH` e diferentes estruturas interobservador, enquanto A1b pergunta se
alterar `D_A` a `A_bar` aproximadamente fixo modifica a dinâmica coletiva.

Status prospectivo:

```text
A1B_PRIMARY_OUTCOME_CANDIDATE = STATE_DIVERGENCE_D
CANDIDATE_STATUS = FROZEN_FOR_DERIVATIONAL_AUDIT_NOT_YET_AUTHORIZED
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
```

Congelar o candidato para auditoria não equivale a autorizar sua utilização como
outcome confirmatório.

## 17.1. Subcheck ADIST0.DERIVATIONAL_CONTENT_AUDIT

Considere o caso basal homogêneo permitido pelo desenho:

```text
p_i(0) = p_0 comum
p_target_i = p_target comum
omega_i = omega comum
iota_obs_i = iota_obs comum
kappa comum
D_i(W) = W para todos
```

Defina a transformação basal de uma atualização válida por:

\[
F(p)=p+\eta^{(0)}(p)(p_{target}-p).
\]

Depois de `U_i` conclusões válidas:

\[
p_i(W)=F^{U_i}(p_0),
\qquad
A_i=U_i/W.
\]

Se, adicionalmente, durante a trajetória:

```text
p_0 != p_target
0 < eta0(p) < 1
```

então cada nova atualização move estritamente o estado em direção ao mesmo alvo. Logo:

- no braço perfeitamente uniforme, `A_i` igual implica `U_i` igual e, portanto,
  estados finais iguais (`D=0` quando os estados iniciais também são iguais);
- num braço com `D_A>0`, existem `U_i` distintos; sob as condições acima isso produz
  estados finais distintos e, portanto, `D>0`.

Nesse subdomínio do desenho, um efeito em `D` é:

```text
DERIVATIONALLY_FORCED_EFFECT_IF_CONDITIONS_HOLD
```

e não poderia receber crédito confirmatório de A1b.

## 17.2. Por que a classificação final ainda não é FAIL_DERIVATIONAL

A v2.0.0 ainda não congelou os números basais nem a regra completa de heterogeneidade do
observador. Existem configurações admissíveis nas quais a conclusão acima não é uma
identidade global, por exemplo:

- `eta0=1` pode levar observadores ao alvo em uma única atualização, tornando contagens
  adicionais irrelevantes depois da primeira;
- `p_i(0)=p_target` elimina o drive naquele episódio;
- `omega_i`/`iota_obs_i` heterogêneos tornam `D` dependente também da associação entre
  propriedades basais e a distribuição de `A_i`.

Portanto, antes do congelamento numérico, a classificação correta é:

```text
ADIST0.DERIVATIONAL_CONTENT_AUDIT_PRENUMERIC =
    CONDITIONAL_NOT_GLOBALLY_FORCED

ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL =
    PENDING_BASAL_REGIME_AND_ASSIGNMENT_RULE
```

A classificação final deve ser repetida **depois** de congelados o regime basal do
observador, a inicialização, a regra de atribuição da distribuição de atenção e os
parâmetros que garantem a admissibilidade de `eta0`, mas **antes** da primeira trajetória
científica.

## 17.3. Independência da atribuição em A1b

Se os parâmetros basais variarem entre observadores, a atribuição de níveis de atenção
não pode ser escolhida a partir de `omega_i`, `iota_obs_i`, estado, `EH`, sucesso, fila
ou outcome. A regra deve ser exógena, prospectiva e balanceada/aleatorizada de modo a
não transformar correlação `A_i`–propriedade basal em uma segunda intervenção oculta.

Este requisito é subcheck de `ADIST0`; não cria novo Gate raiz.

## 17.4. Regra anti-resgate

É proibido substituir `D` por outro outcome primário apenas porque a auditoria final o
classifique como `DERIVATIONALLY_FORCED_EFFECT` ou `DERIVATIONALLY_INVARIANT`.

Se a classificação final mostrar que `D` não possui conteúdo discriminativo nesta
construção:

```text
A1b = MECHANISM_DEMONSTRATION_ONLY [C1]
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
```

Uma hipótese sucessora poderá usar outro desenho, com nova justificativa prospectiva,
mas não reclassificará esta auditoria.

A restrição temporal permanece:

```text
A1B_DERIVATIONAL_AUDIT_FINAL_MUST_PRECEDE_FIRST_SCIENTIFIC_TRAJECTORY
```

---

'''
spec = spec[:a] + section17 + spec[b:]

marker = '''AISO0
  .SERVICE_INVARIANCE
  .PROPAGATION_INVARIANCE
  .TOPOLOGY_INVARIANCE
  .EXOGENOUS_DEMAND_INVARIANCE

AINT0'''
replacement = '''AISO0
  .SERVICE_INVARIANCE
  .PROPAGATION_INVARIANCE
  .TOPOLOGY_INVARIANCE
  .EXOGENOUS_DEMAND_INVARIANCE

ADIST0
  .DERIVATIONAL_CONTENT_AUDIT
  .ATTENTION_TO_OBSERVER_ASSIGNMENT_INDEPENDENCE

AINT0'''
if marker not in spec:
    raise SystemExit('subcheck marker not found')
spec = spec.replace(marker, replacement, 1)

a = spec.index('# 26. Itens numéricos ainda NÃO congelados')
b = spec.index('# 28. Regra automática de rastreabilidade para o código')
section26_27 = r'''# 26. Itens de desenho e números ainda NÃO congelados

A v2.0.0 conscientemente deixa como `UNFROZEN_REQUIRED_BEFORE_RUN`:

```text
N
W
basal_eta0_bound_admissibility
observer_basal_parameter_regime
omega_i_rule
omega_i_values_or_distribution
iota_obs_i_rule
iota_obs_i_values_or_distribution
kappa_value_or_rule
observer_buffer_capacity_heterogeneity_regime
observer_buffer_capacity_rule
observer_buffer_capacity_values_or_distribution
required_work_rule
required_work_range_or_distribution
L_grid
regras instrumentais candidatas de ABENCH0
critérios instrumentais de ABENCH0
L_A
number_of_arms
instrumental_contrast_criteria
saturation_avoidance_criteria
attention_to_observer_assignment_rule_A1b
ADIST0_final_derivational_classification
margem de matching de A_bar
diferença mínima de D_A
margem de efeito A1b
regra inferencial A1b
tamanho amostral/poder
```

Nenhum desses campos pode ser preenchido com base em outcomes científicos da série
v1.0.x nem escolhido para obter uma classificação desejada em `ADIST0`.

A microdinâmica basal **não é mais um bloqueio aberto**:

```text
A1A_OBSERVER_MICRODYNAMIC =
  FROZEN_CANONICAL_DISCRETE_WITH_AUXILIARY_COMPLETION_MAPPING
ANBC0 = FAIL_DERIVATIONAL
```

O contrato de `p_alvo` permanece semanticamente congelado, mas ainda exige:

```text
p_A
p_B
number_of_target_episodes
A_B_episode_balance_and_order
target_episode_length
initial_p_rule
target_stationarity_certification
```

---

# 27. Procedimento autorizado daqui até run-ready

A ordem prospectiva passa a ser:

1. preservar a microdinâmica basal já congelada e aceitar `ANBC0=FAIL_DERIVATIONAL`;
2. manter `D` como candidato primário congelado para a auditoria de A1b, sem trocar de
   outcome para obter uma classificação desejada;
3. congelar o regime basal do observador (`omega_i`, `iota_obs_i`, `kappa`), a regra de
   inicialização e a regra exógena de atribuição de atenção por critério independente de
   outcomes A1;
4. certificar prospectivamente `0 < eta0 <= 1` no domínio admissível, sem clamp pós-hoc;
5. repetir `ADIST0.DERIVATIONAL_CONTENT_AUDIT` com esses números/regras congelados;
6. se `D` for derivacionalmente forçado ou invariante, registrar A1b como demonstração
   de mecanismo nesta construção e **não** selecionar outro outcome como resgate;
7. somente se `D` permanecer discriminativo, congelar as margens de `A_bar`, `D_A`,
   materialidade, inferência e poder de A1b;
8. executar os benchmarks técnicos/integridade aplicáveis (`AETA0`, `ABENCH0`, `AMAN0`,
   `AISO0`, `AINT0`) sem usar outcomes científicos para tuning;
9. manter esta mesma identidade `v2.0.0` enquanto o objeto continuar pré-publicação;
   qualquer regeneração deve atualizar hashes e manifesto de integridade.

Não existe mais nesta versão a etapa "resolver observer_microdynamic_contract" nem a
instrução automática de gerar `2.0.1_RUN_READY`.

---

'''
spec = spec[:a] + section26_27 + spec[b:]

old_a1a = '''## A1a

Com todos os pré-requisitos adequados:

```text
ATTENTION_MULTIPLICATIVE_SEPARABILITY_COMPATIBLE [C1]
ATTENTION_MULTIPLICATIVE_SEPARABILITY_REFUTED [C1]
INCONCLUSIVE_*
```
'''
new_a1a = '''## A1a

Na construção corrente da v2.0.0:

```text
ANBC0 = FAIL_DERIVATIONAL
A1a = MECHANISM_DEMONSTRATION_ONLY [C1]
ASEP0_CONFIRMATORY = NOT_AUTHORIZED
```

As categorias `...COMPATIBLE [C1]` e `...REFUTED [C1]` pertencem ao contrato geral de
H-A1S, mas não podem ser emitidas por esta implementação.
'''
if old_a1a not in spec:
    raise SystemExit('A1a result logic marker not found')
spec = spec.replace(old_a1a, new_a1a, 1)

old_a1b = '''## A1b

Somente depois de ADIST0 ser totalmente congelado:

```text
ATTENTION_DISTRIBUTION_EFFECT_ESTABLISHED/COMPATIBLE [C1]
ATTENTION_DISTRIBUTION_EFFECT_NOT_ESTABLISHED
ATTENTION_DISTRIBUTION_EFFECT_REFUTED
INCONCLUSIVE_*
```
'''
new_a1b = '''## A1b

Estado corrente:

```text
PRIMARY_OUTCOME_CANDIDATE = STATE_DIVERGENCE_D
ADIST0.DERIVATIONAL_CONTENT_AUDIT_PRENUMERIC = CONDITIONAL_NOT_GLOBALLY_FORCED
ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = PENDING_BASAL_REGIME_AND_ASSIGNMENT_RULE
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
```

Somente se a auditoria final classificar o candidato como discriminativo e os demais
critérios forem congelados poderão ser usadas as categorias gerais de resultado de A1b.
'''
if old_a1b not in spec:
    raise SystemExit('A1b result logic marker not found')
spec = spec.replace(old_a1b, new_a1b, 1)

spec = spec.replace('NEXT = AUDIT_A1B_INDEPENDENT_CONTENT_THEN_FREEZE_REMAINING_NUMERICAL_DESIGN',
                    'NEXT = FREEZE_BASAL_OBSERVER_REGIME_AND_COMPLETE_ADIST0_DERIVATIONAL_AUDIT')
specp.write_text(spec, encoding='utf-8', newline='\n')

tr = json.loads(tracep.read_text(encoding='utf-8'))
tr['status'] = 'V2_0_0_A1B_DERIVATIONAL_AUDIT_PREPUBLICATION'
tr['scientific_run_authorized'] = False
tr['a1b_derivational_audit'] = {
    'id': 'ADIST0_DERIVATIONAL_CONTENT_AUDIT',
    'kind': 'GATE_SUBCHECK',
    'parent_gate': 'ADIST0',
    'scientific_role': 'DERIVATIONAL_DIAGNOSTIC',
    'primary_outcome_candidate': {
        'id': 'STATE_DIVERGENCE_D',
        'canonical_symbol': 'D',
        'formula': '(1/N) * sum_i |p_i - p_bar|',
        'status': 'FROZEN_FOR_DERIVATIONAL_AUDIT_NOT_YET_AUTHORIZED'
    },
    'pre_numeric_classification': 'CONDITIONAL_NOT_GLOBALLY_FORCED',
    'final_classification': 'PENDING_BASAL_REGIME_AND_ASSIGNMENT_RULE',
    'homogeneous_sufficient_pattern': {
        'conditions': [
            'common initial p_0',
            'common p_target',
            'common omega/iota_obs/kappa',
            'D_i(W)=W',
            'p_0 != p_target',
            '0 < eta0(p) < 1 along the relevant path',
            'D_A > 0 implies distinct U_i'
        ],
        'consequence': 'uniform A_i -> equal final p_i; heterogeneous A_i -> distinct final p_i; therefore D changes by construction',
        'classification': 'DERIVATIONALLY_FORCED_EFFECT_IF_CONDITIONS_HOLD'
    },
    'non_global_counterconditions': [
        'eta0=1 may collapse different positive update counts to the same target state',
        'p_i(0)=p_target removes drive',
        'heterogeneous omega_i/iota_obs_i makes D depend also on the assignment of attention to observer properties'
    ],
    'assignment_independence_required_if_basal_heterogeneous': True,
    'anti_rescue_rule': 'Do not replace D with another primary outcome merely to obtain a discriminative classification. If final audit is forced or invariant, A1b in this construction is mechanism demonstration only.',
    'canonical_refs': [
        {
            'artifact_id': 'HUMH_1.9A',
            'sha256': 'baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b',
            'section': 'A4',
            'clause_or_statement': 'D=(1/N) sum_i |p_i-p_bar| is interobserver divergence and is distinct from EH.'
        },
        {
            'artifact_id': 'HUMH_ATTENTION_DEFINITION_1.0.0',
            'sha256': '3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a',
            'section': 67,
            'clause_or_statement': 'A1b asks whether changing D_A at fixed A_bar changes collective dynamics.'
        },
        {
            'artifact_id': 'HUMH_ATTENTION_DEFINITION_1.0.0',
            'sha256': '3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a',
            'section': 69,
            'clause_or_statement': 'A1b is an additional collective question and requires its own specification and gates.'
        },
        {
            'artifact_id': 'HUMH_ATTENTION_DEFINITION_1.0.0',
            'sha256': '3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a',
            'section': 103,
            'clause_or_statement': 'First A1b forbids reactive reallocation; the allocation rule must be exogenous and frozen.'
        }
    ]
}

subs = tr.setdefault('subchecks_only', {})
ad = subs.setdefault('ADIST0', [])
for name in ['DERIVATIONAL_CONTENT_AUDIT', 'ATTENTION_TO_OBSERVER_ASSIGNMENT_INDEPENDENCE']:
    if name not in ad:
        ad.append(name)

pending = tr.setdefault('unfrozen_required_before_run', [])
for x in [
    'basal_eta0_bound_admissibility',
    'observer_basal_parameter_regime',
    'omega_i_rule',
    'omega_i_values_or_distribution',
    'iota_obs_i_rule',
    'iota_obs_i_values_or_distribution',
    'kappa_value_or_rule',
    'attention_to_observer_assignment_rule_A1b',
    'ADIST0_final_derivational_classification'
]:
    if x not in pending:
        pending.append(x)

tr['next_version'] = ('Keep v2.0.0 while unpublished. Microdynamic and ANBC0 are already frozen. '
                      'D is frozen only as the A1b primary-outcome candidate for derivational audit. '
                      'Next freeze the basal observer regime and exogenous attention-to-observer assignment rule, '
                      'then complete the final ADIST0 derivational audit before any scientific trajectory. '
                      'Do not switch outcomes to rescue discriminativity.')

rl = tr.setdefault('result_logic', {})
if isinstance(rl.get('A1a'), dict):
    rl['A1a']['current_disposition'] = 'MECHANISM_DEMONSTRATION_ONLY [C1]'
    rl['A1a']['confirmatory_authorized'] = False
if isinstance(rl.get('A1b'), dict):
    rl['A1b']['current_authorization'] = 'NOT_AUTHORIZED_PENDING_FINAL_DERIVATIONAL_AUDIT'
    rl['A1b']['primary_outcome_candidate'] = 'STATE_DIVERGENCE_D'
    rl['A1b']['pre_numeric_derivational_classification'] = 'CONDITIONAL_NOT_GLOBALLY_FORCED'

tracep.write_text(json.dumps(tr, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

readme = readmep.read_text(encoding='utf-8')
old = '''## Próximo bloqueio

Auditar se A1b possui conteúdo coletivo próprio não redutível à identidade local de A1a.
Depois, congelar os parâmetros numéricos restantes.

`scientific_run_authorized = false`
'''
new = '''## Auditoria A1b em curso

A divergência interobservador canônica

`D = (1/N) * sum_i |p_i - p_bar|`

fica congelada **somente como candidato primário para auditoria derivacional**.
A análise pré-numérica encontrou um padrão suficiente em que o efeito é forçado
(homogeneidade basal, mesmo estado inicial/alvo e `0 < eta0 < 1`), mas esse padrão não é
uma identidade global de todo o espaço ainda admissível.

Status:

`ADIST0.DERIVATIONAL_CONTENT_AUDIT_PRENUMERIC = CONDITIONAL_NOT_GLOBALLY_FORCED`

`ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = PENDING_BASAL_REGIME_AND_ASSIGNMENT_RULE`

Próximo bloqueio: congelar prospectivamente o regime basal do observador e a regra
exógena de atribuição de atenção; depois repetir a auditoria final. É proibido trocar
`D` por outro outcome apenas para obter uma classificação discriminativa.

`scientific_run_authorized = false`
'''
if old not in readme:
    raise SystemExit('version README marker not found')
readme = readme.replace(old, new)
readmep.write_text(readme, encoding='utf-8', newline='\n')

pr = parent_readme.read_text(encoding='utf-8')
pr = pr.replace('- próximo bloqueio: auditoria do conteúdo coletivo independente de A1b;',
                '- A1b: `D` (divergência interobservador) congelado como candidato para auditoria derivacional;')
pr = pr.replace('- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.',
                '- auditoria pré-numérica de A1b: `CONDITIONAL_NOT_GLOBALLY_FORCED`; final pendente do regime basal e regra de atribuição;\n- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.')
parent_readme.write_text(pr, encoding='utf-8', newline='\n')

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

rootsha.write_text(
    f"{sha(specp)}  {specp.name}\n{sha(tracep)}  {tracep.name}\n",
    encoding='utf-8', newline='\n')

lines = []
for line in sumsp.read_text(encoding='utf-8').splitlines():
    if not line.strip():
        continue
    _, rel = line.split('  ', 1)
    p = v / rel
    if not p.exists():
        raise SystemExit(f'missing materialized file: {rel}')
    lines.append(f'{sha(p)}  {rel}')
sumsp.write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')

final_spec = specp.read_text(encoding='utf-8')
for stale in [
    'observer_microdynamic_contract',
    'HUMH_A0_A1_SPEC_2.0.1_RUN_READY',
    'ATTENTION_INSTRUMENT = FROZEN_LOGICAL_WORK_BUDGET'
]:
    if stale in final_spec:
        raise SystemExit(f'stale marker remains: {stale}')

print('SPEC_SHA256', sha(specp))
print('TRACE_SHA256', sha(tracep))
print('ROOT_SHA_MANIFEST_SHA256', sha(rootsha))
