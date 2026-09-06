# HUMH — A0/A1 · Especificação Experimental v2.0.0
## Reset de rastreabilidade à definição canônica

**Identidade:** `HUMH_A0_A1_SPEC_2.0.0_TRACEABILITY_RESET`  
**Referente normativo primário para A0/A1:** `HUMH_ATTENTION_DEFINITION_1.0.0`  
**Definition SHA-256:** `3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a`  
**Theory SHA-256:** `3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b`  
**Nucleus SHA-256:** `baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b`  
**Program SHA-256:** `a9bfd724b7af7849711570798eb8134282fa93fe39093fbd7f4b637041f5a226`  
**KREF0 SHA-256:** `234c752534589f84d53836cdc18d3964ba30c17783292f977fbf6fcfdeeef6f7`

**Status:** `PRE_CODE_A1B_STRUCTURAL_AUDIT`  
**Run científico:** `SCIENTIFIC_RUN_NOT_AUTHORIZED`  
**Motivo:** A1a permanece `MECHANISM_DEMONSTRATION_ONLY [C1]` por `ANBC0=FAIL_DERIVATIONAL`. A auditoria de A1b foi refinada: `D` continua candidato canônico, mas `D_A` determina apenas a quantidade total de conclusões por observador, não a exposição temporal aos fatores de atualização dependentes do estado coletivo. Para impedir que ordem física de WebWorkers se torne variável científica, congela-se uma barreira síncrona por ciclo lógico e um regime basal homogêneo para o primeiro A1. A classificação final de `ADIST0` continua anterior a qualquer trajetória científica.

---

# 1. Regra-mãe de v2.0.0

> **Nenhuma variável, Gate, hipótese, contraste, margem ou condição de decisão entra no experimento sem apontar primeiro qual afirmação da definição canônica ela operacionaliza.**

Esta regra é executável:

1. todo item científico ou de integridade deve existir no `HUMH_A0_A1_Traceabilidade_v2.0.0.json`;
2. todo item deve informar `canonical_refs`;
3. cada `canonical_ref` deve conter, no mínimo, `artifact_id`, `sha256`, `section` e `clause_or_statement`;
4. `canonical_refs=[]` invalida o item;
5. o SHA declarado em cada referência deve coincidir com o artefato canônico registrado no manifesto;
6. itens apenas de implementação devem ser marcados `IMPLEMENTATION_ONLY` e não podem entrar em nenhuma conclusão científica;
7. nenhum novo Gate científico pode ser acrescentado durante a implementação;
8. verificações auxiliares podem existir apenas como **subchecks** de um Gate canônico já autorizado;
9. se uma necessidade nova não puder ser mapeada a um artefato canônico qualificado, a implementação para e a spec precisa ser revista antes de nova coleta.

---


## 1.1. Autoridade normativa desta versão

A v2.0.0 consolidada possui exatamente dois artefatos normativos:

```text
HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md
HUMH_A0_A1_Traceabilidade_v2.0.0.json
```

Arquivos auxiliares produzidos durante a elaboração da v2.0.0 não possuem autoridade
normativa e não são necessários para interpretar, implementar ou auditar o desenho.

Toda regra válida de `p_alvo`, instrumento de atenção, `AETA0`, `ANBC0`, `M_alt`,
lógica de resultados e sequência científica está incorporada nestes dois artefatos.


# 2. Regra de não herança científica da série v1.0.x

A série experimental v1.0.x é classificada, para a v2.0.0, como:

`PREVIOUS_OUTCOMES_EXPOSED_DIAGNOSTIC_ONLY`

Ela pode ser usada para reconhecer bugs de software, riscos de implementação e necessidades de auditoria já conhecidas.

Ela **não pode** ser usada para escolher na v2.0.0:

- braços HIGH/MID/LOW;
- regras/níveis correspondentes de alocação de oportunidades;
- `W`;
- `L_A`, exceto via novo `ABENCH0` cego técnico;
- `delta_drive`;
- número mínimo de passos;
- informação mínima `sum(x^2)`;
- fronteiras dos estratos de estado;
- margem de equivalência/refutação;
- subconjunto de contrastes;
- tamanho amostral;
- regra de multiplicidade;
- competência mínima de `ACOMP0`.

Nenhum resultado v1.0.x é reclassificado por esta spec.

---

# 3. Sequência científica autorizada pela definição

A v2.0.0 preserva literalmente a sequência conceitual:

```text
A0  = ATTENTION MEASUREMENT CONTRACT
A1a = ATTENTION MULTIPLICATIVE SEPARABILITY
A1b = ATTENTION DISTRIBUTION EFFECT
A2  = ATTENTION–MACRO TRANSPORT — NOT AUTHORIZED / NOT TESTED
```

Não há A2 nesta especificação.

---

# 4. Vocabulário teórico fechado

## 4.1 Atenção individual

\[
\boxed{
A_i(W)=\frac{U_i(W)}{D_i(W)}
}
\]

`A_i` é a variável teórica de atenção.

### D_i(W)

\[
D_i(W)=
\#\{\text{requisições observacionais elegíveis geradas exogenamente para }O_i\text{ em }W\}.
\]

### U_i(W)

Número de requisições de `D_i` cuja cadeia

\[
observação\rightarrow processamento\rightarrow atualização
\]

termina dentro do deadline lógico comum.

### W

Janela em ciclos lógicos.

### L_A

Uma requisição criada em `t` entra em `U_i` somente se:

\[
t_{complete}\le t+L_A.
\]

`L_A` é comum aos braços e independente de atenção, `EH`, inércia e outcome.

## 4.2 Atenção coletiva

\[
\boxed{
\bar A=\frac1N\sum_i A_i
}
\]

\[
\boxed{
D_A=\frac1N\sum_i|A_i-\bar A|
}
\]

Estas são as únicas agregações de atenção autorizadas pela definição para A1.

## 4.3 Variáveis que NÃO existem nesta teoria

Ficam proibidas como variáveis científicas da v2.0.0:

```text
A_global
A_by_stratum
A_stratum
AEXP
exposure_stability_across_EH
qualquer outra redefinição de A_i por estrato de EH
```

É permitido calcular valores temporários para depuração do software, desde que sejam `IMPLEMENTATION_ONLY`, não persistam no dataset científico e não participem de Gates ou decisões.

---

# 5. Instrumento causal de atenção

A variável de implementação causal é:

\[
P_i^{obs}
\]

com cadeia:

\[
\boxed{
P_i^{obs}\rightarrow A_i.
}
\]

`P_i^{obs}` é o instrumento causal; nesta v2.0.0 ele é operacionalizado pela **alocação exógena de oportunidades de execução ao observador**.

`B_i`, definido abaixo, representa capacidade basal computacional do observador por oportunidade. Ele **não é atenção**, não é manipulado entre braços pareados e não pode ser usado como substituto de `A_i`.

O scheduler pode decidir quantas/quais oportunidades de execução são concedidas e verificar o cumprimento de `L_A`, mas não pode modificar demanda exógena, capacidade basal do observador, dinâmica estrutural ou regra interna de atualização em função do braço.

---


# 5.1. Instrumento computacional de atenção — congelado

