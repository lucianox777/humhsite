from pathlib import Path
import hashlib, json

root = Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v = root / 'v2.0.0'
specp = v / '01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep = v / '01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
lockp = v / '02_dependencias/DEPENDENCIES.lock.json'
sumsp = v / '03_integridade/SHA256SUMS.txt'
rootshap = v / 'HUMH_A0_A1_v2.0.0.sha256'
ATT = '3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a'
THEORY = '3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p, s): p.write_text(s, encoding='utf-8', newline='\n')
def dump(p, obj): write(p, json.dumps(obj, indent=2, ensure_ascii=False)+'\n')
def replace_once(s, old, new):
    assert s.count(old) == 1, ('Expected one anchor', old[:100], s.count(old))
    return s.replace(old, new, 1)
def ref(section, statement):
    return {'artifact_id':'HUMH_ATTENTION_DEFINITION_1.0.0','sha256':ATT,
            'section':section,'clause_or_statement':statement}

assert sha(specp) == 'f7449dc82d60cee773b0731a552a8de97f2145a291e64000723e995db5410807'
assert sha(tracep) == '008ec6a21149114ffc3cd5a4b08abf908eeec49f33deb558a641f5e554889ae9'
assert sha(v/'03_integridade/audit_schedules.py')
for name, expected in [('HUMH_Definicao_Atencao_Observacional_Efetiva_v1.0.0.md',ATT),('teoria.md',THEORY)]:
    assert sha(v/'02_dependencias'/name) == expected

spec = specp.read_text(encoding='utf-8')
spec = replace_once(spec, '**Status:** `PRE_CODE_MINIMAL_WORKLOAD_AND_DEADLINE_FREEZE`',
                    '**Status:** `PRE_CODE_SCHEDULE_FEASIBILITY_AND_DERIVATIONAL_AUDIT`')
a = spec.index('**Motivo:** ')
b = spec.index('\n', a)
spec = spec[:a] + ('**Motivo:** O R7 permanece congelado. A auditoria R8 demonstra que a razão nominal oportunidades/trabalho não determina A_i, identifica bloqueio de fase do FIFO e apresenta um testemunho de matching A1b com massa nominal, trabalho efetivo e número de atualizações iguais por ciclo. O próprio testemunho força divergência D pela regra basal e, portanto, é demonstração de mecanismo, não confirmação independente. Os níveis científicos de A1b continuam pendentes; nenhum parâmetro é escolhido para resgatar a classificação.') + spec[b:]

window = r'''## 4.1.2. Coorte de demanda e borda direita — ESCLARECIMENTO

A janela primária W contém os ciclos de geração `0,...,W-1`. A regra `D_i(W)=W`
conta as demandas geradas nesses ciclos, e não as conclusões ocorridas dentro do
intervalo de geração. Para a mesma coorte:

\[
U_i(W)=\sum_{j:\,arrival_j\in[0,W-1]}
\mathbf 1\{completion_j\le arrival_j+L_A\}.
\]

A demanda criada em `W-1` ainda pode concluir no ciclo `W` quando `L_A=1`.
O processamento da coorte continua até o último deadline inclusivo; não se criam
novas demandas elegíveis para o denominador durante essa cauda. Ao abrir o ciclo
seguinte ao último deadline, as pendências vencidas são expiradas sem atualização.
Apenas então a contabilidade é encerrada. A cauda não muda W, D_i ou A_i.

```
COHORT = ARRIVALS_IN_W
LAST_VALID_COMPLETION_CYCLE = W-1+L_A
EXPIRE_ONLY_IF = current_cycle > deadline_cycle
NO_NEW_ELIGIBLE_DEMANDS_IN_COHORT_DRAIN = TRUE
NO_LATE_BASAL_UPDATE = TRUE
```

A mesma regra vale para todos os braços e para o benchmark cego. O fechamento
não pode transformar demanda pendente em sucesso, descartar demanda do denominador
ou permitir que um braço receba prorrogação diferente. Este esclarecimento
operacionaliza os §§8–16 e 21 da definição canônica e os subchecks já existentes
`AMEAS0.RIGHT_EDGE_ACCOUNTING` e `AINT0.NO_RIGHT_CENSORING`.

---

'''
spec = replace_once(spec, '## 4.2 Atenção coletiva', window+'## 4.2 Atenção coletiva')

