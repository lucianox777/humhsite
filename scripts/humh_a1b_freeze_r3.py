from pathlib import Path
import hashlib, json

root=Path('source/HUMH.Api/wwwroot/content/experimentos/atencao')
v=root/'v2.0.0'
specp=v/'01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
tracep=v/'01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
lockp=v/'02_dependencias/DEPENDENCIES.lock.json'
readmep=v/'README.md'
parent=root/'README.md'
rootsha=v/'HUMH_A0_A1_v2.0.0.sha256'
sumsp=v/'03_integridade/SHA256SUMS.txt'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

spec=specp.read_text(encoding='utf-8')

# Insert analytic admissibility freeze after domain preservation status.
marker='''```text\nBASAL_ETA0_BOUND_PRESERVATION = REQUIRED_BEFORE_RUN\nPOST_HOC_CLAMPING = FORBIDDEN\n```\n'''
insert=r'''

### 7.1.2.1. Critério analítico de admissibilidade de `eta0` — CONGELADO

Como `EH` pertence ao intervalo `[0,1]`, defina:

\[
m=\min_{h\in[0,1]}\left(1+\iota_{obs}+\kappa h\right)
 =1+\iota_{obs}+\min(0,\kappa).
\]

Para o regime homogêneo do primeiro A1, a condição prospectiva que garante simultaneamente
denominador positivo e:

\[
0<\eta^{(0)}(h)\le1
\]

para todo `h in [0,1]` é:

\[
\boxed{m>0\quad\land\quad 0<\omega\le m.}
\]

Se `kappa>=0`, a expressão reduz-se a:

\[
0<\omega\le1+\iota_{obs}.
\]

A desigualdade é um **critério de admissibilidade**, não uma escolha numérica. `omega`,
`iota_obs` e `kappa` continuam pendentes. Qualquer combinação que viole a condição bloqueia
o run; não existe correção por clamp.

Status:

```text
BASAL_ETA0_BOUND_ADMISSIBILITY = FROZEN_ANALYTIC
POST_HOC_CLAMPING = FORBIDDEN
```
'''
if '### 7.1.2.1. Critério analítico de admissibilidade de `eta0`' not in spec:
    spec=spec.replace(marker,marker+insert,1)

# Replace A1b temporal control subsection with frozen assignment semantics.
a=spec.index('## 17.3. Controle temporal obrigatório do instrumento A1b')
b=spec.index('## 17.4. Classificação prospectiva atual de ADIST0',a)
sec=r'''## 17.3. Regra de atribuição A1b — SEMÂNTICA CONGELADA

A1b deve alterar a distribuição de atenção **entre observadores**, preservando o volume
global de oportunidades em cada ciclo lógico. Para isso, congela-se a seguinte semântica:

```text
A1B_ASSIGNMENT_SEMANTICS = FIXED_PREASSIGNED_STRATA
A1B_GLOBAL_OPPORTUNITY_MASS = MATCHED_PER_LOGICAL_CYCLE
A1B_REACTIVE_REALLOCATION = FORBIDDEN
```

Antes de qualquer trajetória científica, uma seed do namespace exclusivo `A1B_ASSIGNMENT`
atribui os observadores aos estratos da condição heterogênea. A atribuição:

```text
não lê p_i
não lê EH
não lê omega/iota/B
não lê fila ou deadline miss
não lê eta_hat, D ou qualquer outcome
permanece fixa durante toda a janela W
```

A condição `UNIFORM` distribui oportunidades nominais o mais igualmente possível entre os
observadores em cada ciclo. Se restrições inteiras produzirem resto, usa-se rotação
round-robin predeterminada pela seed, sem consulta ao estado.

A condição `HETEROGENEOUS` utiliza dois estratos fixos:

```text
HIGH_ATTENTION_STRATUM
LOW_ATTENTION_STRATUM
```

com níveis prospectivos `q_H > q_L`. Proporção dos estratos e valores de `q_H`, `q_L`
continuam numéricos pendentes. Em todo ciclo `n`, entretanto, deve valer exatamente:

\[
\boxed{
\sum_i P^{obs}_{i,UNIFORM}(n)
=
\sum_i P^{obs}_{i,HETEROGENEOUS}(n).
}
\]

A partição fixa é escolhida para produzir heterogeneidade **entre observadores** no horizonte,
não heterogeneidade temporal criada por troca reativa de quem recebe recurso.

A barreira síncrona já congelada garante que velocidade física, ordem de mensagens e
interleaving de WebWorkers não participem do efeito.

Status:

```text
A1B_ASSIGNMENT_RULE_SEMANTICS = FROZEN
A1B_ASSIGNMENT_NUMERICS = UNFROZEN_REQUIRED_BEFORE_RUN
```

'''
spec=spec[:a]+sec+spec[b:]