A variável teórica permanece exclusivamente:

\[
\boxed{A_i(W)=U_i(W)/D_i(W)}.
\]

A implementação separa explicitamente:

\[
\boxed{
\text{trabalho da tarefa}
+
\text{capacidade basal do observador}
+
\text{oportunidades concedidas}
+
\text{deadline}
\longrightarrow U_i
}
\]

Nenhum desses componentes isoladamente é atenção.

## 5.1.1. Capacidade basal do observador

Define-se, como operacionalização computacional auxiliar:

\[
\boxed{
B_i=
\text{quantidade máxima de trabalho observacional processada por }O_i
\text{ em uma oportunidade}
}
\]

Implementação:

```text
observer_buffer_capacity
```

Nesta v2.0.0:

```text
B_i = FIXED_WITHIN_OBSERVER
B_i_HIGH = B_i_LOW para o mesmo observador pareado
B_i != A_i
B_i != P_i_obs
```

Para a teoria geral, observadores poderiam possuir capacidades auxiliares diferentes.
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

## 5.1.2. Trabalho exigido pela tarefa

Cada demanda `j` possui:

\[
\boxed{
C_j=\texttt{required_work}_j
}
\]

determinado antes de consultar o braço.

`C_j` permanece idêntico para o mesmo `demand_id` em todos os braços pareados.

É permitido:

\[
C_j>B_i.
\]

Isso não torna a tarefa impossível. Ela é processada em partes ao longo de múltiplas
oportunidades.

Para uma tarefa isolada, sem espera anterior na fila:

\[
\boxed{
n^{req}_{ij}
=
\left\lceil\frac{C_j}{B_i}\right\rceil
}
\]

é o número mínimo de oportunidades necessárias.

Portanto, se `B_i>0`, `C_j` é finito, oportunidades continuam sendo concedidas e não
existe deadline, a tarefa pode ser concluída mesmo quando `C_j>B_i`.

O buffer define **quanto pode ser processado por oportunidade**, não o tamanho máximo
de tarefa que o observador consegue resolver.

## 5.1.3. Instrumento de atenção: oportunidades

Nesta v2.0.0:

```text
P_i_obs = observer_opportunity_schedule
```

`observer_opportunity_schedule` é uma regra exógena, congelada e dependente do braço
que determina as oportunidades de processamento concedidas ao observador ao longo dos
ciclos lógicos.

```text
observer_opportunity_schedule != A_i
observer_buffer_capacity != A_i
P_i_obs -> oportunidades concedidas -> U_i/D_i
```

O braço HIGH **não aumenta `B_i`**. O mesmo observador conserva a mesma capacidade basal;
muda somente a disponibilidade de oportunidades para empregar essa capacidade.

A regra de oportunidades não pode reagir a:

```text
p_i
EH
sucesso/falha
deadline_miss observado
eta_hat
consenso
outcome
fila futura
estado futuro
```

## 5.1.4. Pareamento entre braços

Para o mesmo observador em braços pareados permanecem idênticos:

```text
observer_id
estado inicial
parâmetros basais do observador
observer_buffer_capacity = B_i
sequência de demandas
demand_id
payload/conteúdo
required_work = C_j
regra de processamento
regra basal de atualização
L_A
seeds exógenas
topologia
arrivals
serviço
propagação
```

Varia somente:

```text
observer_opportunity_schedule = P_i_obs
```

## 5.1.5. Tempo científico

```text
logical_cycle = SCIENTIFIC_TIME
wall_clock_ms = DIAGNOSTIC_ONLY
cpu_time_ms = DIAGNOSTIC_ONLY
```

O resultado científico não pode depender de turbo, clock físico, escalonamento real
do sistema operacional ou duração real do WebWorker.

## 5.1.6. Demanda e trabalho remanescente

Cada demanda é definida antes de consultar o braço:

```text
demand_id
observer_id
arrival_cycle
payload_id
payload
required_work = C_j
remaining_work
deadline_cycle = arrival_cycle + L_A
```

`required_work` é `arm-blind`.

```text
WORK_QUANTUM = 1
```

é unidade abstrata de trabalho lógico, não ms, instrução física, MHz ou %CPU.

## 5.1.7. Fila observacional

Cada observador possui fila:

```text
FIFO_DETERMINISTIC
```

A ordem deriva das demandas exógenas e não pode depender do braço, `EH`, sucesso/falha
ou outcome.

A espera por tarefas anteriores pode atrasar uma demanda. Isso não altera `B_i`.

## 5.1.8. Algoritmo lógico de serviço

No início de cada ciclo, a regra de expiração é estritamente:

\[
oxed{
	exttt{expire}
\iff
	exttt{current_cycle}>	exttt{deadline_cycle}
}
\]

Em pseudocódigo:

```text
for each queued demand:
    if current_cycle > job.deadline_cycle:
        expire job
        -> remains in D_i
        -> does not enter U_i
        -> does not generate late basal update
```

Portanto, quando:

```text
current_cycle == deadline_cycle
```

a demanda **ainda é elegível para receber oportunidade e concluir naquele ciclo**.

Isso é coerente com o contrato:

\[
t_{complete}\le t+L_A.
\]

Depois:

```text
n_granted = observer_opportunity_schedule(observer_id, arm, current_cycle)
```

Para cada oportunidade concedida:

```text
if queue is empty:
    stop this opportunity

job = queue.front

q = min(observer_buffer_capacity, job.remaining_work)
execute exactly q logical work quanta
job.remaining_work -= q

if job.remaining_work == 0:
    execute exactly one instance of the same basal observer update
    record completion_cycle

    if completion_cycle <= job.deadline_cycle:
        count exactly once in U_i

    remove job from queue

end opportunity
```

Uma oportunidade atua somente sobre a demanda na frente da fila. Capacidade não usada
porque essa demanda terminou não é transferida para outra demanda na mesma oportunidade.

Assim, para uma tarefa isolada:

\[
n^{req}_{ij}=\left\lceil C_j/B_i\right\rceil.
\]

## 5.1.9. Deadline e atenção efetiva

Uma demanda conta em `U_i` apenas se completar até o deadline.

Logo, `U_i` depende conjuntamente de:

```text
C_j                            trabalho da tarefa
B_i                            capacidade basal do observador
observer_opportunity_schedule  oportunidades disponibilizadas
L_A                            tempo válido
estado da fila                 contenção temporal
```

e a atenção continua exclusivamente:

\[
\boxed{A_i=U_i/D_i}.
\]

## 5.1.10. Não equivalências

É proibido definir:

```text
A_i := observer_buffer_capacity
A_i := observer_opportunity_schedule
A_i := opportunities_granted
A_i := 1 / processing_latency
A_i := CPU_percent
A_i := thread_priority
A_i := wall_clock_speed
```

## 5.1.11. Manipulation check

Não basta HIGH receber mais oportunidades nominais que LOW.

`ABENCH0/AMAN0` deve confirmar contraste adequado em:

\[
A_{HIGH}>A_{LOW}
\]

sem alterar `B_i`, `C_j`, demanda, substrato ou regra basal do observador.

