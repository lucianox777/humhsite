# HUMH — Definição de Atenção Observacional Efetiva
## Especificação conceitual v1.0.0

**Identidade:** `HUMH_ATTENTION_DEFINITION_1.0.0`  
**Status:** PRONTA PARA CONGELAMENTO CONCEITUAL — A0/A1 COM IDENTIFICAÇÃO INDEPENDENTE DE η; A2 AINDA NÃO AUTORIZADO  
**Classe:** definição mecanística / extensão prospectiva da HUMH  
**Objeto:** atenção como variável do observador, contrato de mensuração e hipóteses falsificáveis de forma/distribuição  
**Regra histórica:** esta definição não reclassifica resultados anteriores da linha N3T-K  

**Nota de governança:** este arquivo mantém deliberadamente o número `v1.0.0`, porque nenhuma redação anterior desta definição foi congelada. Os SHAs anteriores `e13229d2cca6dd1306636a0951495b91a5d29183bbbbb982b4250c772966e18a` e `20e5b5606656492041d76b4930449d1ca7765147a22358091116d56f1f046997` ficam **SUPERSEDED_PRE_FREEZE** e não devem ser usados como referentes congelados.

---

# 1. Linhagem normativa canônica

Referentes canônicos:

```text
theory_sha256  = 3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b
nucleus_sha256 = baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b
program_sha256 = a9bfd724b7af7849711570798eb8134282fa93fe39093fbd7f4b637041f5a226
```

# 2. Antecedente experimental imediato

A linha de atenção é aberta após o resultado confirmatório local:

```text
S2RK0 spec        = HUMH_S2RK0_SPEC_1.0.1
spec_sha256       = 6a120801b7801139a55e6c464a8adeb0877ffeba4f8e9c2cbb46a690c2870169
contract_sha256   = 6f489ed44a977e42dd1ef31bd66955b6179e5d0988aac45699209149ef578f4b
implementation   = HUMH_S2RK0_HTML_1.0.1-HF2_COMBOKEYS
HTML_sha256       = 9ffc5ad9907ef3ef13aedb72e88e74631c86059dc259496a8c8044741d32194f
manifest_code_sha = 5a9731afdc4991b3976b1f5531506188741c9baedeb364b94c3adc542f55cccc
run_zip_sha256    = 7868a70bb60b4da375c04e0a3b2ea5615dd52c5cebb9a51da444df94f7496a71
result            = S2R_LOCAL_K_REFUTED
```

# 3. KREF0 — compatibilidade de referentes do antecedente

O run científico de S2RK0 somente é aceito nesta linhagem porque o Gate prospectivo `KREF0` foi satisfeito antes da inferência.

```text
KREF0_status       = PASS
KREF0_artifact     = HUMH_S2RK0_ReferentCompatibility_v1.0.1_PASS.json
KREF0_sha256       = 234c752534589f84d53836cdc18d3964ba30c17783292f977fbf6fcfdeeef6f7
```

A presença desse artefato na linhagem não reescreve manifests históricos. Ela apenas documenta que a compatibilidade de referentes exigida pela spec S2RK0 v1.0.1 foi satisfeita no ramo científico considerado válido.

# 4. Resultado histórico preservado

Registrar permanentemente:

```text
N3T-K0_CONSTANT = REFUTADA [C1]
```

A nova linha de atenção não reclassifica, apaga ou converte esse resultado em compatibilidade.

# 5. Motivação

A HUMH distingue propriedades do observador de propriedades estruturais do sistema.

Atenção é introduzida como variável própria do observador e não como novo parâmetro livre criado para ajustar o resultado anterior.

# 6. Atenção não é sinônimo de outros termos

Atenção não é sinônimo de:

- confiança;
- Entropia de Hipótese `EH`;
- inércia observacional;
- resistência estrutural;
- dívida de manutenção;
- reserva estrutural;
- prioridade nominal de thread;
- velocidade global da CPU;
- taxa observada de mudança de crença.

# 7. Definição fundamental

Para um observador `O_i`, define-se **Atenção Observacional Efetiva** por:

\[
\boxed{
A_i(W)=\frac{U_i(W)}{D_i(W)}
}
\]

com:

\[
0\le A_i\le1.
\]

# 8. Demanda exógena D_i

A variável `D_i(W)` é definida como:

\[
\boxed{
D_i(W)=
\#\{\text{requisições observacionais elegíveis geradas exogenamente para }O_i\text{ em }W\}
}
\]

# 9. Independência de D_i da atenção

A demanda deve ser determinada antes da manipulação do orçamento do observador.

Por construção:

\[
\boxed{
D_i\perp P_i^{obs}
}
\]

no sentido experimental de que mudar o braço de atenção não muda o número, identidade ou conteúdo das requisições observacionais geradas.