a = spec.index('## 5.1.13. Parâmetros numéricos pendentes')
b = spec.index('## 5.1.14.', a)
part = spec[a:b]
part = part.replace('observer_buffer_capacity_value\n', '').replace('L_A\n', '')
part = part.replace('A semântica e o regime de isolamento já estão congelados.',
                    'A semântica, B=1, K_C=2 e L_A=1 já estão congelados.')
spec = spec[:a]+part+spec[b:]

spec = replace_once(spec,
    'Se `L_A=1` não for tecnicamente adequado, um novo benchmark cego selecionará `L_A`.',
    'O R7 congela `L_A=1` porque a arquitetura lógica suporta a cadeia completa dentro do intervalo canônico. ABENCH0 valida cegamente esse contrato e os níveis instrumentais ainda pendentes; não seleciona outro deadline nem altera K_C. Se a implementação não conseguir cumpri-lo, o Gate falha e o run permanece não autorizado. Uma alteração do contrato exige revisão prospectiva antes de qualquer trajetória científica.')
spec = replace_once(spec,
    'Se nenhum `L_A` satisfizer a regra congelada:\n\n```text\nABENCH0 = FAIL\nSCIENTIFIC_RUN_NOT_AUTHORIZED\n```',
    'Se o contrato congelado não for tecnicamente atendido:\n\n```text\nABENCH0 = FAIL\nSCIENTIFIC_RUN_NOT_AUTHORIZED\nNO_POST_HOC_DEADLINE_RESCUE = TRUE\n```')

witness = r'''## 17.3.1. Auditoria R8 de viabilidade e conteúdo derivacional — PRÉ-CÓDIGO

Esta auditoria não congela os níveis científicos de A1b. Ela verifica, antes de
qualquer trajetória científica, o que o mecanismo de fila permite e o que ele
já determina matematicamente. Os testes executáveis ficam em
`03_integridade/audit_schedules.py`, sem acesso a p, EH, eta ou outcomes.

### A razão nominal não é atenção

Com `B=1`, `K_C=2`, `L_A=1`, demanda unitária por ciclo e FIFO, um schedule
constante de uma oportunidade/ciclo não produz A=1/2. A demanda 0 usa os
ciclos 0 e 1 e conclui; a demanda 1 começa no seu deadline, ciclo 2, recebe
somente uma oportunidade e expira no ciclo 3. O mesmo bloqueio de fase se
repete. Para W>=2, a coorte produz U_i=1, e não aproximadamente W/2.
Logo, nenhuma regra científica pode converter diretamente Pobs/K_C em A_i.

### Testemunho auxiliar de matching

Considere N e W pares, fila inicialmente vazia, estratos fixos de mesmo tamanho,
e a seguinte regra exógena, em que n é o ciclo lógico:

| Condição | n par | n ímpar |
|---|---:|---:|
| UNIFORM, todos os observadores | 0 | 2 |
| HETEROGENEOUS, estrato HIGH | 0 | 4 |
| HETEROGENEOUS, estrato LOW | 0 | 0 |

Este é um testemunho analítico, não uma escolha de braços confirmatórios. A
atribuição HIGH/LOW é fixa e independente dos estados. Para cada par de ciclos,
o uniforme conclui a demanda do primeiro ciclo e deixa vencer a segunda;
o HIGH conclui ambas e o LOW nenhuma. A contabilidade por coorte, inclusive
a última demanda e seu deadline, dá exatamente:

\[
A_i^{uniform}=1/2,\qquad
A_i^{heterogeneous}\in\{1,0\},
\]

\[
\bar A_{uniform}=\bar A_{heterogeneous}=1/2,
\quad D_{A,uniform}=0,\quad D_{A,heterogeneous}=1/2.
\]

Em cada ciclo par os dois braços recebem zero oportunidades. Em cada ciclo
ímpar, o uniforme recebe `2N` e o heterogêneo recebe `4(N/2)=2N`.
Nesses ciclos, ambos também executam exatamente `2N` unidades de trabalho
e completam exatamente N atualizações. Portanto o testemunho iguala inclusive
trabalho efetivo e número global de updates por ciclo, não apenas orçamento
nominal. A igualdade decorre da fila, não de correção reativa do schedule.

W par é condição matemática deste testemunho: com W ímpar, a coorte de último
ciclo pode concluir na cauda e o matching exato acima não vale. Não se escolhe
W científico, nível de atenção, proporção ou margem com base neste resultado.

### O mesmo testemunho não confirma A1b

No regime basal homogêneo, com p_i(0)=p_0, alvo comum fixo e
`0<eta_n<=1`, a condição uniforme conserva todos os observadores no mesmo
estado. Portanto `D_uniform(W)=0` é uma identidade da construção.

No heterogêneo, o estrato LOW não atualiza e permanece em p_0. No HIGH,
cada ciclo ímpar aplica duas vezes a regra basal com o mesmo EH[n] do snapshot.
Definindo `r_n=1-eta_n`, segue exatamente:

\[
p_H(W)=p_{target}+(p_0-p_{target})\prod_{n\,impar}r_n^2,
\qquad p_L(W)=p_0.
\]

Para dois estratos de mesmo tamanho:

\[
\boxed{
D_{heterogeneous}(W)=\frac{|p_{target}-p_0|}{2}
\left(1-\prod_{n\,impar}(1-\eta_n)^2\right).
}
\]

Com p_0 distinto do alvo e taxa basal admissível positiva, esse D é
estritamente positivo. A conclusão não depende de escolher lambda_state>0:
vale também para lambda_state=0 e para qualquer sequência admissível de EH.

Assim, a diferença de D deste testemunho é **derivacional**. A auditoria de
instrumentação passa, mas ADIST0 não pode promover esse efeito a confirmação
independente. Não se trata de refutação da HUMH ou de H-A1S.

```
A1B_R8_WITNESS = AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION
A1B_R8_INSTRUMENT_FEASIBILITY = PASS_ANALYTIC
A1B_R8_WITNESS_DERIVATIONAL_CONTENT = FAIL_DERIVATIONAL
A1B_R8_WITNESS_SCIENTIFIC_ROLE = MECHANISM_DEMONSTRATION_ONLY
A1B_SCIENTIFIC_ASSIGNMENT_LEVELS = UNFROZEN_REQUIRED_BEFORE_RUN
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
SCIENTIFIC_RUN_NOT_AUTHORIZED
```

O testemunho não fixa os números do primeiro A1b e não autoriza busca de outra
parametrização para obter um rótulo favorável. A ausência de uma identidade geral
D_A->D não é condição suficiente de discriminação: cada desenho concreto deve
passar por sua própria auditoria de consequência algébrica e competência.

---

'''
spec = replace_once(spec, '## 17.4. Classificação prospectiva atual de ADIST0',
                    witness+'## 17.4. Classificação prospectiva atual de ADIST0')