`eta_hat`, `EH`, consenso e outcomes A1a/A1b não podem participar da escolha das regras
de oportunidades.

## 5.1.12. Separação de CANAL_ETA e da atualização basal

O módulo `CANAL_ETA` e a rotina basal que altera `p_i` não recebem:

```text
observer_buffer_capacity
observer_opportunity_schedule
opportunities_granted
D_i
U_i
A_i
deadline_misses
remaining_work
queue_length
```

`B_i` atua somente na camada de processamento da demanda. Depois de a demanda ser
integralmente processada, ele não determina quanto `p_i` muda.

Somente após os dois canais terminarem é permitido comparar `eta_hat` com `A_i`.

## 5.1.13. Parâmetros numéricos pendentes

A semântica e o regime de isolamento já estão congelados. Antes do run ainda devem ser congelados:

```text
basal_eta0_bound_admissibility
observer_buffer_capacity_value
required_work_rule
required_work_range_or_distribution
observer_opportunity_arm_rules
ABENCH0_opportunity_candidate_rules
L_A
W
number_of_arms
instrumental_contrast_criteria
saturation_avoidance_criteria
```

Status:

```text
ATTENTION_INSTRUMENT_SEMANTICS = FROZEN
OBSERVER_PROCESSING_CAPACITY_SEMANTICS = FROZEN_AUXILIARY
OBSERVER_BUFFER_HETEROGENEITY_REGIME = HOMOGENEOUS_FROZEN_FOR_FIRST_A1
ATTENTION_INSTRUMENT_ALGORITHM = FROZEN_OPPORTUNITY_ALLOCATION
ATTENTION_INSTRUMENT_NUMERICS = UNFROZEN_REQUIRED_BEFORE_RUN
```

## 5.1.14. Barreira síncrona do ciclo lógico — CONGELADA

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

# 6. Dois canais de mensuração — separação obrigatória

## CANAL_A

Entradas permitidas:

```text
D_i
U_i
```

Saída:

\[
A_i=U_i/D_i.
\]

## CANAL_ETA

Entradas permitidas:

```text
p_i(t)
p_alvo,i(t)
metadados estritamente necessários para elegibilidade de trajetória
```

Defina:

\[
x_{it}=p_{alvo,i}(t)-p_i(t)
\]

\[
y_{it}=p_i(t+1)-p_i(t)
\]

e, para cada observador/condição/estrato de estado prospectivamente definido:

\[
\boxed{
\widehat\eta=
\frac{\sum_{t\in\mathcal E}x_{it}y_{it}}
{\sum_{t\in\mathcal E}x_{it}^{2}}
}
\]

O CANAL_ETA é proibido de ler direta ou indiretamente:

```text
U_i
D_i
A_i
A_bar
D_A
attention_arm
attention_opportunity_allocation
served_fraction
deadline_misses
```

A razão `eta_hat/A_i` só é formada depois de os dois canais terminarem.

---


# 6.1. Contrato operacional de `p_alvo` — CONGELADO

A linhagem canônica permite fechar o significado de `p_alvo` sem criar uma nova variável.

Na teoria basal:

\[
\frac{dp}{dt}
=
\eta(p)\,[p_{\text{alvo}}(s)-p(t)],
\]

e `p_alvo(s)` é o **atrator basal ativo** determinado pelo estado do sistema. No regime estável em A, antes de saturação, `p_alvo=p_A`; no regime estável em B, antes de saturação, `p_alvo=p_B`.

A definição de atenção individualiza apenas o registro:

\[
x_{it}=p_{\text{alvo},i}(t)-p_i(t),
\]

exigindo que `p_alvo,i(t)` seja produzido pela dinâmica basal antes da atualização e sem usar contadores de atenção.

Portanto, A1 congela:

\[
\boxed{
p_{\text{alvo},i}(t)=p_{Z_e}
}
\]

onde:

```text
e   = episódio basal
Z_e ∈ {A,B} = atrator basal ativo do episódio
p_{Z_e} ∈ {p_A,p_B}
```

e o mesmo `p_{Z_e}` vale para todos os observadores e todos os ciclos pertencentes ao episódio `e`.

Status:

```text
P_TARGET_OPERATIONAL_STATUS = FROZEN_STATIONARY_ACTIVE_ATTRACTOR
```

## 6.1.1. Por que o episódio é estacionário

A1 testa atenção, não a mecânica de saturação/manutenção nem a troca de atratores.

A hipótese H-A1S exige comparação para o mesmo observador/estado basal. Portanto, a unidade primária de identificação de `eta_hat` é um trecho no qual o atrator basal ativo permanece fixo.

A1 utiliza apenas os trechos canônicos:

```text
REGIME_A_UNSATURATED: p_alvo = p_A
REGIME_B_UNSATURATED: p_alvo = p_B
```

A transição:

```text
A -> B por saturação
B -> A por saturação
```

não é outcome de A1 e não entra no estimando de A1a.

Isso não afirma que a saturação não exista. Apenas condiciona A1 a janelas basais estacionárias para não misturar atenção com a dinâmica de troca de atrator.

## 6.1.2. O que `p_alvo` NÃO é em A1

Ficam explicitamente excluídos:

```text
p_alvo != A_i
p_alvo != A_bar
p_alvo != D_A
p_alvo != U_i/D_i
p_alvo != budget
p_alvo != attention_arm
p_alvo != served_fraction
p_alvo != média dos vizinhos
p_alvo != maioria dos vizinhos
p_alvo != consenso observado no mesmo ciclo
p_alvo != reconstrução pós-hoc da trajetória
```

Um sinal observacional ou evidência local pode fazer parte do conteúdo da demanda basal, mas **não redefine `p_alvo`**: o alvo do estimador continua sendo o atrator basal ativo.

## 6.1.3. Ordem temporal obrigatória

Para cada episódio `e` e ciclo `t`:

```text
1. Z_e já está congelado antes do ciclo.
2. Registrar p_pre_i(t) = p_i(t).
3. Registrar p_alvo_i(t) = p_Ze.
4. Gerar/registrar a demanda observacional D_i(t) e seu conteúdo exógeno.
5. O scheduler decide apenas oportunidade/serviço/deadline.
6. Se a cadeia observacional for executada, chamar a rotina basal do observador.
7. Registrar p_i(t+1).
8. Somente depois formar:
      x_it = p_alvo_i(t) - p_i(t)
      y_it = p_i(t+1) - p_i(t)
```

A rotina do observador não recebe:

```text
A_i
A_bar
D_A
attention_arm
attention_opportunity_allocation
served_fraction
```

## 6.1.4. Pareamento e CRN

Para braços de atenção comparados dentro da mesma replicação:

```text
episode_id                 idêntico
Z_e                        idêntico
p_alvo                     idêntico
estado inicial pareado     idêntico
conteúdo de D_i            idêntico
RNG exógeno basal          idêntico por chave
topologia                  idêntica
microdinâmica basal        idêntica
```

A única intervenção autorizada é:

```text
P_i_obs -> A_i
```

Se o checksum da sequência `(episode_id, Z_e, p_alvo, D_i content)` divergir entre braços:

```text
AINT0 = FAIL
ASEP0 = INCONCLUSIVE_INTEGRITY
```