# 10. Proibição de demanda endógena

É proibido definir `D_i` a partir de:

- quantidade de CPU recebida;
- atualizações concluídas;
- estado final do observador;
- `EH` futuro;
- perda do atrator;
- scheduler do braço;
- outcome experimental.

# 11. Regra mínima de geração de demanda

No primeiro A1, a forma preferencial é gerar uma requisição observacional elegível por observador por ciclo lógico:

\[
D_i(W)=W
\]

quando `W` é contado em ciclos e não há ciclos inelegíveis por contrato.

A spec pré-código de A1 deve congelar quaisquer exceções.

# 12. Atualização atendida U_i

`U_i(W)` é o número de requisições de `D_i(W)` cuja sequência:

\[
\text{observar}\rightarrow\text{processar}\rightarrow\text{atualizar estado}
\]

foi concluída dentro do prazo válido.

# 13. Janela W

`W` é uma janela de medição definida em **ciclos lógicos do experimento**, não em milissegundos de relógio de parede.

A spec de A1 deve congelar `W` antes do run.

# 14. Deadline observacional L_A

Cada requisição criada no ciclo `t` tem prazo operacional exógeno:

\[
\boxed{
t_{complete}\le t+L_A
}
\]

para contar em `U_i`.

# 15. Independência de L_A

`L_A` deve ser igual em todos os braços e não pode depender de:

- prioridade;
- budget;
- performance observada;
- `EH`;
- `iota_obs`;
- resultado.

# 16. Escolha de L_A

Para o primeiro A1, preferir `L_A=1` ciclo se a arquitetura comportar uma atualização completa nesse intervalo.

Se não comportar, `L_A` deve ser determinado em piloto técnico separado, congelado antes do confirmatório e jamais escolhido olhando o efeito científico.

# 17. ABENCH0 — benchmark cego de instrumentação

Se `L_A=1` não for tecnicamente adequado, a escolha de `L_A` deve ser feita exclusivamente por um benchmark cego de instrumentação:

```text
ABENCH0 — ATTENTION_INSTRUMENTATION_BENCHMARK
```

O benchmark ocorre antes do run científico e não pode exportar nenhum outcome de A1a/A1b.

# 18. Saídas permitidas em ABENCH0

ABENCH0 pode exportar somente quantidades instrumentais/técnicas, tais como:

```text
D_i
U_i
A_i
distribuição de latência de update
deadline_misses
queue/service timing técnico
runtime metadata
hardwareConcurrency
```

# 19. Saídas proibidas em ABENCH0

É proibido calcular, exportar, mostrar ou usar para escolher `L_A`:

```text
eta_hat
trajetórias p_i(t)
EH
dispersão de crença
consenso
atrator/perda de atrator
Y
T_dwell
t_trans
chi_O
qualquer estatística primária ou secundária de A1a/A1b
```

# 20. Regra de seleção de L_A

Antes de executar ABENCH0, a spec pré-código deve congelar:

- conjunto finito candidato `L_grid`;
- budgets instrumentais usados no benchmark;
- faixa admissível de `A` para evitar saturação em 0 ou 1;
- contraste mínimo instrumental entre braços;
- regra determinística de desempate.

ABENCH0 seleciona o menor `L_A` que satisfaça todos os critérios instrumentais congelados. Se nenhum candidato satisfizer os critérios, o resultado é:

```text
ABENCH0 = FAIL
SCIENTIFIC_RUN_NOT_AUTHORIZED
```

É proibido alterar os critérios após visualizar qualquer outcome científico.

# 21. Atualização atrasada

Se a atualização ultrapassa `L_A`:

```text
DEMAND_NOT_SERVED_IN_TIME
```

Ela permanece em `D_i`, mas não entra em `U_i`.

# 22. Atenção é exposição efetiva

A variável teórica é:

\[
\boxed{A_i=U_i/D_i}
\]

O orçamento nominal é somente instrumento de manipulação.

# 23. Prioridade não é atenção

É proibido definir:

\[
A_i\equiv\texttt{threadPriority}.
\]

A prioridade de thread, quando disponível, é apenas possível instrumento causal.

# 24. Instrumento local do observador

Defina:

\[
P_i^{obs}
\]

como orçamento/oportunidade de execução local concedido especificamente à cadeia observacional.

A relação experimental é:

\[
\boxed{P_i^{obs}\rightarrow A_i.}
\]

# 25. Implementação preferencial no browser

Como Web Workers não oferecem prioridade de thread de SO portátil e controlável, A1 deve preferir controle lógico explícito:

```text
required_updates
allowed_observer_updates
observer_deadline
valid_updates_completed
valid_updates_missed
```

# 26. CPU global não é braço de atenção