spec = replace_once(spec,
    '`CONDITIONAL_DISCRIMINATIVE` significa que a construção **não contém uma identidade geral**\n`D_A -> D`, mas possui subdomínios admissíveis em que um efeito em `D` é derivacional.',
    '`CONDITIONAL_DISCRIMINATIVE` é apenas a classificação geral preliminar de ausência de uma identidade universal `D_A -> D`. Não é demonstração de competência discriminativa nem autorização confirmatória. O R8 mostra um subdomínio concreto no qual o contraste em D é derivacional mesmo com EH dependente do estado. A auditoria final de qualquer desenho científico deverá excluir conclusões já garantidas por sua própria construção, sem selecionar parâmetros para forçar aprovação.')
spec = replace_once(spec,
    'A classificação final deve ser repetida depois de congelados `omega`, `iota_obs`, `kappa`,\n`B`, `p_0`, `L_A`, `W` e a regra exata de distribuição temporal de oportunidades, sempre\nantes da primeira trajetória científica.',
    'A classificação final deve ser repetida depois de congelados os compostos basais identificáveis, p_0, W e os níveis instrumentais ainda pendentes, sempre antes da primeira trajetória científica. B=1, K_C=2 e L_A=1 não são reabertos. A classificação do testemunho R8 já é derivacional e não pode ser revertida por tuning.')
write(specp,spec)