## 6.1.5. Identidade entre observadores

O índice `i` em `p_alvo,i(t)` existe para que cada linha de trajetória seja auto-contida.

No A1 inicial:

\[
\boxed{
p_{\text{alvo},1}(t)=\cdots=p_{\text{alvo},N}(t)=p_{Z_e}
}
\]

dentro do mesmo episódio.

A1 não introduz alvos idiossincráticos por observador.

## 6.1.6. Parâmetros numéricos ainda delegados à versão run-ready

O significado de `p_alvo` fica congelado aqui, mas ainda devem ser congelados prospectivamente, sem usar outcomes v1.0.x:

```text
p_A
p_B
número de episódios A/B
ordem/balanceamento dos episódios
comprimento de episódio
regra de inicialização de p_i
burn-in, se houver
regra exata que certifica ausência de troca de atrator dentro do episódio
```

Esses parâmetros são de desenho; não mudam a definição de `p_alvo`.

## 6.1.7. Referências canônicas

`p_alvo` possui referências qualificadas a:

1. `HUMH_ATTENTION_DEFINITION_1.0.0`, §§38–39:
   - CANAL_ETA usa `p_i(t), p_alvo,i(t)`;
   - o alvo deve ser registrado pela dinâmica basal antes da atualização;
   - o alvo não pode ser reconstruído dos contadores de atenção.

2. `teoria.md`, §4.3.5:
   - `dp/dt = eta(p)[p_alvo(s)-p(t)]`;
   - em A não saturado, `p_alvo=p_A`;
   - em B não saturado, `p_alvo=p_B`;
   - a troca de alvo pertence à dinâmica de saturação.

3. `HUMH_ATTENTION_DEFINITION_1.0.0`, §§45, 47–50:
   - scheduler decide apenas oportunidade de execução;
   - H-A1S compara a resposta de atenção para o mesmo estado basal;
   - `eta/A` é o objeto normalizado, não uma redefinição do alvo.

Com isso:

```text
P_TARGET_SEMANTIC_CONTRACT = FROZEN
P_TARGET_NUMERICS = UNFROZEN_REQUIRED_BEFORE_RUN
```

`p_alvo` deixa de ser bloqueio conceitual de v2.0.0. O run científico continua não autorizado pelos demais parâmetros ainda não congelados.

# 7. Regra executada pelo observador

É proibido inserir na rotina do observador:

```text
A_i
A_bar
D_A
attention_arm
attention_opportunity_allocation
served_fraction
qualquer transformação direta desses itens
```

Em particular, a equação teórica

\[
\eta_i(A,p)=
A_i\frac{\omega_i}{1+\iota_{obs,i}+\kappa EH(p)}
\]

**não pode** ser codificada como regra de atualização.

Ela é hipótese macroscópica/observacional a ser confrontada pelos dois canais independentes.

---


## 7.1. Microdinâmica basal do observador — CONGELADA

A teoria-base já fornece duas peças suficientes para fechar a forma basal sem criar uma
nova dinâmica científica:

1. em `teoria.md`, §4.2.5:

\[
\eta_i^{(0)}(p)
=
\frac{\omega_i}
{1+\iota_{obs,i}+\kappa EH(p)};
\]

2. em `teoria.md`, §4.4.2, a formulação discreta computacional:

\[
p[n+1]
=
p[n]+\eta\,[p^*-p[n]].
\]

A definição canônica de atenção, §37, individualiza a taxa basal como
`\eta_i^{(0)}(p)`, e §§44–45 proíbem que a rotina executada leia atenção, braço,
budget ou fração atendida.

Portanto, para uma demanda `j` que termine integralmente dentro de seu deadline,
congela-se:

\[
\boxed{
g_{ij}
=
\eta_i^{(0)}(p^-_{ij})
\,[p_{\text{alvo},ij}-p^-_{ij}]
}
\]

e:

\[
\boxed{
p^+_{ij}=p^-_{ij}+g_{ij}.
}
\]

Onde:

```text
p^-_ij     = estado imediatamente antes da atualização produzida pela demanda j
p^+_ij     = estado imediatamente depois dessa atualização
p_alvo_ij  = atrator basal ativo já congelado pelo contrato de p_alvo
```

A rotina basal recebe somente:

```text
p_pre
p_alvo
omega_i
iota_obs_i
kappa
EH(p_pre)
```

e não recebe:

```text
A_i
D_i
U_i
B_i
C_j
observer_opportunity_schedule
opportunities_granted
attention_arm
served_fraction
deadline_misses
queue_length
```

### 7.1.1. Mapeamento evento → atualização

A forma funcional acima é canônica. O seguinte mapeamento de evento é uma
operacionalização experimental auxiliar necessária para executá-la:

```text
cada demanda concluída validamente -> exatamente uma atualização basal
demanda não concluída/expirada      -> nenhuma atualização basal
```

Status:

```text
BASAL_UPDATE_FUNCTIONAL_FORM = FROZEN_CANONICAL_DISCRETE
COMPLETION_TO_UPDATE_MAPPING = FROZEN_AUXILIARY_EXPERIMENTAL_OPERATIONALIZATION
```

Se mais de uma demanda for concluída no mesmo ciclo lógico, as atualizações são
executadas sequencialmente na ordem FIFO de conclusão, cada uma lendo o estado
resultante da atualização imediatamente anterior.

### 7.1.2. Preservação do domínio de p

A implementação não pode usar `clamp`, saturação artificial ou correção pós-hoc para
manter `p` em `[0,1]`, pois isso acrescentaria uma não linearidade não pertencente à
regra basal.

Antes do run deve ser certificado, para todo estado admissível:

\[
\boxed{
0 < \eta_i^{(0)}(p)\le 1.
}
\]

Assim, cada atualização é uma combinação convexa entre `p_pre` e `p_alvo` e preserva
automaticamente:

\[
0\le p_i\le1.
\]

O critério numérico que garante essa condição permanece a congelar prospectivamente.

Status:

```text
BASAL_ETA0_BOUND_PRESERVATION = REQUIRED_BEFORE_RUN
POST_HOC_CLAMPING = FORBIDDEN
```

### 7.1.3. Ausência explícita de atenção na regra

A atualização executada é somente:

```text
eta0 = omega_i / (1 + iota_obs_i + kappa*EH(p_pre))
delta_p = eta0 * (p_alvo - p_pre)
p_post = p_pre + delta_p
```

Nunca:

```text
delta_p = A_i * eta0 * (p_alvo - p_pre)
```

Portanto:

```text
NO_ATTENTION_IN_OBSERVER_RULE = SATISFIED_BY_CONSTRUCTION
```

Isso, isoladamente, ainda não autoriza interpretação científica de A1a.


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

---

## 7.2. ANBC0 — classificação analítica da construção congelada

Defina para cada demanda elegível `j`:

\[
S_{ij}=
\begin{cases}
1,&\text{se a cadeia observação-processamento-atualização termina validamente;}\\
0,&\text{caso contrário.}
\end{cases}
\]

Pela própria definição de atenção:

\[
\boxed{
A_i
=
\frac{1}{D_i}\sum_{j=1}^{D_i}S_{ij}.
}
\]