No A1 confirmatório é proibido criar contraste de atenção alterando:

- clock/frequência global de CPU;
- carga global da máquina;
- thermal throttling global;
- número global de cores;
- processo concorrente global;
- máquina física.

# 27. ATTENTION_ISOLATION

Entre braços, manter invariantes:

\[
\boxed{
C_{CPU}^{global},
\gamma_{manut},
service,
propagation,
R_{eff}^*,
\text{topologia e microdinâmica estrutural}
}
\]

até os limites prospectivamente congelados no Gate de isolamento.

# 28. Motivo do isolamento

Se atenção local e CPU global forem alteradas juntas, um efeito pode ser causado por atenção, manutenção, serviço, propagação ou interação entre esses componentes.

Esse desenho não testa causalmente atenção.

# 29. Atenção coletiva média

Para `N` observadores:

\[
\boxed{
\bar A=\frac1N\sum_{i=1}^{N}A_i.
}
\]

# 30. Heterogeneidade de atenção

Defina:

\[
\boxed{
D_A=\frac1N\sum_{i=1}^{N}|A_i-\bar A|.
}
\]

# 31. Não suficiência automática de A_bar

A mesma `A_bar` pode representar distribuições distintas de atenção.

Exemplo conceitual:

```text
UNIFORM:   A_i = 0.5 para todos
POLARIZED: metade A_i = 1; metade A_i = 0
```

Ambos têm `A_bar=0.5`, mas `D_A` diferente.

# 32. Atenção como recurso do observador

Na HUMH, atenção representa:

\[
\boxed{
\text{capacidade efetivamente disponibilizada para processar uma demanda observacional exógena dentro do prazo válido}
}
\]

# 33. Atenção versus inércia observacional

Atenção e inércia observacional são distintas.

É proibido definir:

\[
A_i\equiv1/\iota_{obs,i}.
\]

# 34. Observador atento e inercial

Pode ocorrer:

\[
A_i\approx1,
\qquad
\iota_{obs,i}\gg0.
\]

O observador recebe capacidade para processar, mas resiste a alterar seu estado.

# 35. Observador pouco atento e pouco inercial

Também pode ocorrer:

\[
A_i\ll1,
\qquad
\iota_{obs,i}\approx0.
\]

O observador mudaria facilmente se processasse, mas recebe poucas oportunidades efetivas.

# 36. Distinção oficial

\[
\boxed{A_i=\text{disponibilidade efetiva para processar/atualizar}}
\]

\[
\boxed{\iota_{obs,i}=\text{resistência do observador à atualização}}
\]

# 37. Dinâmica basal sem atenção

Defina a dinâmica basal do observador:

\[
\eta_i^{(0)}(p)=
\frac{\omega_i}{1+\iota_{obs,i}+\kappa EH(p)}.
\]

# 38. Dois canais de mensuração independentes

A1a exige dois canais operacionalmente separados:

```text
CANAL_A   = contadores do scheduler: D_i, U_i -> A_i
CANAL_ETA = trajetória de estado: p_i(t), p_alvo,i(t) -> eta_hat
```

`eta_hat` não pode ser calculado a partir de `U_i`, `D_i`, `A_i`, budget, misses ou rótulo do braço.

# 39. Drive dinâmico observável

Para cada passo elegível, defina:

\[
x_{it}=p_{alvo,i}(t)-p_i(t)
\]

\[
y_{it}=p_i(t+1)-p_i(t).
\]

O alvo `p_alvo,i(t)` deve ser registrado pela dinâmica basal antes da atualização de `p_i(t+1)` e não pode ser reconstruído a partir dos contadores de atenção.

# 40. Estimador primário de eta

Para cada observador/condição e estrato prospectivamente definido de estado, o estimador primário é a inclinação sem intercepto:

\[
\boxed{
\widehat\eta
=
\frac{\sum_{t\in\mathcal E} x_{it}y_{it}}{\sum_{t\in\mathcal E}x_{it}^{2}}
}
\]

onde `E` é o conjunto de passos elegíveis congelado pela spec pré-código.

A forma do estimador fica congelada nesta definição. A próxima spec deve congelar apenas os valores numéricos dos critérios de elegibilidade, estratos e Gates de identificação.

# 41. Elegibilidade para estimar eta

A spec pré-código deve excluir passos sem identificação suficiente, incluindo no mínimo casos em que:

\[
|x_{it}|<\delta_{drive}.
\]

`delta_drive`, número mínimo de passos e informação mínima `sum(x^2)` devem ser congelados antes do run científico.

É proibido escolher esses valores olhando o efeito de atenção.

# 42. Independência aritmética de eta_hat

O estimador de `eta` é proibido de usar como input direto ou indireto:

```text
U_i
D_i
A_i
A_bar
D_A
attention_arm
attention_budget
served_fraction
deadline_misses
```

A razão `eta_hat/A` só é calculada depois que `eta_hat` e `A` foram produzidos por módulos separados.

# 43. AETA0 — Gate de identificação e independência

Antes de `ASEP0`, deve passar:

```text
AETA0 — ETA_IDENTIFICATION_AND_INDEPENDENCE
```

AETA0 exige cumulativamente:

1. informação dinâmica suficiente segundo limiares congelados;
2. `eta_hat` finito e identificável nos estratos requeridos;
3. auditoria de dependências demonstrando que o módulo de `eta_hat` não lê contadores/arm/budget;
4. teste de permutação estrutural: mantendo as trajetórias `p` fixas e permutando `U/D/A`, `eta_hat` deve permanecer bitwise idêntico;
5. teste de sensibilidade: mantendo os contadores fixos e alterando uma trajetória sintética com inclinação conhecida, `eta_hat` deve responder na direção/magnitude esperada.

Falha em qualquer item produz:

```text
INCONCLUSIVE_ETA_IDENTIFICATION
```

e `ASEP0` não é interpretado.

# 44. NO_ATTENTION_IN_OBSERVER_RULE

É proibido inserir atenção como fator literal ou metadado na regra de atualização do observador.

A função que atualiza `p_i` não pode ler:

```text
A_i
A_bar
D_A
attention_arm
attention_budget
served_fraction
qualquer transformação direta dessas variáveis
```

Em particular, é proibido codificar:

```text
eta = A * omega / (1 + iota_obs + kappa*EH)
```

como regra executada pelo observador.

# 45. Papel permitido do scheduler

O scheduler pode decidir se uma requisição observacional recebe oportunidade de execução e se termina dentro de `L_A`.

Quando a rotina do observador é chamada, ela recebe somente os inputs observacionais/dinâmicos permitidos; não recebe o valor de atenção nem o rótulo do braço.

`A_i` é medido a posteriori a partir de `U_i/D_i` em módulo de instrumentação separado.

# 46. Gate de ausência de auto-confirmação literal

Antes do run científico, uma auditoria estática/dinâmica do código deve confirmar `NO_ATTENTION_IN_OBSERVER_RULE`.

Falha produz:

```text
INVALID_SELF_CONFIRMATORY_IMPLEMENTATION
SCIENTIFIC_RUN_NOT_AUTHORIZED
```

# 47. Hipótese H-A1S — separabilidade multiplicativa

A hipótese mecanística principal deixa de ser “mais atenção produz mais updates”.

Passa a ser:

\[
\boxed{
H\!\text{-}A1_S:\quad
\eta_i(A,p)=A_i\,\eta_i^{(0)}(p)
}
\]

ou:

\[
\boxed{
\eta_i(A,p)=
\frac{A_i\omega_i}{1+\iota_{obs,i}+\kappa EH(p)}.
}
\]

# 48. Conteúdo falsificável de H-A1S

O conteúdo científico não é que o throttle funcione.

É que atenção entra como **fator multiplicativo separável**, sem exigir novo termo aditivo em `iota_obs` e sem interação extra não prevista com `EH`.

# 49. Predição de razão

Para o mesmo observador/estado basal:

\[
\boxed{
\frac{\eta_i(A_2,p)}{\eta_i(A_1,p)}
=
\frac{A_2}{A_1}.
}
\]

# 50. Predição normalizada

Equivalentemente:

\[
\boxed{
\frac{\eta_i(A,p)}{A_i}
=
\eta_i^{(0)}(p).
}
\]

A quantidade `eta/A` deve ser invariável entre braços de atenção dentro da margem prospectivamente congelada.

# 51. O que pode refutar H-A1S

H-A1S pode falhar se, por exemplo:

- `eta/A` variar materialmente entre braços;
- atenção agir como resistência aditiva;
- houver interação adicional `A × EH` além da forma multiplicativa;
- houver interação adicional `A × iota_obs` além da forma prevista;
- um único parâmetro basal não generalizar entre condições retidas.

# 52. Separabilidade não pode ser consequência algébrica do scheduler

A ausência de `A_i` no código do observador é necessária, mas não suficiente.

A1a só recebe interpretação científica se a separabilidade multiplicativa não for uma identidade ou teorema automático das microdinâmicas de execução/descarte.

# 53. ANBC0 — SEPARABILITY_NOT_BY_CONSTRUCTION

Antes do run confirmatório deve ser executada uma auditoria analítica e computacional:

```text
ANBC0 — SEPARABILITY_NOT_BY_CONSTRUCTION
```

Ela deve determinar se, dadas as microdinâmicas congeladas, o mecanismo de serving/thinning implica necessariamente:

\[
E[\Delta p\mid p,A]=A\,f(p)
\]

independentemente da hipótese HUMH.

# 54. Consequência de ANBC0

Se a separabilidade for garantida por construção:

```text
ANBC0 = FAIL
A1a = MECHANISM_DEMONSTRATION_ONLY [C1]
ASEP0_CONFIRMATORY = NOT_AUTHORIZED
```

Nesse caso o resultado não pode receber `ATTENTION_MULTIPLICATIVE_SEPARABILITY_COMPATIBLE [C1]`.

A1b pode continuar somente se possuir conteúdo próprio e Gates independentes.

# 55. Competência adversarial para não-separabilidade

Mesmo com `ANBC0=PASS`, a implementação deve incluir uma condição sintética de benchmark em que uma interação não separável conhecida seja introduzida apenas no harness de validação.

O pipeline de análise deve detectá-la com a competência prospectivamente congelada; caso contrário o confirmatório real é inconclusivo.

# 56. Correção importante sobre EH

H-A1S **não** prevê o mesmo efeito absoluto de `A` em todos os níveis de `EH`.

Pois:

\[
\frac{\partial\eta}{\partial A}
=
\frac{\omega}{1+\iota_{obs}+\kappa EH}.
\]

# 57. Invariância correta em EH

A previsão é relativa:

\[
\boxed{
\frac{\eta(A_2,EH)}{\eta(A_1,EH)}
=
\frac{A_2}{A_1}
}
\]

para regimes de `EH` diferentes, mantidos os demais termos correspondentes.

# 58. Correção importante sobre iota_obs

Um mesmo `A` não deve produzir o mesmo `eta` quando `iota_obs` muda.

A equação prevê explicitamente:

\[
\iota_{obs}\uparrow\Rightarrow\eta\downarrow
\]

para `A`, `EH` e `omega` fixos.

# 59. A1 não pode receber crédito por direção trivial

A constatação isolada:

```text
A_HIGH > A_LOW e updates_HIGH > updates_LOW
```

é manipulation check, não confirmação de H-A1S.

# 60. Manipulation check

A1 só é cientificamente interpretável se os braços produzirem níveis de atenção suficientemente distintos segundo critério congelado.

Falha:

```text
INCONCLUSIVE_MANIPULATION
```

# 61. Common Random Numbers

Entre condições pareadas, manter:

```text
mesmo estado inicial
mesmas requisições D_i
mesmo conteúdo observacional
mesmas tarefas estruturais
mesmos arrivals
mesmo serviço
mesma propagação
mesmo RNG exógeno
```

alterando apenas `P_i^obs`.

# 62. Gate ATTENTION_ISOLATION_GATE

A spec A1 deve definir um Gate que verifique que a manipulação não alterou materialmente:

- manutenção;
- serviço;
- propagação;
- topologia;
- demanda exógena;
- outros componentes estruturais.

Falha:

```text
INCONCLUSIVE_TECHNICAL_OR_ISOLATION
```

# 63. A0 deixa de ser “teste de definição”

A0 passa a chamar-se:

```text
A0 — ATTENTION MEASUREMENT CONTRACT
```

Definição não “passa” empiricamente.

# 64. Objeto de A0

A0 deve congelar:

\[
D_i,
U_i,
W,
L_A,
A_i=U_i/D_i
\]

além de:

- contadores, timing e regras de descarte;
- `ABENCH0` e sua regra cega de seleção de `L_A`;
- definição de `p_alvo`;
- estimador primário `eta_hat` baseado em trajetória;
- critérios de elegibilidade e identificação de `eta_hat`;
- separação dos módulos `CANAL_A` e `CANAL_ETA`;
- auditoria `NO_ATTENTION_IN_OBSERVER_RULE`;
- Gate `AETA0`;
- auditoria `ANBC0`.

# 65. O que A0 pode verificar

A0 pode verificar instrumentalmente:

- ausência de contagem dupla;
- identidade de `D_i` entre braços pareados;
- exogeneidade da demanda;
- reprodutibilidade;
- integridade do deadline;
- estabilidade dos contadores;
- capacidade de produzir contraste em `A` sem contaminar o substrato.

# 66. A1a — separabilidade individual

A primeira hipótese científica é:

```text
A1a — ATTENTION_MULTIPLICATIVE_SEPARABILITY
```

com H-A1S como núcleo.

# 67. A1b — distribuição coletiva da atenção

A segunda hipótese científica é:

```text
A1b — ATTENTION_DISTRIBUTION_EFFECT
```

Ela pergunta se, mantendo `A_bar` constante, alterar `D_A` modifica a dinâmica coletiva.

# 68. Conteúdo genuíno de A1b

Como `A_bar` é igual entre braços, uma diferença coletiva não pode ser atribuída apenas à quantidade média total de atenção.

