from pathlib import Path
import hashlib, json, subprocess

V=Path('source/HUMH.Api/wwwroot/content/experimentos/atencao/v2.0.0')
S=V/'01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md'
T=V/'01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json'
D='3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a'
H='3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b'
N='baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b'
G={'AGOV0','AMEAS0','ABENCH0','AMAN0','AISO0','AETA0','ANBC0','ACOMP0','ASEP0','ADIST0','AINT0'}
STATUS='FAIL_INDEPENDENT_CONFIRMATORY_CONTENT_CURRENT_CONSTRUCTION'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,s): p.write_text(s,encoding='utf-8',newline='\n')
def dump(p,o): put(p,json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def rep(s,a,b):
    assert s.count(a)==1,(a,s.count(a))
    return s.replace(a,b,1)
def block(s,a,b,c):
    i=s.index(a);j=s.index(b,i+len(a));return s[:i]+c+s[j:]
def ref(a,h,s,t): return dict(artifact_id=a,sha256=h,section=s,clause_or_statement=t)
assert sha(S)=='58b91f15b583e1ce0dac726febe455e898d267bc6083509e2ce2959c4dace728'
assert sha(T)=='6c72c36864ce5abcb6d61dd37b6fe03e48bcf49246b2fb80f4a280fdd2f3c074'
subprocess.run(['python3',str(V/'03_integridade/verify.py')],check=True)
s=S.read_text();t=json.loads(T.read_text());assert {g['id'] for g in t['root_gates']}==G
s=rep(s,'**Status:** `PRE_CODE_SCHEDULE_FEASIBILITY_AND_DERIVATIONAL_AUDIT`','**Status:** `PRE_CODE_INDEPENDENT_CONTENT_AUDIT_CLOSED_R9`')
i=s.index('**Motivo:** ');j=s.index('\n\n---',i)
s=s[:i]+'**Motivo:** A0 não executado; A1a demonstração de mecanismo por ANBC0=FAIL_DERIVATIONAL. A1b não possui conteúdo confirmatório independente no gerador corrente. O testemunho R8 é derivacional e a ausência de uma identidade universal D_A→D não basta para discriminação. A hipótese não foi refutada; A2 não autorizado. Não se escolherão novos números para resgatar esta construção.'+s[j:]
s=rep(s,'A auditoria desse conteúdo próprio passa a ser o próximo bloqueio conceitual antes do\ncongelamento final dos números.','A auditoria desse conteúdo próprio está encerrada para a construção corrente no §17.4. A1b não recebe autorização confirmatória por escolha posterior de números.')
s=rep(s,'A1b não é consequência automática de H-A1S. Entretanto, qualquer outcome coletivo candidato deve primeiro passar por auditoria derivacional dentro de `ADIST0`, para excluir efeito que seja invariância ou consequência matemática automática da construção local.','A1b não é consequência automática de H-A1S. A auditoria de ADIST0 deve excluir invariância, efeito imposto e ausência de conteúdo independente do gerador. Não basta mostrar que D_A não determina universalmente D. O fechamento corrente está no §17.4.')
NEW=r'''## 17.4. Fechamento da auditoria de conteúdo independente — R9

A classificação preliminar `CONDITIONAL_DISCRIMINATIVE` foi excessiva: ela provava apenas que D_A não determina universalmente D(W). Isso não demonstra competência discriminativa. O R8 já oferece um contraste concreto derivacional. O fechamento abaixo aplica-se à construção atual, não a toda possível dinâmica coletiva.

### 17.4.1. Recorrência e alcance da inferência

Com alvo comum, parâmetros homogêneos e barreira síncrona:

\[
p_i[n+1]=p_{target}+(p_i[n]-p_{target])r_n^{k_i[n]},\qquad r_n=1-\eta_0(EH[n]).
\]

As conclusões k_i[n] decorrem da fila, demandas, deadlines e schedule; EH[n] decorre do snapshot anterior. Dados o estado inicial, a regra basal, a história exógena e o schedule, a trajetória é determinada recursivamente. A1b pode ter consequências emergentes não óbvias, mas executar esse gerador e recuperar sua própria recorrência demonstra consistência interna, não evidência independente de que a lei descreva outro substrato.

Modelos determinísticos podem gerar previsões não triviais e falsificáveis por dados independentes. O bloqueio corrente não é determinismo em si: é a ausência de um confronto independente e de alternativas capazes de contrariar a interpretação pretendida. O núcleo 1.9-A, A2, distingue C1 de C2/E; A5 proíbe inserir diretamente EH/kappa EH nos agentes cuja convergência confirmará N1a, e A6 exige o competidor aninhado. A regra basal atual contém eta0(EH), o que é admissível para demonstração declarada, mas não confirma independentemente N1a, H-A1S ou A1b.

### 17.4.2. Simetria do modelo homogêneo

Para uma permutação P aplicada conjuntamente a estados, filas e schedules, a dinâmica atual satisfaz:

\[
F(Pp,Pk)=P F(p,k).
\]

A média e EH são invariantes à permutação, os parâmetros e o alvo são comuns e não há leitura de vizinhos/topologia na atualização. Por indução, a trajetória apenas é permutada. Logo, a média, EH e D são exatamente iguais. Com estado inicial homogêneo, trocar o mesmo multiconjunto de schedules entre observadores homogêneos também preserva esses outcomes coletivos.

Portanto, a proposta futura de manter toda a distribuição de atenção e apenas trocar quem a recebe não possui conteúdo adicional nesta microdinâmica. Ela exigiria heterogeneidade basal ou interação estrutural efetiva previamente justificada. Não se introduzirá heterogeneidade auxiliar B_i apenas para produzir um efeito. A simetria não é uma afirmação sobre observadores reais.

### 17.4.3. Disposição da construção corrente

A hipótese dos §§67–69 permanece aberta: a distribuição de atenção pode conter informação dinâmica além da média. O R8 demonstra viabilidade do instrumento, não a verdade dessa hipótese. O modelo corrente não fornece conteúdo confirmatório independente suficiente para promover D a outcome primário de um teste da HUMH. O bloqueio é de desenho/identificação, não de potência ou de falta de um número conveniente.

```text
ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = FAIL_INDEPENDENT_CONFIRMATORY_CONTENT_CURRENT_CONSTRUCTION
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
A1b = MECHANISM_DEMONSTRATION_ONLY [C1]
A1b_PRIMARY_OUTCOME_D = FROZEN_FOR_AUDIT_NOT_CONFIRMATORY
A1b_THEORY_REFUTATION = FALSE
ADIST0_CONFIRMATORY_RUN = NOT_EXECUTED
SCIENTIFIC_RUN_NOT_AUTHORIZED
```

Essa disposição pertence ao subcheck existente, não cria Gate raiz nem refuta a teoria. Não significa que todos os schedules forcem o mesmo sinal. A1b pode ser demonstrado mecanicamente com rotulagem explícita, sem emitir ESTABLISHED/COMPATIBLE ou REFUTED. Não se escolherão eta_EH0, lambda_state, p_0, W, q_H, q_L ou margens para converter o bloqueio em PASS.

## 17.5. Próximo desenho sem resgate ad hoc

Preserva-se um experimento A0/A1: A0 como infraestrutura de mensuração e os módulos atuais A1a/A1b como diagnósticos mecanísticos. O próximo módulo coletivo poderá reutilizar o instrumento e a rastreabilidade, mas deverá receber especificação prospectiva antes de coleta científica.

A teoria §2.4.2 apresenta C2C como agregação de medições individuais, ajustes e nova agregação. Essa é uma linhagem pertinente, mas não fornece sozinha uma implementação A1 completa, parâmetros, margens, outcome independente ou evidência. Introduzir pooling ou média dos vizinhos no p_target atual violaria seu contrato; programar convergência e depois medi-la repetiria a auto-confirmação.

Antes do próximo run será necessário justificar a proveniência de um substrato coletivo, congelar sua dinâmica sem ajuste por outcomes A1, especificar rivais e uma previsão capaz de falhar e estabelecer a fonte independente da resposta. Um substrato computacional preexistente, selecionado por regra pré-registrada, ou coleta externa adequada são possibilidades. Uma ponte C1 continua útil para consistência, mas não é validação independente.

A distinção atenção/inércia/EH/recurso global, os controles locais, o pareamento e a sequência A0→A1a→A1b permanecem. Nenhuma nova hipótese, variável teórica, Gate raiz ou A2 é congelada aqui. O próximo trabalho é especificar conteúdo coletivo independente, não outro benchmark de schedules. Os números R8 continuam testemunho auxiliar.

---

'''
s=block(s,'## 17.4. Classificação prospectiva atual de ADIST0\n','# 18. Gates — lista fechada\n',NEW)
s=block(s,'# 26. Itens de desenho e números ainda NÃO congelados\n','# 28. Regra automática de rastreabilidade para o código\n','''# 26. Parâmetros e autorização

B=1, K_C=2 e L_A=1 permanecem contratos da operacionalização mecanística, não constantes estimadas da HUMH. N, W, parâmetros basais, atratores, episódios, níveis instrumentais, margens e poder confirmatórios não foram escolhidos. Os números A1b são diferidos até existir desenho científico autorizado; não serão escolhidos para contornar ADIST0.

# 27. Procedimento autorizado

A0 e o auditor de schedules podem continuar tecnicamente, sem outcomes científicos. A1a/A1b atuais só poderão ser executados como demonstrações mecanísticas explicitamente rotuladas, após congelamento e integridade aplicáveis. Não há autorização para busca numérica confirmatória.

O próximo trabalho científico é especificar prospectivamente um substrato coletivo independente ou uma ponte a confrontar com dados independentes. Essa escolha precede dinâmica, rivais, outcomes, margens, poder e seeds. O instrumento A0 poderá ser reutilizado se seu mapeamento for validado no novo substrato. Mantém-se v2.0.0 pré-publicação; teoria, núcleo, programa N3 e A2 não são alterados.

---

''')
a=s.index('## A1b\n',s.index('# 29. Critérios de conclusão'));b=s.index('## A2\n',a)
s=s[:a]+'## A1b\n\nA auditoria final da construção corrente é `'+STATUS+'`. D permanece candidato auditado, não outcome confirmatório. A1b é demonstração de mecanismo [C1], sem run confirmatório, sem refutação teórica e sem autorização para resgate numérico. As categorias gerais permanecem disponíveis para um futuro desenho adequado.\n\n'+s[b:]
s=rep(s,'NEXT = FREEZE_BASAL_AND_SERVICE_NUMERICS_PLUS_A1B_LEVELS_THEN_COMPLETE_ADIST0_DERIVATIONAL_AUDIT','NEXT = SPECIFY_INDEPENDENT_COLLECTIVE_CONTENT_BEFORE_NEW_SCIENTIFIC_NUMERICS')
put(S,s)
t['status']='V2_0_0_INDEPENDENT_CONTENT_AUDIT_CLOSED_R9_PREPUBLICATION';t['scientific_run_authorized']=False
for g in t['root_gates']:
    if g['id']=='ANBC0':g['pre_run_status']='FAIL_DERIVATIONAL'
a=t['result_logic']['A1b'];a.update(current_authorization='NOT_AUTHORIZED_INDEPENDENT_CONTENT_BLOCK',derivational_audit_structural='GENERAL_NONIDENTITY_ONLY_NOT_SUFFICIENT',derivational_audit_final=STATUS,pre_numeric_derivational_classification='GENERAL_NONIDENTITY_ONLY_NOT_SUFFICIENT',current_confirmatory_authorization=False,current_disposition='MECHANISM_DEMONSTRATION_ONLY [C1]',candidate_status='FROZEN_FOR_STRUCTURAL_AUDIT_NOT_CONFIRMATORY',current_allowed_results=['MECHANISM_DEMONSTRATION_ONLY [C1]','INCONCLUSIVE_TECHNICAL_OR_IMPLEMENTATION'],current_forbidden_results=[v for v in a['allowed_results'] if v!='INCONCLUSIVE_*'],current_rule='Current generator lacks independent confirmatory content; no numerical rescue. The theoretical hypothesis is not refuted.')
t['scientific_sequence']['A1b_continuation_condition']='Current confirmatory construction blocked. Preserve A0 and mechanism diagnostics; specify independent collective content before numerical design. A2 unauthorized.'
t['scientific_sequence']['current_A1b_disposition']='MECHANISM_DEMONSTRATION_ONLY [C1]'
a=t['a1b_derivational_audit'];a.update(status_structural='GENERAL_NONIDENTITY_ONLY_NOT_SUFFICIENT',status_final=STATUS,confirmatory_authorized=False,current_confirmatory_authorization=False,anti_rescue='No numeric rescue of current confirmatory construction.')
a['primary_outcome_candidate']['status']='FROZEN_FOR_STRUCTURAL_AUDIT_NOT_CONFIRMATORY'
a['general_state_dependent_case']['scientific_interpretation']='General nonidentity does not establish independent-content discrimination.'
a['R9_closure']=dict(kind='GATE_SUBCHECK',parent_gate='ADIST0',status=STATUS,theory_refutation=False,confirmatory_run_executed=False,permutation_equivariance='F(Pp,Pk)=P F(p,k) for homogeneous non-networked basal construction',scope_limit='Does not claim all schedules force one sign or deterministic models cannot be tested independently',canonical_refs=[ref('HUMH_ATTENTION_DEFINITION_1.0.0',D,67,'Attention distribution effect at fixed mean.'),ref('HUMH_ATTENTION_DEFINITION_1.0.0',D,69,'A1b is not automatic from H-A1S.'),ref('HUMH_ATTENTION_DEFINITION_1.0.0',D,108,'Separability must distinguish rivals without constructing the answer.'),ref('HUMH_ATTENTION_DEFINITION_1.0.0',D,116,'A1b result logic and frozen inference.'),ref('HUMH_NUCLEUS_CANONICAL',N,'A2','C1 versus independent C2/E substrata.'),ref('HUMH_NUCLEUS_CANONICAL',N,'A4','D is distinct from EH.'),ref('HUMH_NUCLEUS_CANONICAL',N,'A5','N1a prohibits direct EH causal insertion in confirmatory agents.'),ref('HUMH_NUCLEUS_CANONICAL',N,'A6','Nested competitor without EH term.'),ref('HUMH_THEORY_CANONICAL',H,'4.2.5','Basal state-dependent rate.'),ref('HUMH_THEORY_CANONICAL',H,'4.4.2','Discrete basal update.')])
t['canonical_artifact_registry'].setdefault('HUMH_NUCLEUS_CANONICAL',dict(sha256=N,role='lineage-only, not bundled or modified'))
old=t['unfrozen_required_before_run'];deferred=[x for x in old if x.startswith(('A1b_','ADIST0_'))]
t['unfrozen_required_before_run']=[x for x in old if x not in deferred]
t['deferred_confirmatory_design']=dict(kind='GOVERNANCE_STATUS',status='DEFERRED_PENDING_INDEPENDENT_CONTENT',fields=deferred,canonical_refs=[ref('HUMH_ATTENTION_DEFINITION_1.0.0',D,70,'Numerical arms not frozen by definition.'),ref('HUMH_ATTENTION_DEFINITION_1.0.0',D,71,'No outcome-based contrast selection.'),ref('HUMH_ATTENTION_DEFINITION_1.0.0',D,120,'Freeze design before scientific collection.')])
t['next_version']='Keep unpublished v2.0.0; current A1a/A1b mechanism only. Specify independent collective content before confirmatory numerics. A2 unauthorized.'
t['prepublication_amendments'].append(dict(id='V2_0_0_PREPUBLICATION_INDEPENDENT_CONTENT_CLOSURE_R9',scientific_version_bump=False,changes=['Closed current A1b independent-content audit without numerical rescue','Preserved R8 witness and corrected the general-nonidentity inference','Proved homogeneous permutation equivariance','Deferred confirmatory numerical design; preserved A0 and A2 prohibition']))
assert {g['id'] for g in t['root_gates']}==G
assert not t['result_logic']['A1a']['current_confirmatory_authorization'] and not a['confirmatory_authorized']
assert t['result_logic']['A2']['result']=='NOT_AUTHORIZED / NOT_TESTED'
registry={k:v['sha256'] for k,v in t['canonical_artifact_registry'].items()}
for obj in (a['R9_closure'],t['deferred_confirmatory_design']):
    for r in obj['canonical_refs']:
        assert registry[r['artifact_id']]==r['sha256'] and set(('artifact_id','sha256','section','clause_or_statement'))<=r.keys()
dump(T,t)
L=V/'02_dependencias/DEPENDENCIES.lock.json';l=json.loads(L.read_text());l.update(publication_state='REGENERATED_PRE_PUBLICATION_INDEPENDENT_CONTENT_R9',A1b_structural_audit=STATUS,A1b_structural_audit_scope='CURRENT_GENERATOR_NO_INDEPENDENT_CONFIRMATORY_CONTENT',A1b_confirmatory_authorized=False,A1b_current_disposition='MECHANISM_DEMONSTRATION_ONLY [C1]',scientific_run_authorized=False)
for x in l['normative_artifacts']:x['sha256']=sha(V/x['path'])
dump(L,l)
for p,msg in [(V/'README.md','\n## R9 — conteúdo independente\n\nA1a/A1b atuais são demonstrações de mecanismo, não testes confirmatórios. A1b não foi refutada; a auditoria do gerador foi encerrada. O próximo desenho requer conteúdo coletivo independente antes de novos números. A0 permanece não executado e A2 não autorizado. Ver §§17.4–17.5, 26–27 e 29.\n'),(V.parent/'README.md','\nR9: auditoria de conteúdo independente encerrada; A1a/A1b somente demonstração de mecanismo. Ver v2.0.0.\n')]:put(p,p.read_text()+msg)
q=V/'HUMH_A0_A1_v2.0.0.sha256';put(q,f'{sha(S)}  {S.name}\n{sha(T)}  {T.name}\n')
sums=V/'03_integridade/SHA256SUMS.txt';paths=[x.split('  ',1)[1] for x in sums.read_text().splitlines() if x.strip()]
assert set(paths)=={str(p.relative_to(V)) for p in V.rglob('*') if p.is_file() and p!=sums}
put(sums,''.join(f'{sha(V/p)}  {p}\n' for p in paths))
for dep in l['active_canonical_dependencies']:assert sha(V/dep['path'])==dep['sha256']
subprocess.run(['python3',str(V/'03_integridade/verify.py')],check=True)
print('SPEC_SHA256',sha(S));print('TRACE_SHA256',sha(T));print('ROOT_GATES',len(G));print('SCIENTIFIC_RUN_AUTHORIZED',False)