A contribuição basal potencial de uma demanda, condicionada ao mesmo estado basal, é:

\[
G_i(p,x)=\eta_i^{(0)}(p)\,x,
\qquad
x=p_{\text{alvo}}-p.
\]

Como a construção congelada determina:

```text
S_ij = 1 -> executa exatamente G_i
S_ij = 0 -> executa zero
```

segue:

\[
\boxed{
\Delta p_{ij}
=
S_{ij}\,G_i(p,x).
}
\]

`G_i` não lê atenção, braço, `B_i`, `C_j` ou o schedule. Esses elementos determinam
apenas se `S_{ij}=1` ou `0` e, portanto, o valor observado de `A_i`.

Para repetições comparáveis no mesmo estado basal:

\[
E[\Delta p\mid p,x,A_i]
=
A_i\,\eta_i^{(0)}(p)\,x.
\]

Logo, a taxa efetiva construída satisfaz:

\[
\boxed{
\eta_i(A,p)=A_i\,\eta_i^{(0)}(p)
}
\]

não porque A1a a descobriu, mas porque o mecanismo executável é exatamente uma
seleção `S` entre **uma atualização basal fixa** e **zero atualização**.

Essa construção corresponde ao padrão suficiente `NC1_DERIVATIONAL_PATTERN` dos
§§52–54 da definição de atenção.

Portanto:

```text
A1A_OBSERVER_MICRODYNAMIC =
    FROZEN_CANONICAL_DISCRETE_WITH_AUXILIARY_COMPLETION_MAPPING

ANBC0 =
    FAIL_DERIVATIONAL

ANBC0.NC1_DERIVATIONAL_PATTERN =
    PRESENT

A1a =
    MECHANISM_DEMONSTRATION_ONLY [C1]

ASEP0_CONFIRMATORY =
    NOT_AUTHORIZED
```

### 7.2.1. Interpretação correta de FAIL_DERIVATIONAL

`FAIL_DERIVATIONAL`:

```text
não refuta H-A1S
não refuta a HUMH
não invalida A_i=U_i/D_i
não invalida o instrumento de B_i/C_j/oportunidades
não é bug de código
```

Ele significa somente:

> esta implementação não pode ser usada como confirmação independente da
> separabilidade multiplicativa, porque a relação já decorre da microdinâmica
> congelada.

Desvios numéricos de `eta_hat/A` observados nesta implementação não podem ser
reinterpretados automaticamente como refutação de H-A1S. Antes devem ser tratados
como possível efeito de estimação, discretização, estratificação, fila, janela ou
erro de implementação, pois a relação local por demanda já foi construída.

### 7.2.2. Proibição de resgate

É proibido trocar a microdinâmica por outra apenas para obter:

```text
ANBC0 = PASS_DISCRIMINATIVE
```

A classificação derivacional é aceita como resultado da auditoria prospectiva.

Se futuramente for desejado um teste independente de H-A1S, ele deverá usar outro
desenho experimental cuja ligação entre atenção medida e atualização não torne
`\eta=A\eta_0` uma identidade do mecanismo.

### 7.2.3. Consequência para A1b

A1b não é automaticamente cancelado.

Ele poderá continuar apenas se demonstrar conteúdo próprio:

```text
mesmo A_bar entre condições
D_A diferente segundo regra congelada
outcome coletivo primário congelado
efeito não reduzível à identidade local de A1a
Gates independentes de integridade/poder
```

A auditoria desse conteúdo próprio passa a ser o próximo bloqueio conceitual antes do
congelamento final dos números.


# 8. A0 — ATTENTION MEASUREMENT CONTRACT

A0 não é teste da teoria.

A0 congela e verifica o instrumento:

```text
D_i
U_i
W
L_A
A_i=U_i/D_i
observer_buffer_capacity = B_i
required_work = C_j
observer_opportunity_schedule = P_i_obs
contadores
deadline
regras de descarte
ABENCH0
p_alvo
eta_hat
elegibilidade de eta_hat
independência CANAL_A/CANAL_ETA
ausência de atenção na regra do observador
ANBC0
```

A0 bem-sucedido significa apenas:

`ATTENTION_MEASUREMENT_CONTRACT_VALID`

Não significa suporte à HUMH.

---

# 9. ABENCH0 — benchmark cego de instrumentação

Se `L_A=1` não for tecnicamente adequado, um novo benchmark cego selecionará `L_A`.

Antes de executar ABENCH0, devem ser congelados:

```text
L_grid
observer_buffer_capacity_rule e valores/distribuição já congelados
required_work_rule e faixa/distribuição já congelados
regras candidatas de alocação de oportunidades exclusivamente instrumentais
faixa admissível de A para evitar saturação
contraste instrumental mínimo
regra determinística de desempate
```

ABENCH0 pode observar apenas:

```text
D_i
U_i
A_i
latência técnica
deadline_misses
queue/service timing
runtime metadata
hardwareConcurrency
```

É proibido observar ou exportar:

```text
eta_hat
p_i(t)
EH
consenso
dispersão de crença
qualquer outcome de A1a/A1b
```

Se nenhum `L_A` satisfizer a regra congelada:

```text
ABENCH0 = FAIL
SCIENTIFIC_RUN_NOT_AUTHORIZED
```

---

# 10. H-A1S — hipótese científica de A1a

Hipótese canônica:

\[
\boxed{
\eta_i(A,p)=A_i\,\eta_i^{(0)}(p)
}
\]

com

\[
\eta_i^{(0)}(p)=
\frac{\omega_i}
{1+\iota_{obs,i}+\kappa EH(p)}.
\]

Predição de razão, para o mesmo observador/estado basal:

\[
\boxed{
\frac{\eta_i(A_2,p)}
{\eta_i(A_1,p)}
=
\frac{A_{i,2}}
{A_{i,1}}
}
\]

Predição normalizada:

\[
\boxed{
\frac{\eta_i(A,p)}{A_i}
=
\eta_i^{(0)}(p).
}
\]

A1a não testa que HIGH executa mais updates que LOW. Isso é apenas manipulation check.

---


# 10.1. Estatuto teórico de H-A1S — teoria-base, extensão prospectiva e alternativas

A v2.0.0 separa explicitamente três níveis que não podem ser confundidos.

## 10.1.1. Teoria-base

A teoria-base fornece:

\[
\eta_i^{(0)}(p)
=
\frac{\omega_i}
{1+\iota_{obs,i}+\kappa EH(p)}
\]

Nesse nível:

```text
omega_i      = ritmo/propriedade basal do observador
iota_obs_i   = resistência basal do observador à atualização
kappa*EH(p)  = resistência associada ao estado de ordenação
```

A teoria-base não contém, por si só, o fator `A_i` multiplicando o numerador.

## 10.1.2. H-A1S é extensão prospectiva

A definição de atenção introduz prospectivamente:

\[
\boxed{
\eta_i(A,p)
=
A_i\,
\frac{\omega_i}
{1+\iota_{obs,i}+\kappa EH(p)}
}
\]

como hipótese mecanística falsificável.

Portanto:

```text
H-A1S != consequência já deduzida da teoria-base
H-A1S = extensão prospectiva a ser confrontada experimentalmente
```

A v2.0.0 não cria nem utiliza uma variável teórica `omega_eff`.
A expressão `A_i*omega_i` é apenas a forma algébrica postulada por H-A1S.

## 10.1.3. Pareamento do mesmo observador

No contraste A1a, o mesmo observador mantém invariantes seus parâmetros basais:

```text
omega_i
iota_obs_i
demais parâmetros estruturais do observador
```

A intervenção planejada atua no instrumento de atenção:

```text
P_i_obs -> A_i
```

A operacionalização principal não redefine `iota_obs_i` em função do braço.
Manipular simultaneamente `A_i` e `iota_obs_i` seria uma segunda intervenção.

## 10.1.4. Formas alternativas M_alt

A1a deve permanecer capaz de distinguir H-A1S de alternativas nas quais a atenção
não atua como fator multiplicativo separável.

Exemplos de `M_alt`:

### Resistência aditiva dependente de atenção

\[
\eta_i(A,p)
=
\frac{\omega_i}
{1+\iota_{obs,i}+h(A_i)+\kappa EH(p)}.
\]

### Interação atenção × resistência

\[
\eta_i(A,p)
=
\frac{A_i\omega_i}
{1+\iota_{obs,i}+\phi(A_i,\iota_{obs,i})+\kappa EH(p)}.
\]

### Outra forma não separável

\[
\eta_i(A,p)=F(A_i,p,\omega_i,\iota_{obs,i},EH).
\]

Essas formas:

```text
não são proibidas por ANBC0
não são tratadas como bug do instrumento
não devem ser removidas para “limpar” o experimento
```

Se emergirem da dinâmica congelada e produzirem desvios materiais de H-A1S,
constituem exatamente o tipo de alternativa que A1a deve conseguir detectar.

## 10.1.5. Papel limitado de ANBC0

ANBC0 não escolhe entre H-A1S e `M_alt`.

Ele verifica apenas se a implementação tornou H-A1S inevitável antes da observação:

```text
H-A1S inevitável por construção
    -> FAIL_DERIVATIONAL
    -> A1a não é teste independente

H-A1S não inevitável por construção
    -> PASS_DISCRIMINATIVE
    -> A1a pode confrontar H-A1S com M_alt

estatuto não resolvido
    -> INCONCLUSIVE_ANALYTIC
```

Uma dependência emergente de resistência em relação ao recurso, por exemplo
`h(A)` ou `phi(A,iota_obs)`, não é automaticamente falha de ANBC0.
Ela pertence a `M_alt`, salvo se tiver sido implementada de modo a tornar
matematicamente inevitável a própria relação específica de H-A1S.

## 10.1.6. Cadeia conceitual congelada

```text
TEORIA-BASE
  eta0 = omega / (1 + iota_obs + kappa*EH)

EXTENSÃO PROSPECTIVA H-A1S
  eta(A,p) = A * eta0(p)

HIPÓTESES RIVAIS M_alt
  atenção como resistência aditiva
  interação A × iota_obs
  outras formas não separáveis

A1a
  confrontar H-A1S com M_alt sem hard-code da forma H-A1S
```

# 11. Papel de EH em A1a

`EH` não redefine atenção.

Os estratos de estado existem apenas no CANAL_ETA para comparar condições em regimes de estado prospectivamente definidos.

A teoria **não** exige:

```text
A_i(EH_LOW) = A_i(EH_MID) = A_i(EH_HIGH)
```

e a v2.0.0 não cria nenhuma dessas variáveis.

A previsão correta é relativa:

\[
\frac{\eta(A_2,EH)}
{\eta(A_1,EH)}
=
\frac{A_2}{A_1}
\]

em cada regime de estado no qual `eta_hat` seja identificável.

Se um estrato não contiver informação dinâmica suficiente, isso é problema de identificação de `eta_hat` e pertence a `AETA0`; não gera um Gate novo sobre atenção.

---

# 12. Estimando primário de A1a

Para cada observador `i`, estrato de estado `s` e par de braços prospectivamente definido `a,b`, formar somente depois dos dois canais:

\[
q_{i,s,a}=
\frac{\widehat\eta_{i,s,a}}
{A_{i,a}}
\]

e o contraste estatístico:

\[
\boxed{
C_{i,s}^{a,b}
=
\log q_{i,s,a}
-
\log q_{i,s,b}
}
\]

Este contraste **não é nova variável teórica**. É apenas operacionalização estatística da predição canônica `eta/A = invariável entre braços`.

Sob separabilidade:

\[
C_{i,s}^{a,b}\approx0.
\]

A lista de pares de braços e estratos primários deve ser fechada antes da coleta.

---

# 13. ASEP0 — decisão primária de A1a

> **DISPOSIÇÃO ATUAL DA v2.0.0:** `ANBC0=FAIL_DERIVATIONAL`. Portanto, a lógica
> confirmatória descrita nesta seção permanece documentada como contrato geral da
> hipótese, mas **não está autorizada nesta implementação**. Nenhum resultado desta
> construção pode receber `ATTENTION_MULTIPLICATIVE_SEPARABILITY_COMPATIBLE [C1]`
> ou `...REFUTED [C1]`; o máximo permitido para A1a é
> `MECHANISM_DEMONSTRATION_ONLY [C1]`.


A definição exige distinguir prospectivamente:

```text
M_sep = H-A1S: atenção multiplicativa separável
M_alt = resistência aditiva dependente de atenção, interação A×iota_obs,
        ou outra forma não separável prospectivamente admissível
```

A v2.0.0 fixa a forma da decisão, mas **não escolhe ainda a margem numérica**.

Parâmetros a congelar na versão run-ready:

```text
Delta_sep
alpha_family
método de controle da família de contrastes
procedimento de intervalo
lista fechada de contrastes primários
```

Regras finais obrigatórias:

### Compatível

Todos os contrastes primários identificáveis devem satisfazer o critério de equivalência congelado, com todos os Gates pré-requisitos em PASS:

```text
ATTENTION_MULTIPLICATIVE_SEPARABILITY_COMPATIBLE [C1]
```

### Refutado

Violação material prospectivamente definida em pelo menos um contraste primário, com identificação/potência/Gates adequados:

```text
ATTENTION_MULTIPLICATIVE_SEPARABILITY_REFUTED [C1]
```

### Inconclusivo

Falha de benchmark, manipulação, isolamento, identificação, competência, integridade ou potência:

```text
INCONCLUSIVE_*
```

Nunca converter insuficiência de dados em refutação.

---

# 14. ANBC0 — estatuto discriminativo do teste

ANBC0 não é hipótese sobre a HUMH e **não exige que `eta/A` possa variar**.

Ele pergunta somente:

> dadas a microdinâmica basal e a operacionalização experimental congeladas,
> H-A1S poderia ser contrariada pelo simulador ou é uma consequência matemática
> inevitável da própria construção?

Classificações:

```text
PASS_DISCRIMINATIVE
FAIL_DERIVATIONAL
INCONCLUSIVE_ANALYTIC
```

`PASS_DISCRIMINATIVE`: H-A1S não é implicada necessariamente.