Isso testa se a distribuição de atenção contém informação dinâmica adicional.

# 69. A1b não é consequência automática de H-A1S

H-A1S é uma hipótese individual/separável.

A1b testa uma consequência coletiva adicional e deve possuir spec e Gates próprios.

# 70. Braços numéricos não são congelados nesta definição

Valores como `100/60/25%` não são parte desta definição consolidada.

A spec A0/A1 deve derivar níveis de atenção por critério estrutural/instrumental antes do outcome científico.

# 71. Proibição de escolher contraste pela resposta científica

É proibido aumentar ou reduzir o contraste HIGH/MID/LOW depois de observar efeitos em `eta`, `EH`, consenso ou outro outcome científico.

# 72. Relação com CPU física

CPU física pode afetar atenção em sistemas reais, mas deve ser estudada somente em experimento separado depois do teste isolado.

# 73. Experimento fatorial futuro

Uma etapa posterior pode testar:

\[
2\times2:
\quad
\text{atenção local HIGH/LOW}
\times
\text{recurso global HIGH/LOW}.
\]

Isso não pertence a A1a/A1b confirmatórios iniciais.

# 74. Relação com R_eff_star

Atenção não substitui:

\[
R_{eff}^*.
\]

`R_eff_star` permanece reserva estrutural condicionada ao estado.

# 75. Relação com gamma_manut

Atenção não substitui:

\[
\gamma_{manut}.
\]

`gamma_manut` mede a dinâmica de manutenção do substrato.

# 76. Relação com EH

Atenção não é `EH`.

`EH` representa indeterminação da hipótese; atenção representa disponibilidade de processamento observacional.

# 77. Relação com D de crença

`D_A` não é a dispersão entre estados/crenças dos observadores.

São variáveis distintas.

# 78. Relação com kappa

Não confundir:

\[
\kappa
\]

com o coeficiente macroscópico de transporte.

`kappa` continua sendo o acoplamento estrutural de `EH` em `iota_ord`.

# 79. Coeficiente macroscópico diagnóstico corrigido

Compatível com S2RK0 v1.0.1, defina somente diagnosticamente:

\[
\boxed{
\chi_O(X)
=
\frac{
\widetilde Y^{KM}(X)\,\gamma_{manut}(X)
}{
R_{eff}^*(X)
}
}
\]

onde `Y` é o tempo até `A_exit`, com censura e estimativa primária por mediana Kaplan–Meier.

# 80. Proibição da definição antiga de chi_O

Não usar como estimando primário:

\[
(T_{dwell}-t_{trans})\gamma/R^*
\]

calculado somente em trajetórias completas.

Essa forma foi abandonada por causa do viés de censura.

# 81. chi_O não é parâmetro livre

É proibido definir um modelo preditivo usando o próprio `Y` da condição VAL para construir `chi_O`.

Isso seria tautológico.

# 82. Hipótese antiga preservada

O caso constante permanece historicamente:

\[
H_{K0}:\chi_O(X)=K_0.
\]

Status:

```text
REFUTADA [C1]
```

# 83. A2 não está autorizado nesta definição

A linha atual termina cientificamente em A1a/A1b.

`A2 — ATTENTION_MACRO_TRANSPORT` permanece:

```text
NOT AUTHORIZED / NOT TESTED
```

até resultado prospectivo de A1.

# 84. Possível forma futura de A2

Se A1 sobreviver, poderá ser proposta:

\[
\chi_O(X)=G(A(X),Z(X);\theta).
\]

Essa equação ainda não é uma hipótese congelada de teste.

# 85. Regra anti-contaminação para Z

Os resíduos por célula de S2RK0 já foram observados.

Portanto, variáveis como:

```text
M
rC
snapshot_cycle
lambda
```

são marcadas nesta linha como:

```text
POST_S2RK0_EXPOSED
```

# 86. Consequência da exposição prévia

Variáveis `POST_S2RK0_EXPOSED` não podem ser apresentadas na primeira geração de A2 como candidatos confirmatórios independentes cuja escolha não foi influenciada pelos resultados anteriores.

Se usadas por essa motivação, a análise correspondente deve ser rotulada exploratória.

# 87. Lista fechada de Z neste estágio

Para A0/A1:

\[
\boxed{Z_{allowed}=\varnothing}
\]

Nenhuma variável `Z` entra no teste principal de atenção.

# 88. Lista fechada futura de Z

Antes de qualquer A2 confirmatório, uma nova spec deve congelar uma lista fechada de `Z`, origem teórica de cada variável e declaração explícita de exposição prévia.

Não é permitido acrescentar variáveis depois de observar VAL.

# 89. Consequência para a viabilidade confirmatória de A2 em S2R

