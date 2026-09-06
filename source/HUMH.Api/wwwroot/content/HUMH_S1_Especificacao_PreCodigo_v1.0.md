# HUMH — Especificação Pré-Código de S1
## S1 — Fila Central de Manutenção, CAL/VAL e Gate K0

**Identidade do objeto:** `HUMH_S1_SPEC_1.0`  
**Status:** PROPOSTA PRÉ-CÓDIGO — pronta para revisão e posterior congelamento  
**Classe epistemológica:** C1  
**Plataforma prevista:** HTML + JavaScript + Web Workers  
**Referente teórico:** `teoria.md`  
**SHA-256 da teoria:** `5c8258e1aae5f735d5730ddc93f0f816825c8ec2b23f126aa0c969d10a0a5505`  
**Núcleo relacionado:** `HUMH_Nucleo_1.9A.md`  
**SHA-256 do núcleo:** `dfdd673da080b4e1e4038f7a57c2608d48c947f77a1629b9094cfb18bd835991`  
**Programa relacionado:** `HUMH_Programa_N3_1.9B.md`  
**SHA-256 do programa:** `a9bfd724b7af7849711570798eb8134282fa93fe39093fbd7f4b637041f5a226`

> Esta especificação separa compromissos já presentes no programa N3 das escolhas novas necessárias para tornar S1 executável. As escolhas numéricas e microdinâmicas abaixo são **propostas novas**. Depois de aprovadas, o arquivo deverá ser hasheado e nenhuma delas poderá ser ajustada usando resultados confirmatórios de S1.

---

# 1. Objetivo de S1

S1 testa a invariância interna da lei escalar candidata:

\[
\boxed{
T_{dwell}
\approx
t_{trans}
+
K_{N3}
\frac{R_{eff}}{\gamma_{manut}}
}
\]

em um substrato C1 de **fila central de manutenção**.

O teste principal não é demonstrar que:

\[
R_{eff}/\gamma_{manut}
\]

possui dimensão temporal, nem obter \(K\approx1\).

O compromisso confirmatório é:

\[
\boxed{
K_{N3}
\text{ estimado em S1-CAL deve prever S1-VAL sem reajuste.}
}
\]

S1 não pode fornecer status acima de **COMPATÍVEL**, mas pode refutar a forma atual de N3T\(_K\) se Gate K0 falhar com precisão e Gates técnicos adequados.

---

# 2. Princípio de independência micro–macro

Nenhum agente e nenhuma regra do scheduler poderá consultar:

- EH;
- \(\bar p\);
- \(D\);
- \(R_{eff}\);
- \(\gamma_{manut}\);
- \(K_{N3}\);
- \(T_{dwell}\);
- \(t_{trans}\);
- idade global do atrator;
- rótulo global A/B;
- probabilidade de transição estimada;
- previsão HUMH.

Essas grandezas existem apenas no **harness de medição/análise**.

É proibido implementar regra do tipo:

```text
if backlog > threshold:
    switch_attractor()
```

ou qualquer equivalente funcional que leia uma variável global e force diretamente a transição.

---

# 3. Unidade de Manutenção — UM

Define-se:

\[
\boxed{
1\ UM
=
1\ obrigação de manutenção de um agente que expirou sem serviço.
}
\]

Cada obrigação é uma tarefa lógica unitária.

Características:

- uma tarefa requer exatamente **1 quantum de serviço**;
- o quantum é lógico, não milissegundos de CPU;
- uma tarefa atendida dentro do TTL não cria dívida;
- uma tarefa expirada acrescenta exatamente **1 UM** à dívida local do agente;
- UM não depende do estado A/B;
- UM não depende de EH;
- UM é idêntica em todas as células S1.

O tempo físico de execução do navegador é apenas diagnóstico e nunca entra em \(R_{eff}\), \(\gamma_{manut}\), \(K_{N3}\) ou Gate K0.

---

# 4. Microestado dos agentes

Número de agentes:

\[
\boxed{N=100}
\]

Cada agente \(i\) possui somente:

```text
s_i          ∈ {-1,+1}   estado binário atual
r_i          ∈ {-1,+1}   estado local de referência gravado ao fim da formação
d_i          ∈ {0,1,...} dívida de manutenção acumulada em UM
phase_i      ∈ {0,...,P-1} fase fixa de emissão de tarefa
```