`FAIL_DERIVATIONAL`: H-A1S decorre necessariamente das regras implementadas.
Isso não refuta H-A1S nem a HUMH. Apenas impede interpretar A1a como teste
computacional independente:

```text
A1a = MECHANISM_DEMONSTRATION_ONLY [C1]
ASEP0_CONFIRMATORY = NOT_AUTHORIZED
```

`INCONCLUSIVE_ANALYTIC`: ainda não foi possível determinar o estatuto.

ANBC0 não deve eliminar alternativas científicas para tornar o desenho “mais limpo”.
Em particular, uma forma emergente `iota_obs(A)` ou `h(A)` pertence a `M_alt` e
deve permanecer detectável por A1a. Ela só entra no escopo de ANBC0 se a forma
implementada tornar matematicamente inevitável a própria relação específica de H-A1S.

É proibido escolher ou trocar a microdinâmica apenas para obter
`PASS_DISCRIMINATIVE`.

O padrão `y=S*G`, quando suas premissas matemáticas forem satisfeitas, continua
sendo apenas um diagnóstico suficiente de caso derivacional. Ele não significa
que a teoria exija variabilidade de `eta/A`.

Status atual:

```text
ATTENTION_INSTRUMENT = FROZEN_OPPORTUNITY_ALLOCATION
A1A_OBSERVER_MICRODYNAMIC = FROZEN_CANONICAL_DISCRETE_WITH_AUXILIARY_COMPLETION_MAPPING
ANBC0 = FAIL_DERIVATIONAL
```

---
# 15. ACOMP0 — competência adversarial

Antes do run científico, o pipeline deve demonstrar em harness sintético que detecta:

1. uma condição separável conhecida;
2. pelo menos uma violação não separável conhecida;
3. a direção correta do contraste;
4. a competência mínima prospectivamente congelada.

O harness adversarial não pode compartilhar a regra geradora do outcome real.

Se a competência mínima não for atingida:

```text
ACOMP0 = FAIL
ASEP0 = INCONCLUSIVE_PIPELINE_COMPETENCE
```

---

# 16. A1b — ATTENTION DISTRIBUTION EFFECT

A1b usa exclusivamente as variáveis teóricas:

\[
\bar A
\quad\text{e}\quad
D_A.
\]

Pergunta científica:

> mantendo \(\bar A\) constante dentro da margem prospectiva, alterar \(D_A\) modifica a dinâmica coletiva?

Desenho conceitual:

```text
UNIFORM:
  A_i aproximadamente semelhante entre observadores
  D_A menor

HETEROGENEOUS:
  distribuição de A_i mais dispersa
  D_A maior
```

Restrições:

- `D_i` deve ser idêntico por observador entre braços pareados;
- somente a capacidade de atender a demanda é redistribuída;
- nenhuma realocação pode responder a `EH`, crença, dívida, sucesso ou falha durante a trajetória;
- regra de alocação exógena e congelada;
- `A_bar` não pode ser “corrigido” depois olhando o outcome coletivo.

A1b não é consequência automática de H-A1S. Entretanto, qualquer outcome coletivo candidato deve primeiro passar por auditoria derivacional dentro de `ADIST0`, para excluir efeito que seja invariância ou consequência matemática automática da construção local.

---

# 17. Outcome primário de A1b — candidato canônico e auditoria estrutural

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

# 18. Gates — lista fechada

A lista de Gates científicos/integridade da v2.0.0 é **exatamente** a estrutura mínima da definição:

```text
AGOV0   — governança/hashes/KREF0/traceability
AMEAS0  — contrato D/U/W/L_A e contadores
ABENCH0 — benchmark cego de instrumentação/deadline
AMAN0   — manipulation check de A
AISO0   — isolamento estrutural
AETA0   — identificação independente de eta_hat
ANBC0   — separabilidade não garantida por construção
ACOMP0  — competência para detectar não-separabilidade
ASEP0   — teste primário H-A1S
ADIST0  — teste A1b, se autorizado
AINT0   — integridade/RNG/checkpoint/reprodutibilidade
```

Não existem Gates científicos adicionais nesta versão.

---

# 19. Subchecks permitidos — sem criar nova teoria

Verificações úteis da série v1.0.x podem ser preservadas somente como subchecks:

```text
AGOV0
  .REFERENT_HASHES
  .NO_ATTENTION_IN_OBSERVER_RULE
  .TRACEABILITY_MANIFEST_COMPLETE

AMEAS0
  .NO_DOUBLE_COUNTING
  .D_IDENTITY_PAIRED_ARMS
  .DEADLINE_ACCOUNTING
  .RIGHT_EDGE_ACCOUNTING

AETA0
  .ETA_FINITE_AND_IDENTIFIABLE
  .TRAJECTORY_ONLY_DEPENDENCY_AUDIT
  .PERMUTATION_INVARIANCE_TO_A_COUNTERS
  .SYNTHETIC_SLOPE_RECOVERY
  .QUEUE_END_TO_END_RECOVERY

ANBC0
  .ANALYTIC_NONCONSTRUCTION
  .STATIONARY_WITNESS

AISO0
  .SERVICE_INVARIANCE
  .PROPAGATION_INVARIANCE
  .TOPOLOGY_INVARIANCE
  .EXOGENOUS_DEMAND_INVARIANCE

ADIST0
  .DERIVATIONAL_CONTENT_AUDIT
  .ATTENTION_TO_OBSERVER_ASSIGNMENT_INDEPENDENCE
  .GLOBAL_OPPORTUNITY_MASS_MATCHED_PER_CYCLE
  .LOGICAL_CYCLE_SNAPSHOT_INVARIANCE

AINT0
  .CRN_IDENTITY
  .RNG_LABEL_AUDIT
  .CHECKPOINT_RESUME_EQUIVALENCE
  .NO_RIGHT_CENSORING
  .DEMAND_CHECKSUMS
```

Esses nomes não podem ser usados para acrescentar condição científica não contida no Gate pai.

Itens explicitamente removidos como Gates:

```text
AEXP0
ACSUP0
ASTRAT0
AETA1
AETA2
ANBC1
ACRN0
ACRNB0
ACKPT0
ARULE0
```

Quando úteis, suas verificações técnicas são absorvidas pelos Gates canônicos acima.

---

# 20. AMAN0 — manipulation check

AMAN0 verifica apenas que os instrumentos `P_i_obs` geraram níveis de `A_i` suficientemente distintos segundo regra congelada.

Isso não conta como evidência de H-A1S.

Parâmetros ainda a congelar:

```text
número de braços
alvos/faixas instrumentais de A
contraste mínimo entre braços
regra para saturação em 0/1
```

É proibido escolher ou reajustar esses valores usando `eta_hat`, `EH` ou outcome coletivo.

---

# 21. AISO0 — isolamento

Entre braços pareados, manter invariantes, dentro de tolerâncias técnicas pré-fixadas:

```text
CPU global
manutenção
serviço
propagação
R_eff*
topologia
microdinâmica estrutural
D_i
conteúdo observacional
RNG exógeno
```

Somente `P_i_obs` varia.

Falha:

```text
INCONCLUSIVE_TECHNICAL_OR_ISOLATION
```

---

# 22. AETA0 — identificação de eta_hat

AETA0 exige cumulativamente:

1. informação dinâmica suficiente;
2. `eta_hat` finito nos estratos primários requeridos;
3. módulo ETA sem dependência de contadores/arm/alocação de oportunidades/capacidade de processamento;
4. permutar `U/D/A` mantendo trajetória fixa não altera `eta_hat`;
5. trajetória sintética de inclinação conhecida é recuperada corretamente.

Os seguintes parâmetros devem ser congelados antes do run:

```text
delta_drive
min_steps
min_sum_x2
estratos de estado
regra de passos elegíveis
```

Insuficiência em qualquer estrato primário produz categoria inconclusiva de identificação; não cria hipótese sobre `A_i`.


## 22.1. Harness técnico AETA0 — especificado, não executado

Antes de qualquer trajetória científica, o módulo `CANAL_ETA` deve passar três testes independentes de A1a:

```text
SYNTHETIC_SLOPE_RECOVERY
PERMUTATION_INVARIANCE_TO_A_COUNTERS
TRAJECTORY_SENSITIVITY
```

No primeiro, usar trajetória sintética de forma:

\[
y_t=\beta x_t+\epsilon_t
\]

com `beta` conhecido somente pelo harness. Os números do harness são `IMPLEMENTATION_ONLY` e não podem ser reutilizados para margem, poder, braços ou outcome científico.

No segundo, manter `p(t)` e `p_alvo(t)` bitwise fixos e permutar/substituir `U,D,A,arm,observer_opportunity_schedule,observer_buffer_capacity`; `eta_hat` deve permanecer bitwise idêntico.

No terceiro, manter os contadores fixos e alterar somente a trajetória sintética; `eta_hat` deve responder à inclinação imposta.

Status nesta v2.0.0:

```text
AETA0_HARNESS = SPECIFIED_NOT_EXECUTED
```

---

# 23. AINT0 — integridade

AINT0 cobre:

- seeds novas para a coleta v2;
- CRN nas condições pareadas;
- identidade de demanda;
- checksums;
- reprodutibilidade;
- checkpoint/resume sem alteração de resultado;
- ausência de top-up pós-outcome;
- ausência de censura direita não prevista;
- registro da versão exata da spec e implementação.

---

# 24. Novas seeds obrigatórias

Todo run científico v2 deve usar seeds nunca utilizadas na série v1.0.x.

As seeds confirmatórias não podem ser abertas em piloto.

Benchmarks técnicos e adversariais usam namespaces RNG separados da coleta científica.

---

# 25. Unidade inferencial

A unidade inferencial final ainda precisa ser congelada na versão run-ready, coerente com o pareamento por replicação/observador e sem pseudo-replicação.

A escolha deve ser feita antes de nova coleta e documentada como operacionalização estatística, não como variável teórica.

---

# 26. Itens de desenho e números ainda NÃO congelados

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

# 28. Regra automática de rastreabilidade para o código

A futura implementação deve carregar um manifest embutido contendo, para cada entidade:

```text
id
kind
status
canonical_refs:
  - artifact_id
    sha256
    section
    clause_or_statement
scientific_role
inputs
outputs
parent_gate
```

O manifesto deve manter também um registro fechado dos artefatos canônicos e seus hashes.

Build/run científico deve falhar se:

```text
scientific_role != IMPLEMENTATION_ONLY
AND canonical_refs estiver vazio
```

ou se qualquer `canonical_ref.sha256` divergir do hash registrado para o respectivo `artifact_id`, ou se existir Gate raiz não pertencente à lista fechada do §18.

A unidade de rastreabilidade, portanto, não é “seção N” isoladamente, mas:

```text
entidade científica
→ artifact_id
→ SHA-256
→ seção/cláusula
→ operacionalização
```


---


## 28.1. Fechamento do manifesto de rastreabilidade

O manifesto `HUMH_A0_A1_Traceabilidade_v2.0.0.json` representa mecanicamente,
além das variáveis, hipóteses e Gates:

```text
M_alt
    hipótese rival formal de H-A1S

ANBC0.NC1_DERIVATIONAL_PATTERN
    subcheck derivacional de ANBC0

result_logic
    mapeamento verificável entre condições/Gates e disposição final

scientific_sequence
    A0 -> A1a -> A1b; A2 não autorizado
```

O padrão histórico em que um identificador, como `ACSUP0`, aparece simultaneamente
em `retired_as_root_gates` e `forbidden_scientific_entities` é permitido pelo
validador: significa apenas que o Gate foi aposentado e também não pode reaparecer
como entidade científica.

Esses objetos são de governança e rastreabilidade. Eles não alteram H-A1S,
`M_alt`, os estimandos, os Gates ou qualquer critério científico.

# 29. Critérios de conclusão

## A0

Pode concluir somente:

```text
ATTENTION_MEASUREMENT_CONTRACT_VALID
ATTENTION_MEASUREMENT_CONTRACT_INVALID
```

Sem status de suporte teórico.

## A1a

Na construção corrente da v2.0.0:

```text
ANBC0 = FAIL_DERIVATIONAL
A1a = MECHANISM_DEMONSTRATION_ONLY [C1]
ASEP0_CONFIRMATORY = NOT_AUTHORIZED
```

As categorias `...COMPATIBLE [C1]` e `...REFUTED [C1]` pertencem ao contrato geral de
H-A1S, mas não podem ser emitidas por esta implementação.

## A1b

Estado corrente:

```text
PRIMARY_OUTCOME_CANDIDATE = STATE_DIVERGENCE_D
ADIST0.DERIVATIONAL_CONTENT_AUDIT_STRUCTURAL = CONDITIONAL_DISCRIMINATIVE
ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = PENDING_FROZEN_NUMERICS_AND_A1B_ASSIGNMENT_RULE
ADIST0_CONFIRMATORY = NOT_AUTHORIZED
```

Somente se a auditoria final classificar o candidato como discriminativo e os demais
critérios forem congelados poderão ser usadas as categorias gerais de resultado de A1b.

## A2

```text
NOT AUTHORIZED / NOT TESTED
```

---

# 30. Regra final

A v2.0.0 não tenta salvar, ajustar ou reinterpretar a série v1.0.x.

Ela restabelece a relação:

\[
\boxed{
\text{definição canônica}
\rightarrow
\text{variável/hipótese}
\rightarrow
\text{operacionalização}
\rightarrow
\text{Gate}
\rightarrow
\text{código}
\rightarrow
\text{resultado}
}
\]

e proíbe a direção inversa:

\[
\boxed{
\text{resultado observado}
\not\rightarrow
\text{nova variável/Gate/hipótese ad hoc}.
}
\]

**Estado final desta versão:**

```text
TRACEABILITY_RESET = FROZEN
SCIENTIFIC_MODEL = CANONICAL_A0_A1_ONLY
SCIENTIFIC_RUN_NOT_AUTHORIZED
NEXT = FREEZE_BASAL_NUMERICS_AND_A1B_ASSIGNMENT_THEN_COMPLETE_ADIST0_DERIVATIONAL_AUDIT
```