Como `M`, `rC`, `snapshot_cycle` e `lambda` já foram expostos aos resíduos de S2RK0, eles não podem ser reutilizados como candidatos confirmatórios independentes motivados por esses mesmos resíduos.

Logo, a viabilidade de um primeiro A2 confirmatório no mesmo substrato S2R é atualmente:

```text
A2_S2R_CONFIRMATORY_FEASIBILITY = UNDETERMINED
```

Um A2 no mesmo substrato só poderá ser confirmatório se usar variáveis antecedentes com origem teórica independente — por exemplo variáveis de atenção prospectivamente definidas — sem reconstruir retrospectivamente os resíduos de S2RK0.

Se não existir conjunto antecedente não contaminado suficiente, A2 deverá migrar para novo desenho/substrato.

# 90. Teto de dimensão para o primeiro A2

Se A2 for autorizado futuramente:

\[
\boxed{\dim(\theta)\le3.}
\]

Esse teto já fica congelado aqui para impedir expansão oportunista da primeira geração de modelo.

# 91. Forma de G não é escolhida agora

A forma funcional de `G` deve ser congelada em nova spec A2 antes da coleta confirmatória correspondente.

Nenhuma busca irrestrita de modelos é autorizada.

# 92. CAL/VAL obrigatório em A2

Se A2 for aberto, parâmetros são estimados apenas em CAL e congelados antes de VAL.

Não há refit em VAL.

# 93. Dados S2RK0 não confirmam G

Os dados que revelaram a falha de `K` constante podem motivar novas perguntas, mas não podem ser apresentados como confirmação de uma função `G` construída posteriormente.

# 94. Novos dados obrigatórios

Qualquer confirmatório A1/A2 deve usar:

- nova spec pré-código;
- novas seeds;
- nova execução;
- Gates congelados antes da coleta;
- nenhum top-up motivado pelo resultado.

# 95. Status epistemológico em C1

Resultado positivo em substrato computacional construído continua limitado a:

```text
COMPATÍVEL [C1]
```

salvo regra epistemológica superior explicitamente satisfeita em outro substrato/classe.

# 96. Falha material pode refutar a hipótese específica

Com Gates adequados, uma violação material prospectivamente definida pode produzir:

```text
REFUTADA [C1]
```

para H-A1S ou para A1b, sem implicar refutação automática de toda a HUMH.

# 97. A0 não ganha status de suporte teórico

Um A0 tecnicamente bem-sucedido apenas estabelece um instrumento de mensuração utilizável.

Não constitui suporte a HUMH.

# 98. CPU global como diagnóstico

CPU time, event-loop delay e carga global podem ser registrados para auditoria técnica.

Não entram na definição de `A_i` e não servem como substitutos de `A_i`.

# 99. Separação entre máquina e atenção

Máquina diferente não é braço de atenção.

Comparações entre máquinas exigem desenho próprio.

# 100. Atenção variável no tempo

A definição admite:

\[
A_i=A_i(t).
\]

Entretanto, o primeiro A1 deve preferir atenção aproximadamente estacionária por braço.

# 101. Atenção heterogênea entre observadores

A definição admite:

\[
A_i\ne A_j.
\]

A distribuição deve ser congelada antes do run.

# 102. Identidade de demanda em A1b

Ao comparar distribuições de atenção, `D_i` deve continuar idêntico por observador entre braços pareados.

Somente a capacidade de atender essa demanda é redistribuída.

# 103. Ausência de realocação reativa

No primeiro A1b, é proibido realocar orçamento de atenção em resposta a `EH`, crença, dívida, sucesso ou falha do observador durante a trajetória.

A regra de alocação deve ser exógena/congelada.

# 104. Ponte humana futura

Em humanos, atenção não deve ser identificada diretamente com um único indicador comportamental.

Uma ponte futura precisa de proxy independente e validado.

# 105. Limite ontológico da analogia computacional

Prioridade/quantum é analogia operacional de alocação de recurso.

Não é identidade ontológica com atenção humana.

# 106. Cadeia causal computacional

O substrato computacional testa a estrutura:

\[
\boxed{
P_i^{obs}
\rightarrow
A_i
\rightarrow
\text{forma da dinâmica observacional}
\rightarrow
\text{dinâmica coletiva}
}
\]

# 107. Cadeia que não recebe crédito

A cadeia trivial:

\[
\text{throttle}\rightarrow\text{menos operações executadas}
\]

não recebe status científico por si só.

# 108. Critério científico de A1a

O teste deve distinguir prospectivamente entre pelo menos:

```text
M_sep: atenção multiplicativa separável
M_alt: forma não separável / interação adicional
```

com margens e decisão congeladas antes do run.

# 109. ACOMP0 — competência adversarial do pipeline