# Pending lists: analytic eta admissibility no longer pending, assignment semantics frozen but levels remain.
spec=spec.replace('basal_eta0_bound_admissibility\n','')
spec=spec.replace('attention_to_observer_assignment_rule_A1b\nA1b_per_cycle_opportunity_levels',
                  'A1b_stratum_proportion\nA1b_q_H\nA1b_q_L\nA1b_per_cycle_opportunity_levels')
spec=spec.replace('NEXT = FREEZE_BASAL_NUMERICS_AND_A1B_ASSIGNMENT_THEN_COMPLETE_ADIST0_DERIVATIONAL_AUDIT',
                  'NEXT = FREEZE_BASAL_AND_SERVICE_NUMERICS_PLUS_A1B_LEVELS_THEN_COMPLETE_ADIST0_DERIVATIONAL_AUDIT')

specp.write_text(spec,encoding='utf-8')

tr=json.loads(tracep.read_text(encoding='utf-8'))
tr['status']='V2_0_0_A1B_ASSIGNMENT_SEMANTICS_AND_ETA_ADMISSIBILITY_FROZEN_PREPUBLICATION'
tr['basal_eta0_bound_admissibility']={
 'status':'FROZEN_ANALYTIC',
 'EH_domain':'[0,1]',
 'min_denominator':'m = 1 + iota_obs + min(0,kappa)',
 'required':'m>0 and 0<omega<=m',
 'if_kappa_nonnegative':'0<omega<=1+iota_obs',
 'post_hoc_clamping_forbidden':True,
 'numeric_values_pending':['omega','iota_obs','kappa']
}
tr['a1b_assignment_semantics']={
 'status':'FROZEN_FIXED_PREASSIGNED_STRATA',
 'assignment_rng_namespace':'A1B_ASSIGNMENT',
 'assignment_independent_of':['p_i','EH','omega','iota_obs','B_i','queue','deadline_miss','eta_hat','D','outcomes'],
 'fixed_during_W':True,
 'uniform_arm':'equal nominal opportunity allocation per cycle; deterministic seed-based round-robin only for integer remainder',
 'heterogeneous_arm':{'strata':['HIGH_ATTENTION_STRATUM','LOW_ATTENTION_STRATUM'],'relation':'q_H > q_L','stratum_proportion':'NUMERIC_PENDING','q_H':'NUMERIC_PENDING','q_L':'NUMERIC_PENDING'},
 'per_cycle_global_mass_constraint':'sum_i Pobs_i_uniform[n] == sum_i Pobs_i_heterogeneous[n] for every n',
 'reactive_reallocation_forbidden':True,
 'scientific_role':'A1B_INSTRUMENT_ISOLATION_RULE'
}

pending=[x for x in tr.get('unfrozen_required_before_run',[]) if x not in ('basal_eta0_bound_admissibility','attention_to_observer_assignment_rule_A1b')]
for x in ['A1b_stratum_proportion','A1b_q_H','A1b_q_L']:
    if x not in pending:
        # insert before existing per-cycle levels when possible
        try: idx=pending.index('A1b_per_cycle_opportunity_levels')
        except ValueError: idx=len(pending)
        pending.insert(idx,x)
tr['unfrozen_required_before_run']=pending

if 'a1b_derivational_audit' in tr:
    tr['a1b_derivational_audit']['instrument_isolation'].update({
      'assignment_semantics':'FROZEN_FIXED_PREASSIGNED_STRATA',
      'heterogeneous_strata':['HIGH_ATTENTION_STRATUM','LOW_ATTENTION_STRATUM'],
      'assignment_fixed_during_W':True,
      'assignment_rng_namespace':'A1B_ASSIGNMENT',
      'assignment_numerics':'PENDING'
    })