trace = json.loads(tracep.read_text(encoding='utf-8'))
trace['status'] = 'V2_0_0_SCHEDULE_FEASIBILITY_AND_DERIVATIONAL_AUDIT_PREPUBLICATION'
trace['scientific_run_authorized'] = False
trace['measurement_window_contract'] = {
    'status':'FROZEN_ARRIVAL_COHORT_INCLUSIVE_DEADLINE',
    'scientific_role':'AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION',
    'demand_generation_cycles':'0 <= n < W',
    'D_i':'W',
    'U_i':'count eligible cohort demands completed at or before arrival_cycle+L_A',
    'last_valid_completion_cycle':'W-1+L_A',
    'expiry_rule':'current_cycle > deadline_cycle',
    'drain_creates_new_cohort_demands':False,
    'no_late_basal_update':True,
    'canonical_refs':[ref(8,'D_i counts exogenous eligible demand in W.'),ref(9,'Attention arms preserve demand identity and content.'),ref(12,'U_i counts completion of the full chain within the valid deadline.'),ref(14,'Completion at the common deadline is valid.'),ref(21,'Attention is measured from completed eligible requests, not nominal priority.'),ref(94,'Integrity includes reproducible measurement and deadline accounting.')]
}
witness_ref = [ref(29,'A_bar is mean individual attention.'),ref(30,'D_A is mean absolute attention deviation.'),ref(31,'A1b compares attention distributions at matched mean.'),ref(67,'A1b studies the distribution of attention.'),ref(68,'ADIST0 requires an authorized frozen distribution comparison.'),ref(69,'A1b inference must not treat an instrumentation artifact as scientific support.'),ref(102,'The first A1b must establish its own scientific content.'),ref(103,'A1b requires prospective decision conditions.'),ref(116,'A1b result categories depend on valid measurement and discriminative inference.')]
trace['a1b_schedule_audit_R8'] = {
    'id':'ADIST0.DERIVATIONAL_CONTENT_AUDIT.R8_WITNESS',
    'kind':'GATE_SUBCHECK',
    'parent_gate':'ADIST0',
    'scientific_role':'AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION',
    'status':'PASS_INSTRUMENT_FEASIBILITY_FAIL_DERIVATIONAL_CONTENT_FOR_WITNESS',
    'scientific_run_authorized':False,
    'scientific_assignment_levels_frozen':False,
    'canonical_refs':witness_ref,
    'queue_phase_trap':{'schedule':'one opportunity per cycle','K_C':2,'L_A':1,'result':'U_i=1 for W>=2, not W/2','meaning':'nominal opportunity ratio is not measured attention'},
    'witness':{'scope':'AUXILIARY_ONLY','required_conditions':['N even','W even','empty initial queues','homogeneous B=1 and K_C=2','L_A=1','fixed equal-size strata'],
       'uniform_schedule':'Pobs_i(n)=0 for even n, 2 for odd n',
       'heterogeneous_high_schedule':'Pobs_i(n)=0 for even n, 4 for odd n',
       'heterogeneous_low_schedule':'Pobs_i(n)=0',
       'U_uniform':'W/2 for every observer','U_high':'W','U_low':'0',
       'Abar_uniform':0.5,'Abar_heterogeneous':0.5,'D_A_uniform':0,'D_A_heterogeneous':0.5,
       'per_cycle_nominal_mass_matched':True,'per_cycle_executed_work_matched':True,'per_cycle_update_count_matched':True,
       'right_edge':'cohort drain through W-1+L_A; no new denominator demands',
       'derivational_disposition':'FAIL_DERIVATIONAL',
       'D_uniform':'0',
       'D_heterogeneous':'abs(p_target-p0)*(1-product_odd_cycles((1-eta_n)^2))/2',
       'strictly_positive_if':'p0 != p_target and eta_n in (0,1] with at least one update cycle',
       'independent_confirmation':False},
    'anti_rescue':'No scientific parameter or schedule may be selected to turn the witness derivational classification into confirmatory support.'
}
audit = trace['a1b_derivational_audit']
audit['R8_witness_disposition'] = 'FAIL_DERIVATIONAL'
audit['R8_witness_instrument_feasibility'] = 'PASS_ANALYTIC'
audit['R8_witness_is_confirmatory'] = False
audit['general_nonidentity_is_sufficient_for_confirmation'] = False
audit['current_confirmatory_authorization'] = False
audit['status_final'] = 'PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_LEVELS'
if 'A1b' in trace.get('result_logic',{}):
    trace['result_logic']['A1b']['R8_witness_disposition'] = 'MECHANISM_DEMONSTRATION_ONLY'
    trace['result_logic']['A1b']['R8_witness_not_independent_confirmation'] = True