O agente não conhece o sinal majoritário do coletivo.

Ao fim da formação:

```text
r_i = s_i
d_i = 0
```

Portanto \(r_i\) é memória **local**, não rótulo global A/B.

---

# 5. Formação do atrator inicial

A formação é padronizada e fica fora de \(T_{dwell}\).

## 5.1 Inicialização

No ciclo inicial:

\[
P(s_i=+1)=0{,}90.
\]

A seleção dos 90 agentes iniciais em \(+1\) é determinada pela seed.

## 5.2 Regra de formação

Enquanto a formação não terminar, manutenção fica desligada.

Em cada ciclo, cada agente:

1. amostra dois pares distintos, uniformemente;
2. recebe um sinal privado \(e_i\in\{-1,+1\}\);
3. o sinal privado satisfaz:

\[
P(e_i=+1)=q_{form}=0{,}55;
\]

4. atualiza \(s_i\) pela maioria dos três votos:

```text
peer_1, peer_2, e_i
```

5. com probabilidade:

\[
\mu_{form}=0{,}002
\]

substitui o resultado por um sinal aleatório \(\pm1\).

## 5.3 Critério de formação

A formação termina quando:

\[
EH\le0{,}10
\]

por:

\[
\boxed{h_{form}=5}
\]

ciclos consecutivos.

O sinal majoritário nesse momento é registrado **apenas pelo harness** como atrator inicial \(A\).

## 5.4 Falha de formação

Limite:

\[
\boxed{T_{form,max}=2000\ ciclos}
\]

Se não houver formação, a execução recebe:

```text
formation_failed = 1
```

e não é substituída por nova seed.

Se mais de 2% das execuções de qualquer célula apresentarem `formation_failed`, a célula falha no Gate técnico F0 e S1 fica **INCONCLUSIVO** até nova versão do protocolo.

---

# 6. Sistema central de manutenção

## 6.1 Periodicidade

Cada agente emite uma tarefa a cada:

\[
\boxed{P=20\ ciclos}
\]

As fases são balanceadas: cada uma das 20 fases possui exatamente 5 agentes.

A seed apenas permuta quais agentes pertencem a cada fase.

Logo, a demanda nominal é:

\[
\lambda_0
=
\frac{N}{P}
=
5\ UM/ciclo.
\]

## 6.2 Fila

- fila única;
- política FIFO;
- empate entre tarefas criadas no mesmo ciclo resolvido por prioridade pseudoaleatória derivada da seed;
- scheduler não consulta estado do agente;
- scheduler não consulta EH;
- scheduler não consulta dívida global.

## 6.3 TTL

Cada tarefa deve ser servida em até:

\[
\boxed{TTL=4\ ciclos}
\]

contados a partir do ciclo de emissão.

Se a tarefa não for servida dentro desse prazo:

```text
task.expired = 1
d_i = d_i + 1
```

e a tarefa é removida.

Tarefas atendidas não alteram \(d_i\).

Assim, \(d_i\) representa **custo acumulado não recuperado** durante o dwell atual.

## 6.4 Capacidade de serviço

A capacidade lógica por ciclo é:

\[
C
=
\rho_C\lambda_0.
\]

Capacidade fracionária é implementada por **token bucket determinístico**:

```text
tokens += C
while tokens >= 1 and queue not empty:
    serve 1 task
    tokens -= 1
```

O saldo fracionário é carregado entre ciclos.

---

# 7. Dívida local e plasticidade

Cada célula possui um limiar local:

\[
M.
\]

O agente permanece **travado** enquanto:

\[
d_i<M.
\]

Agentes travados mantêm \(s_i\).

Quando:

\[
d_i\ge M,
\]

o agente torna-se **plástico**.

Essa mudança depende exclusivamente da dívida local do próprio agente.

---

# 8. Dinâmica dos agentes plásticos

Em cada ciclo, um agente plástico:

1. amostra dois pares distintos;
2. forma três votos:

```text
s_j
s_k
-r_i
```

3. adota a maioria desses três votos;
4. com probabilidade:

\[
\boxed{\mu=0{,}01}
\]

substitui o resultado por um sinal aleatório \(\pm1\).

O voto \(-r_i\) representa fadiga local em relação ao estado que o próprio agente sustentava no início do dwell.

Essa regra:

- é simétrica sob troca \(+1\leftrightarrow-1\);
- não conhece A/B global;
- não consulta EH;
- não consulta backlog;
- não consulta tempo de permanência no atrator;
- não lê \(R_{eff}\) nem \(\gamma_{manut}\).

---

# 9. Variáveis macroscópicas somente para medição

O harness calcula:

\[
p(t)=\frac{\#\{s_i=+1\}}{N}
\]

e:

\[
EH(t)=1-|2p(t)-1|.
\]

Também registra:

\[
D_M(t)=\sum_i d_i
\]

como dívida lógica total, mas \(D_M\) não participa das regras dos agentes.

---

# 10. Definição de \(T_{dwell}\)

O relógio do dwell começa no primeiro ciclo após a formação.

Define-se o atrator oposto \(B\) apenas para análise:

```text
B = -A
```

A execução termina quando a proporção no sinal oposto satisfaz:

\[
p_B\ge0{,}95
\]

por:

\[
\boxed{h_{trans}=5}
\]

ciclos consecutivos.

Então:

\[
\boxed{
T_{dwell}
=
t_{B,end}-t_0
}
\]

em ciclos lógicos.

---

# 11. Definição de início e duração da transição

O atrator inicial é considerado abandonado quando:

\[
p_A<0{,}95
\]

por:

\[
\boxed{h_{exit}=5}
\]

ciclos consecutivos.

Esse ponto inicia uma **transição candidata**.

Se o sistema retornar a:

\[
p_A\ge0{,}95
\]

por 5 ciclos antes de atingir B, a candidata é cancelada.

A próxima saída sustentada cria nova candidata.

A transição válida é a candidata que termina em B.

Para cada execução:

\[
t_{trans,obs}
=
t_{B,end}-t_{exit}.
\]

Esse valor é registrado em CAL e VAL, mas **VAL não pode usá-lo para produzir a própria previsão**.

---

# 12. Operacionalização independente de \(\gamma_{manut}\)

Define-se:

\[
\boxed{
\gamma_{manut}
=
E[\text{tarefas expiradas por ciclo}]
}
\]

em UM/ciclo.

Cada expiração adiciona exatamente 1 UM, portanto essa é a taxa de geração de dívida lógica.

## 12.1 Ensaio de \(\gamma\)

Para cada célula:

- dinâmica de estados é congelada;
- somente tarefas, TTL, fila e scheduler são executados;
- warm-up:

\[
500\ ciclos;
\]

- janela de medição:

\[
5000\ ciclos;
\]

- replicações independentes:

\[
\boxed{n_\gamma=32}
\]

- seeds em namespace separado `GAMMA`.

Estimador:

\[
\hat\gamma_j
=
\frac{1}{32}
\sum_r
\frac{N_{expired,r}}{5000}.
\]

Gate G0:

\[
\frac{SE(\hat\gamma_j)}{\hat\gamma_j}
\le0{,}05.
\]

Se \(\hat\gamma_j=0\) ou G0 falhar, a célula não entra no teste primário.

---

# 13. Operacionalização independente de \(R_{eff}\)

\(R_{eff}\) não é obtido de \(T_{dwell}\).

Ele é medido em **ensaio de pulso de dívida** separado.

## 13.1 Espaço máximo de dívida local

Cada agente possui \(M\) slots relevantes antes da plasticidade.

O total de slots é:

\[
Q=N M.
\]

## 13.2 Pulso

Partindo de snapshot recém-formado:

- estados permanecem inalterados;
- \(d_i=0\);
- são selecionados \(J\) slots de dívida entre os \(Q\) slots possíveis;
- cada slot selecionado adiciona 1 UM ao respectivo agente;
- seleção feita por permutação pseudoaleatória sem reposição dos \(Q\) slots.

Grid:

\[
\frac{J}{Q}
\in
\{
0,\ 0{,}10,\ 0{,}20,\ 0{,}30,\ 0{,}40,\ 0{,}50,\ 0{,}60,\ 0{,}70,\ 0{,}80,\ 0{,}90,\ 1{,}00
\}.
\]

## 13.3 Probe

Depois do pulso:

- nenhuma nova dívida pode ser criada;
- todas as tarefas futuras são tratadas como atendidas;
- estados continuam seguindo as regras normais de travado/plástico;
- duração:

\[
\boxed{H_{probe}=500\ ciclos}
\]

Perda do atrator ocorre se:

\[
p_A<0{,}95
\]

por 5 ciclos consecutivos.

## 13.4 Replicações

Por nível \(J\):

\[
\boxed{n_R=64}
\]

seeds em namespace `REFF`.

## 13.5 Estimador

A curva:

\[
P(\text{perda}\mid J)
\]

é estimada por **regressão isotônica monotônica**.

Define-se:

\[
\boxed{
R_{eff}
=
J_{50}
}
\]

onde \(J_{50}\) é o valor interpolado em que a probabilidade isotônica de perda atinge 0,50.

Unidade:

\[
UM.
\]

## 13.6 Gate R0

A célula é válida somente se:

\[
\hat P(\text{perda}\mid J=0)\le0{,}10
\]

e:

\[
\hat P(\text{perda}\mid J=Q)\ge0{,}80.
\]

Se o nível de 50% não estiver bracketed, \(R_{eff}\) é **INCONCLUSIVO** para a célula.

---

# 14. Famílias confirmatórias de parâmetros

Parâmetros fixos:

| Parâmetro | Valor |
|---|---:|
| \(N\) | 100 |
| \(P\) | 20 ciclos |
| \(\lambda_0\) | 5 UM/ciclo |
| TTL | 4 ciclos |
| \(q_{form}\) | 0,55 |
| \(\mu_{form}\) | 0,002 |
| \(\mu\) | 0,01 |
| \(h_{form}\) | 5 |
| \(h_{exit}\) | 5 |
| \(h_{trans}\) | 5 |
| \(T_{form,max}\) | 2.000 ciclos |
| \(T_{max}\) | 30.000 ciclos |
| \(H_{probe}\) | 500 ciclos |

Fatores confirmatórios:

\[
M\in\{2,3,4,6\}
\]

e:

\[
\rho_C
\in
\{0{,}72,\ 0{,}80,\ 0{,}88,\ 0{,}94\}.
\]

Logo:

\[
C
\in
\{3{,}6,\ 4{,}0,\ 4{,}4,\ 4{,}7\}
\ UM/ciclo.
\]

Total:

\[
\boxed{16\ células}
\]

Não haverá remoção posterior de níveis porque “não funcionaram”.

---

# 15. Divisão S1-CAL / S1-VAL

Ordenam-se:

```text
M index:      0,1,2,3  -> 2,3,4,6
rho_C index:  0,1,2,3  -> .72,.80,.88,.94
```

Regra congelada:

\[
\boxed{
CAL
\iff
(i+j)\bmod2=0
}
\]

e:

\[
\boxed{
VAL
\iff
(i+j)\bmod2=1.
}
\]

Matriz:

| \(M\) \(\backslash\) \(\rho_C\) | 0,72 | 0,80 | 0,88 | 0,94 |
|---:|:---:|:---:|:---:|:---:|
| 2 | CAL | VAL | CAL | VAL |
| 3 | VAL | CAL | VAL | CAL |
| 4 | CAL | VAL | CAL | VAL |
| 6 | VAL | CAL | VAL | CAL |

Assim há 8 células CAL e 8 células VAL.

VAL nunca participa da estimação de \(t_{trans}^*\) ou \(K_{N3}\).

---

# 16. Replicações de dwell

Para cada célula:

\[
\boxed{n_{dwell}=128}
\]

execuções independentes.

Namespaces distintos:

```text
DWELL_CAL
DWELL_VAL
```

Nenhuma execução é substituída após falha, censura ou formação malsucedida.

---

# 17. Seeds

Cada seed é derivada deterministicamente por:

```text
SHA256(
  "HUMH_S1_SPEC_1.0" +
  "|" + namespace +
  "|" + cell_id +
  "|" + replicate_id
)
```

São usados os primeiros 64 bits do digest como seed unsigned.

Namespaces obrigatoriamente distintos:

```text
FORMATION
GAMMA
REFF
DWELL_CAL
DWELL_VAL
BOOTSTRAP
AUDIT_TRACE
```

É proibido reutilizar seed de CAL em VAL ou gerar seeds adicionais para substituir resultados desfavoráveis.

---

# 18. Censura

A contagem inicia em \(t_0\), depois da formação.

Limite:

\[
\boxed{T_{max}=30\,000\ ciclos}
\]

Se B não for alcançado até esse ciclo:

```text
censored = 1
T_dwell = 30000
```

Trata-se de censura à direita.

## Gate C0

Uma célula é primariamente analisável somente se:

\[
\boxed{
f_{cens}\le0{,}10
}
\]

Se qualquer célula CAL necessária ou qualquer célula VAL necessária ultrapassar 10% de censura, Gate K0 não pode ser declarado PASS ou REFUTADO a partir dessa célula; o resultado global de S1 torna-se **INCONCLUSIVO**.

Não será ajustado modelo de sobrevivência pós-hoc para salvar células muito censuradas.

---

# 19. Estimativa de \(t_{trans}^*\)

\(t_{trans}^*\) é estimado **somente em CAL**.

Para cada célula CAL:

\[
\tilde t_{trans,j}
=
mediana(t_{trans,obs})
\]

entre execuções não censuradas.

O escalar S1 é:

\[
\boxed{
t_{trans}^*
=
mediana_j(\tilde t_{trans,j})
}
\]

com peso igual por célula, não por número de execuções.

Depois de calculado em CAL, esse valor é congelado antes de abrir os resultados de dwell de VAL.

VAL registra \(t_{trans,obs}\) apenas como diagnóstico.

---

# 20. Gate U de estabilidade de \(t_{trans}\)

Usa-se:

\[
\boxed{\epsilon_{trans}=0{,}10}.
\]

Bootstrap estratificado em CAL estima:

\[
SE(t_{trans}^*).
\]

Define-se:

\[
T_{maint,CAL}
=
mediana_{CAL}
(T_{dwell}-t_{trans,obs}).
\]

Gate U:

\[
\boxed{
\frac{SE(t_{trans}^*)}
{T_{maint,CAL}}
\le0{,}10
}
\]

Se Gate U falhar:

\[
\boxed{S1=\text{INCONCLUSIVO}}
\]

e K0 não é interpretado.

---

# 21. Estimador de \(K_{N3}\) em CAL

Para cada célula CAL válida:

\[
\tilde T_j
=
mediana(T_{dwell})
\]

e:

\[
K_j
=
\frac{
(\tilde T_j-t_{trans}^*)
\hat\gamma_j
}
{
\hat R_{eff,j}
}.
\]

Estimador primário:

\[
\boxed{
\hat K_{CAL}
=
mediana_j(K_j)
}
\]

com peso igual por célula.

Não há intercepto livre adicional.

Não há \(K\) específico por capacidade.

Não há \(K\) específico por \(M\).

---

# 22. Predição congelada de VAL

Antes de abrir o dwell de VAL, deverá ser produzido:

```text
s1_val_predictions.json
```

contendo para cada célula VAL:

- \(\hat R_{eff,j}\);
- \(\hat\gamma_j\);
- \(t_{trans}^*\);
- \(\hat K_{CAL}\);
- previsão:

\[
\boxed{
\hat T_{dwell,j}
=
t_{trans}^*
+
\hat K_{CAL}
\frac{
\hat R_{eff,j}
}
{
\hat\gamma_j
}
}
\]

- hash do manifesto;
- hash do código;
- hash desta especificação.

Esse arquivo é congelado antes da avaliação de VAL.

---

# 23. \(K_j\) observado em VAL

Depois de abrir VAL:

\[
K_j^{VAL}
=
\frac{
(\tilde T_j^{VAL}-t_{trans}^*)
\hat\gamma_j
}
{
\hat R_{eff,j}
}.
\]

Define-se:

\[
\Delta_j
=
\ln
\left(
\frac{
K_j^{VAL}
}
{
\hat K_{CAL}
}
\right).
\]

Margem interna proposta para K0:

\[
\boxed{
\delta_{K0}=10\%
}
\]

e no espaço log:

\[
m_{K0}
=
\ln(1{,}10).
\]

---

# 24. Bootstrap confirmatório

Número:

\[
\boxed{B=10\,000}
\]

replicações.

O bootstrap é hierárquico e reamostra:

1. runs de dwell dentro de cada célula;
2. replicações de \(\gamma\);
3. replicações do ensaio \(R_{eff}\);
4. runs de \(t_{trans}\) em CAL.

Em cada bootstrap são recalculados:

- \(R_{eff}\);
- \(\gamma\);
- \(t_{trans}^*\);
- \(K_j^{CAL}\);
- \(\hat K_{CAL}\);
- \(K_j^{VAL}\);
- \(\Delta_j\).

---

# 25. Gate K0

Define-se:

\[
Z
=
\max_{j\in VAL}
|\Delta_j|.
\]

## PASS — COMPATÍVEL em S1

Gate K0 passa se o limite superior simultâneo de 90% do bootstrap para \(Z\) satisfizer:

\[
\boxed{
U_{90}(Z)
\le
\ln(1{,}10)
}
\]

com Gates F0, G0, R0, C0 e U satisfeitos.

Conclusão:

\[
\boxed{
N3T_K
\text{ permanece COMPATÍVEL em S1.}
}
\]

## REFUTADO em S1

Gate K0 refuta a forma atual de N3T\(_K\) se, com todos os Gates técnicos satisfeitos, existir ao menos uma célula VAL cujo IC95% de \(\Delta_j\) esteja inteiramente fora de:

\[
[-\ln(1{,}10),+\ln(1{,}10)].
\]

Conclusão:

\[
\boxed{
N3T_K
\text{ é REFUTADA na forma atual e o programa para antes de S2.}
}
\]

## INCONCLUSIVO

Qualquer situação entre os dois critérios, ou falha de Gate técnico/precisão, é classificada:

\[
\boxed{\text{INCONCLUSIVO}}
\]

e não como PASS.

---

# 26. Controles diagnósticos não confirmatórios

## D1 — capacidade alta

\[
\rho_C=1{,}10
\]

para:

\[
M\in\{2,6\}.
\]

Objetivo: verificar se \(\gamma_{manut}\approx0\) produz dwell muito longo/censurado.

## D2 — ausência de mutação

\[
\mu=0
\]

na célula:

```text
M=3
rho_C=0.80
```

Objetivo: quantificar quanto a nucleação estocástica contribui à transição.

D1/D2 nunca podem substituir células confirmatórias nem ser usados para redefinir parâmetros.

---

# 27. Logs obrigatórios

## 27.1 `s1_manifest.json`

```text
spec_version
spec_sha256
theory_sha256
nucleus_sha256
program_sha256
code_sha256
browser_version
os
worker_count
all_fixed_parameters
all_cells
CAL_VAL_rule
seed_rule
T_max
bootstrap_B
Gate thresholds
timestamp_start
timestamp_end
```

## 27.2 `s1_gamma.csv`

```text
cell_id
split
seed
M
rho_C
C
warmup_cycles
measure_cycles
arrivals
served
expired
gamma_run
```

## 27.3 `s1_reff.csv`

```text
cell_id
split
seed
M
rho_C
J
J_over_Q
loss
loss_cycle
probe_cycles
```

Resumo adicional:

```text
s1_reff_summary.csv
```

com \(R_{eff}\), IC e Gates.

## 27.4 `s1_runs.csv`

```text
cell_id
split
seed
M
rho_C
C
formation_status
formation_cycles
A_sign
t0
exit_candidate_count
t_exit_valid
t_B_end
T_dwell
t_trans_obs
censored
max_queue
total_expired
final_total_debt
runtime_error
wall_ms
```

`wall_ms` é apenas diagnóstico.

## 27.5 `s1_cells.csv`

```text
cell_id
split
R_eff
R_eff_CI_low
R_eff_CI_high
gamma
gamma_SE
median_T_dwell
censor_fraction
median_t_trans_obs
K_cell
pred_T_dwell
relative_prediction_error
Gate_F0
Gate_G0
Gate_R0
Gate_C0
Gate_U
```

## 27.6 `s1_val_predictions.json`

Deve existir e ser hasheado **antes** da abertura de VAL.

## 27.7 `s1_audit_trace.csv.gz`

Traço completo apenas para:

\[
\boxed{4\ seeds\ pré-definidas/célula}
\]

em namespace `AUDIT_TRACE`.

```text
cell_id
seed
cycle
p
EH
queue_length
arrivals
served
expired
plastic_count
total_debt
mean_debt
max_debt
candidate_transition
```

Para os demais runs, o summary é suficiente porque seed + código + manifesto tornam a trajetória reproduzível.

---

# 28. Ordem de execução obrigatória

### Fase 0 — validação técnica

- checagem determinística das seeds;
- teste unitário de FIFO;
- teste unitário de TTL;
- teste unitário do token bucket;
- teste de simetria \(+1\leftrightarrow-1\);
- teste de que agentes/scheduler não leem EH.

### Fase 1 — macros independentes

Executar para todas as 16 células:

\[
R_{eff}
\]

e:

\[
\gamma_{manut}.
\]

### Fase 2 — CAL

Executar somente as 8 células CAL.

Estimar:

\[
t_{trans}^*
\]

e:

\[
\hat K_{CAL}.
\]

### Fase 3 — congelamento de previsão

Gerar e hashear:

```text
s1_val_predictions.json
```

### Fase 4 — VAL

Executar as 8 células VAL sem permitir alteração de parâmetros.

### Fase 5 — Gate K0

Calcular PASS / REFUTADO / INCONCLUSIVO.

---

# 29. Regras de parada

S1 para antes de VAL se:

- Gate G0 falhar de forma estrutural;
- Gate R0 falhar em células necessárias;
- Gate F0 falhar;
- Gate U falhar;
- número de células CAL válidas cair abaixo de 8.

Depois de VAL:

- Gate K0 REFUTADO → parar N3T\(_K\); não executar S2 como resgate;
- Gate K0 INCONCLUSIVO → não promover para S2 confirmatório;
- Gate K0 PASS → S1 fornece apenas **COMPATÍVEL**, e S2 pode ser iniciado segundo o programa N3.

---

# 30. Censura, falhas e exclusões técnicas

São exclusões técnicas legítimas somente:

- exceção de runtime;
- corrupção do arquivo de seed;
- violação detectada de determinismo;
- falha comprovada do Worker;
- arquivo de saída incompleto por interrupção externa.

Não são exclusões técnicas:

- dwell longo;
- transição “estranha”;
- \(K\) discrepante;
- \(R_{eff}\) baixo;
- \(\gamma\) inesperado;
- célula que piora Gate K0.

Nenhuma seed é substituída.

---

# 31. Proibições pós-resultado específicas de S1

Depois do hash desta especificação, é proibido:

- alterar \(M\);
- alterar \(\rho_C\);
- alterar TTL;
- alterar \(\mu\);
- alterar \(q_{form}\);
- mudar CAL/VAL;
- aumentar \(T_{max}\) para salvar célula confirmatória;
- trocar mediana por média;
- usar \(t_{trans}\) observado em VAL para melhorar a previsão de VAL;
- estimar \(K\) novamente incluindo VAL;
- criar \(K_M\), \(K_C\) ou \(K_{cell}\) como resgate;
- redefinir UM;
- redefinir \(R_{eff}\) usando dwell;
- redefinir \(\gamma_{manut}\) usando tempo até transição;
- remover células porque violam invariância;
- escolher outro critério de Gate K0 após abrir VAL.

Qualquer mudança exige:

```text
HUMH_S1_SPEC_1.1 ou superior
```

e a versão 1.0 permanece registrada.

---

# 32. O que esta especificação testa de fato

Se K0 passar:

\[
\boxed{
\text{uma mesma constante escalar K comprime a dinâmica de 16 condições S1}
}
\]

dentro da margem congelada e sem reajuste de VAL.

Isso é compatibilidade C1.

Se K0 falhar adequadamente:

\[
\boxed{
\text{a forma escalar atual de N3T_K falha já dentro de S1.}
}
\]

Isso encerra a rota confirmatória N3T\(_K\) atual antes de S2.

---

# 33. Questões que permanecem fora de S1

S1 não decide:

- se o mesmo \(K\) transporta para S2;
- se o mesmo \(K\) transporta para S3;
- se existe \(F(x)\) universal;
- se há suporte C2;
- se há suporte humano;
- se \(R/\gamma\) é uma lei universal.

Essas perguntas pertencem às etapas posteriores do programa.

---

# 34. Regra final antes do código

A ordem obrigatória é:

\[
\boxed{
\text{especificar}
\rightarrow
\text{revisar}
\rightarrow
\text{hash}
\rightarrow
\text{implementar}
\rightarrow
\text{testes unitários}
\rightarrow
\text{CAL}
\rightarrow
\text{hash das previsões VAL}
\rightarrow
\text{VAL}
}
\]

O código deverá implementar esta especificação; a especificação não será reescrita para acomodar o comportamento do código.