tr.setdefault('scientific_sequence',{})['A1b_continuation_condition']=(
 'Freeze omega/iota/kappa/B, service/deadline numerics and q_H/q_L/stratum proportion under the already frozen assignment semantics; then repeat ADIST0 before any scientific trajectory.'
)
tr['next_version']=(
 'Keep v2.0.0 while unpublished. Eta admissibility and A1b assignment semantics are frozen. Next freeze basal/service numerics and A1b levels, then complete the final ADIST0 derivational audit.'
)
tr.setdefault('prepublication_amendments',[]).append({
 'id':'V2_0_0_PREPUBLICATION_A1B_ASSIGNMENT_AND_ETA_BOUND_R3',
 'scientific_version_bump':False,
 'changes':['froze analytic eta0 admissibility criterion over EH in [0,1]','froze A1b fixed preassigned HIGH/LOW strata semantics','required exact per-cycle global opportunity mass matching','kept q_H/q_L/stratum proportion and basal/service values numerical pending']
})
tracep.write_text(json.dumps(tr,ensure_ascii=False,indent=2),encoding='utf-8')

readmep.write_text('''# HUMH A0/A1 v2.0.0 — estado pré-publicação\n\nA1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` (`ANBC0=FAIL_DERIVATIONAL`).\n\nA1b mantém `D` como candidato auditado, com classificação estrutural `CONDITIONAL_DISCRIMINATIVE` e confirmação ainda não autorizada.\n\nNovos congelamentos:\n\n- primeiro A1 basal e `B_i` homogêneos por isolamento;\n- ciclo científico em `SYNCHRONOUS_SNAPSHOT_BARRIER`;\n- admissibilidade de `eta0`: `m=1+iota_obs+min(0,kappa)>0` e `0<omega<=m`;\n- A1b usa estratos `HIGH_ATTENTION_STRATUM`/`LOW_ATTENTION_STRATUM` pré-atribuídos por seed independente e fixos durante `W`;\n- massa global de oportunidades é exatamente igual entre braços em cada ciclo;\n- `q_H`, `q_L`, proporção dos estratos e demais números continuam pendentes.\n\n`SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n''',encoding='utf-8')
parent.write_text('''# HUMH — Experimentos de Atenção\n\n`v2.0.0/` é a árvore corrente A0/A1 pré-publicação.\n\n- `ANBC0 = FAIL_DERIVATIONAL`;\n- `A1a = MECHANISM_DEMONSTRATION_ONLY [C1]`;\n- A1b: `D` candidato em auditoria estrutural `CONDITIONAL_DISCRIMINATIVE`;\n- regime basal/B homogêneo e barreira síncrona congelados;\n- critério analítico `0<eta0<=1` congelado;\n- semântica A1b HIGH/LOW fixa e exógena congelada, níveis ainda pendentes;\n- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.\n\nA teoria exibida pelo site permanece `../../teoria.md`; a cópia em `v2.0.0/02_dependencias/` é a dependência canônica hash-locked.\n''',encoding='utf-8')

lock=json.loads(lockp.read_text(encoding='utf-8'))
for item in lock.get('normative_artifacts',[]):
    if item['path'].endswith(specp.name): item['sha256']=sha(specp)
    if item['path'].endswith(tracep.name): item['sha256']=sha(tracep)
lock['publication_state']='REGENERATED_PRE_PUBLICATION_A1B_ASSIGNMENT_AND_ETA_BOUND_R3'
lock['A1b_confirmatory_authorized']=False
lock['A1b_assignment_semantics']='FROZEN_FIXED_PREASSIGNED_STRATA'
lockp.write_text(json.dumps(lock,ensure_ascii=False,indent=2),encoding='utf-8')

rootsha.write_text(f'{sha(specp)}  {specp.name}\n{sha(tracep)}  {tracep.name}\n',encoding='utf-8')
files=sorted(p for p in v.rglob('*') if p.is_file() and p!=sumsp)
sumsp.write_text('\n'.join(f'{sha(p)}  {p.relative_to(v).as_posix()}' for p in files)+'\n',encoding='utf-8')
print('SPEC_SHA256',sha(specp))
print('TRACE_SHA256',sha(tracep))