for path in [('unfrozen_required_before_run',),('attention_instrument','numerics_pending'),('parameter_provenance_policy','classes','BLIND_INSTRUMENT_CALIBRATION_ABENCH0')]:
    obj = trace
    for key in path[:-1]: obj = obj.get(key,{})
    key = path[-1]
    if isinstance(obj,dict) and isinstance(obj.get(key),list):
        obj[key] = [x for x in obj[key] if x not in {'observer_buffer_capacity_value','observer_buffer_capacity_rule','observer_buffer_capacity_values_or_distribution','observer_buffer_capacity_heterogeneity_regime','required_work_rule','required_work_range_or_distribution','required_opportunities_per_request_K_C','L_grid','L_A'}]
trace['next_version'] = 'Keep unpublished v2.0.0. R8 validates schedule feasibility and identifies a derivational A1b witness; scientific levels remain unfrozen. Do not tune to rescue independent confirmation. Finish prospectively justified design and integrity/power checks before any scientific run.'
assert len(trace['root_gates']) == 11
assert trace['definition']['sha256'] == ATT and trace['definition']['theory_sha256'] == THEORY
assert trace['a1b_schedule_audit_R8']['canonical_refs']
dump(tracep,trace)

lock = json.loads(lockp.read_text(encoding='utf-8'))
lock['publication_state'] = 'REGENERATED_PRE_PUBLICATION_SCHEDULE_AUDIT_R8'
lock['scientific_run_authorized'] = False
lock['A1b_confirmatory_authorized'] = False
lock['A1b_structural_audit_scope'] = 'GENERAL_NONIDENTITY_ONLY_NOT_CONFIRMATORY_AUTHORIZATION'
lock['A1b_R8_witness_disposition'] = 'FAIL_DERIVATIONAL_MECHANISM_DEMONSTRATION_ONLY'
lock['A1b_R8_instrument_feasibility'] = 'PASS_ANALYTIC'
lock['A1b_scientific_assignment_levels_frozen'] = False
for entry in lock['normative_artifacts']:
    entry['sha256'] = sha(v/entry['path'])
for dep in lock['active_canonical_dependencies']:
    assert sha(v/dep['path']) == dep['sha256']
dump(lockp,lock)

readmep = v/'README.md'
readme = readmep.read_text(encoding='utf-8')
readme = readme.replace('A1b mantém `D` como candidato `CONDITIONAL_DISCRIMINATIVE`.',
    'A1b mantém `D` como candidato sob auditoria estrutural; a ausência de identidade geral não autoriza confirmação independente. O testemunho R8 é derivacional e somente demonstra mecanismo.')
readme += '\nO auditor auxiliar `03_integridade/audit_schedules.py` verifica FIFO, deadlines, borda direita e um testemunho de matching sem executar trajetórias científicas. Seus números não congelam os braços A1b.\n'
write(readmep,readme)
parentp = root/'README.md'
parent = parentp.read_text(encoding='utf-8')
parent = parent.replace('A1b: `D` candidato `CONDITIONAL_DISCRIMINATIVE`;',
    'A1b: `D` candidato sob auditoria; testemunho R8 derivacional, sem autorização confirmatória;')
parent += '\nA auditoria pré-código R8 está integrada à spec/trace v2.0.0 e ao verificador auxiliar de schedules. Não congela níveis científicos nem reabre os contratos R7.\n'
write(parentp,parent)

treep = v/'TREE.txt'
tree = treep.read_text(encoding='utf-8')
tree = replace_once(tree, '    └── verify.py', '    ├── audit_schedules.py\n    └── verify.py')
write(treep,tree)
rootshap.write_text(sha(specp)+'  '+specp.name+'\n'+sha(tracep)+'  '+tracep.name+'\n',encoding='utf-8')
files = sorted(p for p in v.rglob('*') if p.is_file() and p != sumsp and '__pycache__' not in p.parts)
write(sumsp,''.join(sha(p)+'  '+p.relative_to(v).as_posix()+'\n' for p in files))
for entry in lock['normative_artifacts']:
    assert sha(v/entry['path']) == entry['sha256']
for line in sumsp.read_text(encoding='utf-8').splitlines():
    expected, rel = line.split('  ',1)
    assert sha(v/rel) == expected
assert set(p.relative_to(v).as_posix() for p in files) == set(line.split('  ',1)[1] for line in sumsp.read_text(encoding='utf-8').splitlines())
assert all(sha(v/dep['path']) == dep['sha256'] for dep in lock['active_canonical_dependencies'])
print('SPEC_SHA256',sha(specp))
print('TRACE_SHA256',sha(tracep))
print('R8 normative/integrity patch PASS; no scientific trajectory executed.')