A implementação A1 deve demonstrar em benchmark sintético que consegue detectar violações conhecidas da separabilidade quando artificialmente introduzidas.

Sem essa competência, um PASS de separabilidade é inconclusivo.

# 110. Manipulation gate não é scientific gate

A separação HIGH/MID/LOW em `A` é requisito de adequação experimental.

Ela não conta como evidência positiva de H-A1S.

# 111. Isolation gate não é scientific gate

Preservar manutenção/serviço/propagação é requisito causal.

Também não conta como suporte positivo.

# 112. Estrutura mínima de Gates para A1

A spec pré-código deve conter no mínimo:

```text
AGOV0   — governança/hashes/KREF0 lineage
AMEAS0  — contrato D/U/W/L_A e contadores
ABENCH0 — benchmark cego de instrumentação/deadline
AMAN0   — manipulation check de A
AISO0   — isolamento estrutural
AETA0   — identificação independente de eta_hat
ANBC0   — separabilidade não garantida por construção
ACOMP0  — competência para detectar não-separabilidade
ASEP0   — teste primário H-A1S
ADIST0  — teste A1b, se executado na mesma spec
AINT0   — integridade/RNG/checkpoint
```

# 113. Resultado A1a compatível

Somente se `AGOV0`, `AMEAS0`, `ABENCH0`, `AMAN0`, `AISO0`, `AETA0`, `ANBC0`, `ACOMP0`, `AINT0` e a inferência `ASEP0` passarem:

```text
ATTENTION_MULTIPLICATIVE_SEPARABILITY_COMPATIBLE [C1]
```

# 114. Resultado A1a refutado

Se houver violação material prospectivamente definida com Gates adequados:

```text
ATTENTION_MULTIPLICATIVE_SEPARABILITY_REFUTED [C1]
```

# 115. Resultado A1a inconclusivo

Falta de potência, separação de atenção, benchmark ou isolamento produz categoria inconclusiva correspondente, não refutação automática.

# 116. Resultado A1b

A1b deve separar:

```text
ATTENTION_DISTRIBUTION_EFFECT_ESTABLISHED/COMPATIBLE [C1]
ATTENTION_DISTRIBUTION_EFFECT_NOT_ESTABLISHED
ATTENTION_DISTRIBUTION_EFFECT_REFUTED
INCONCLUSIVE_*
```

conforme a hipótese/margens congeladas na futura spec pré-código.

# 117. Formulação compacta oficial de atenção

> **Atenção Observacional Efetiva** é a fração da demanda observacional exógena de um observador que recebe recursos suficientes para completar a sequência observação–processamento–atualização dentro de um deadline lógico exógeno e comum aos braços. Denotada por `A_i in [0,1]`, ela é distinta da inércia observacional, de EH, da reserva estrutural e da manutenção. Prioridade, quantum ou budget local são instrumentos de manipulação; a variável teórica é a fração efetivamente atendida `A_i=U_i/D_i`.

# 118. Formulação compacta oficial de H-A1S

\[
\boxed{
\eta_i(A,p)
=
A_i\,
\frac{\omega_i}
{1+\iota_{obs,i}+\kappa EH(p)}
}
\]

O conteúdo falsificável é a separabilidade multiplicativa observada entre os dois canais independentes de mensuração, não a direção trivial do throttle. Esta equação é hipótese de descrição macroscópica/observacional e **não** pode ser inserida literalmente na regra executada pelo observador.

# 119. Nova sequência formal

```text
N3T-K0_CONSTANT = REFUTADA [C1]

A0  = ATTENTION MEASUREMENT CONTRACT
A1a = ATTENTION MULTIPLICATIVE SEPARABILITY
A1b = ATTENTION DISTRIBUTION EFFECT
A2  = ATTENTION–MACRO TRANSPORT — NOT AUTHORIZED / NOT TESTED
```

# 120. Regra final de congelamento

Esta definição pode ser congelada conceitualmente com `A0`, `A1a` e `A1b` como próximos objetos **porque agora separa explicitamente o canal de atenção do canal de dinâmica e proíbe auto-confirmação por código**.

A próxima spec pré-código deve operacionalizar, sem alterar estas regras:

- valores numéricos dos braços de atenção;
- `W` final;
- `L_grid` e critérios cegos de `ABENCH0`;
- `L_A` final;
- `delta_drive`, informação mínima e estratos do estimador `eta_hat`;
- margens de equivalência/refutação de A1a/A1b;
- competência mínima de `ACOMP0`;
- procedimento formal de `ANBC0`;
- tamanho amostral;
- forma de `G` de A2, somente se A2 vier a ser autorizado.

Nenhum desses elementos pode ser escolhido após observar outcomes científicos da nova coleta.
