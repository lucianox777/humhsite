# HUMH — Programa Experimental N3 1.9-B

**Identidade do objeto:** `HUMH_N3_1.9B`  
**Status:** EM DESENVOLVIMENTO / NÃO CONGELADO  
**Plataforma C1 inicial:** HTML + JavaScript + Web Workers  
**Referente teórico normativo:** `teoria.md`  
**Rótulo de versão no cabeçalho da teoria:** 1.7.2  
**SHA-256 do referente teórico:** `5c8258e1aae5f735d5730ddc93f0f816825c8ec2b23f126aa0c969d10a0a5505`  
**Núcleo companheiro congelável:** `HUMH_Nucleo_1.9A.md`  
**SHA-256 do núcleo nesta distribuição:** `dfdd673da080b4e1e4038f7a57c2608d48c947f77a1629b9094cfb18bd835991`

> Este arquivo pode continuar evoluindo sem alterar `HUMH_Nucleo_1.9A.md`. As regras normativas de N1a/N1b/N2, incluindo modelos aninhados, taxonomia e resgates proibidos, residem exclusivamente no núcleo 1.9-A.  
> A numeração histórica das seções abaixo foi preservada para rastreabilidade com a versão metodológica unificada 2.2.

---

# PARTE II — PROGRAMA N3 1.9-B

# 22. Separação lógica

N3 possui dois níveis:

\[
\boxed{N3T_K}
\]

e:

\[
\boxed{N3F}.
\]

N3T\(_K\) testa uma escala macroscópica transportável.

N3F testa uma forma dinâmica inteira transportável.

---

# 23. Relação entre as hipóteses

É possível:

\[
N3T_K=\text{COMPATÍVEL}
\]

e:

\[
N3F=\text{REFUTADA}.
\]

Portanto:

\[
\boxed{
\neg N3F
\not\Rightarrow
\neg N3T_K.
}
\]

---

# 24. Lei escalar candidata

N3T\(_K\) utiliza:

\[
\boxed{
T_{dwell}
\approx
t_{trans}
+
K_{N3}
\frac{R_{eff}}
{\gamma_{manut}}.
}
\]

---

# 25. Número adimensional

Define-se:

\[
\Pi_{N3}
=
\frac{
(T_{dwell}-t_{trans})
\gamma_{manut}
}{
R_{eff}
}.
\]

Na forma operacional:

\[
\Pi_{N3}=K_{N3}.
\]

---

# 26. O que não conta como suporte

Não recebe crédito:

\[
K\approx1.
\]

Também não recebe crédito o simples fato de:

\[
R/\gamma
\]

possuir dimensão temporal.

O compromisso é:

\[
\boxed{
K_{S1}
\approx
K_{S2}
\approx
K_{S3}.
}
\]

---

# PARTE III — CONGELAMENTO ANTES DA EXECUÇÃO

# 27. Desenho dos três substratos

Antes de estimar \(K\) em S1 deverão estar completamente especificados:

\[
S1,\quad S2,\quad S3.
\]

---

# 28. Elementos congelados

Devem incluir:

- UM;
- \(R_{eff}\);
- \(\gamma_{manut}\);
- \(t_{trans}\);
- topologias;
- capacidades;
- schedulers;
- expiração;
- propagação;
- retransmissão;
- condições CAL/VAL;
- seeds;
- duração;
- métricas;
- Gates;
- benchmarks.

---

# 29. Overfitting de desenho proibido

É proibido:

\[
S1
\rightarrow
K
\rightarrow
escolher\ S2/S3.
\]

A ordem será:

\[
\boxed{
desenhar
\rightarrow
hash
\rightarrow
executar.
}
\]

---

# PARTE IV — S1

# 30. Fila central

S1 utiliza:

\[
B(t+1)
=
\max[
0,
B(t)+A_M(t)-C
].
\]

S1 é:

\[
\boxed{C1}.
\]

---

# 31. S1-CAL

Somente:

\[
S1_{CAL}
\]

estima:

\[
K_{N3}.
\]

---

# 32. S1-VAL

Condições retidas de S1 serão previstas sem reajuste.

---

# 33. Gate K0

Antes de qualquer transporte:

\[
\boxed{
K_{N3}
\text{ precisa ser internamente invariável em S1.}
}
\]

---

# 34. Parada em S1

Se S1-VAL falhar confirmatoriamente com poder suficiente:

\[
\boxed{
N3T_K
\text{ é REFUTADA nesta forma.}
}
\]

Não se prossegue para S2/S3 para tentar resgatá-la.

---

# PARTE V — S2

# 35. Rede de dívida propagável

Cada nó possui capacidade local:

\[
C_i.
\]

Dívida não resolvida pode gerar nova dívida:

\[
i\rightarrow j\rightarrow k.
\]

---

# 36. Diferença obrigatória

S2 não pode ser apenas:

\[
N
\]

filas independentes.

A propagação deve modificar:

- correlações;
- dependências temporais;
- caminhos de falha;
- first-passage coletivo.

S2 é C1.

---

# 37. Teste S2

O mesmo \(K_{N3}\) de S1 deverá prever S2.

Se for necessário:

\[
K_{S2}
\]

fora de \(\delta_{transport}\):

\[
\boxed{
N3T_K
\text{ transversal é REFUTADA.}
}
\]

---

# PARTE VI — S3

# 38. Banda informacional

S3 limita:

\[
mensagens/ciclo
\]

ou unidade informacional equivalente.

---

# 39. Dívida informacional

Informação que não pode ser transmitida pode:

- envelhecer;
- tornar estados remotos obsoletos;
- exigir retransmissão;
- gerar inconsistências adicionais.

S3 é C1.

---

# 40. Teste S3

Se S1 e S2 passarem:

\[
K_{S1}
\approx
K_{S2}
\approx
K_{S3}.
\]

Falha além da margem:

\[
\boxed{
\text{refuta a universalidade declarada de }N3T_K.
}
\]

---

# PARTE VII — COMPRESSÃO

# 41. Modelo reduzido

Recebe apenas:

\[
\{
R_{eff},
\gamma_{manut},
t_{trans}
\}
\]

mais o \(K\) congelado.

---

# 42. Benchmark rico

\(M_{rich}\) poderá utilizar informações microscópicas adicionais.

---

# 43. Gate B0

Antes do teste retido, \(M_{rich}\) deverá demonstrar:

- competência;
- regularização adequada;
- estabilidade;
- ausência de tuning sobre o retido.

---

# 44. Custo da compressão

Define-se:

\[
\boxed{
\Delta_{comp}
=
E_H-E_R.
}
\]

---

# 45. \(\Delta_{comp}<0\)

Se B0 foi satisfeito e:

\[
E_H<E_R,
\]

o resultado favorece a representação reduzida naquele teste.

Isso não invalida retrospectivamente o benchmark.

---

# 46. Margem

Define-se:

\[
\boxed{
\delta_{compression}
=
\min(
\delta_{utilidade}^{comp},
\delta_{resolucao}^{comp}
).
}
\]

---

# 47. Falha da compressão

Se:

\[
\Delta_{comp}>
\delta_{compression},
\]

então:

\[
\boxed{
a\ suficiência macroscópica
de N3T_K é REFUTADA.
}
\]

---

# PARTE VIII — MARGEM DE TRANSPORTE

# 48. Definição

\[
\boxed{
\delta_{transport}
=
\min(
\delta_{utilidade},
\delta_{discriminacao}
).
}
\]

A regra de derivação é especificada antes do confirmatório.

Pilotos fornecem apenas seus insumos.

---

# PARTE IX — ESTABILIDADE DE \(t_{trans}\)

# 49. Gate U

Uma célula usada no teste primário deverá satisfazer:

\[
\boxed{
\frac{
SE(t_{trans})
}{
T_{dwell}-t_{trans}
}
\le
\epsilon_{trans}.
}
\]

---

# PARTE X — ROTA C2

# 50. Independência de N3F

Se N3T\(_K\) sobreviver:

\[
S1\rightarrow S2\rightarrow S3,
\]

poderá seguir diretamente para:

\[
\boxed{
C1\rightarrow C2.
}
\]

Esse caminho não depende da existência de uma forma universal \(F(x)\).

---

# 51. Família C2

Antes da execução confirmatória de S1 deverão estar definidos:

\[
\boxed{
\text{família C2 candidata}
}
\]

e:

\[
\boxed{
\text{regra de seleção}.
}
\]

Isso impede caça posterior ao substrato que melhor combine com os resultados.

---

# 52. Requisitos C2

O candidato deverá:

1. existir independentemente da HUMH;
2. não ter sido construído para gerar suas previsões;
3. possuir manutenção operacionalizável;
4. permitir medir entradas sem usar o desfecho previsto;
5. ser selecionado segundo regra independente do resultado C1.

---

# 53. Resultado C2 positivo

Se o \(K\) congelado transportar:

\[
\boxed{
N3T_K=\text{SUPORTADA [C2]}.
}
\]

---

# 54. Resultado C2 negativo

Com Gates satisfeitos:

\[
\boxed{
\text{falha em C2 refuta a extensão C1→C2 declarada.}
}
\]

---

# PARTE XI — N3F

# 55. Hipótese adicional

Somente depois do teste escalar pergunta-se se existe uma função:

\[
F(x)
\]

comum.

---

# 56. Predição

\[
\boxed{
F_{S1}(x)
\approx
F_{S2}(x)
\approx
F_{S3}(x).
}
\]

Esse é um compromisso muito mais forte que a invariância de \(K\).

---

# 57. Regra de seleção de \(F\)

Antes de qualquer dado humano deverão estar congelados:

- famílias candidatas;
- critério de seleção;
- penalização de complexidade;
- regra para declarar ausência de forma comum.

Nenhuma forma será escolhida por inspeção visual.

---

# 58. Falha de N3F

Se nenhuma forma comum sobreviver:

\[
\boxed{
N3F\text{ falha.}
}
\]

Mas:

\[
\boxed{
N3T_K
\text{ pode continuar válida e seguir para C2.}
}
\]

---

# 59. Consequência

A ausência de uma forma dinâmica universal significa:

> pode existir uma escala coletiva transportável sem existir uma trajetória temporal universal completa.

Esse é um resultado científico admissível.

---

# PARTE XII — CRONOGRAMA HUMANO

# 60. Decisão desta versão

Apesar de V7 ser logicamente independente de N3, esta versão escolhe deliberadamente:

\[
\boxed{
\text{não iniciar coleta humana
antes da conclusão do programa computacional prioritário.}
}
\]

---

# 61. Motivo

A suspensão temporária não é necessária para preservar validade estatística.

Ela é uma decisão de programa para:

1. testar primeiro formulações de baixo custo em C1;
2. abandonar hipóteses frágeis antes de humanos;
3. descobrir se existe previsão adicional que justifique novo desenho humano;
4. concentrar a etapa humana nas perguntas que sobreviverem à triagem computacional.

---

# 62. Custo reconhecido da decisão

Essa escolha possui custo explícito:

\[
\boxed{
\text{adiamento temporário da evidência Classe E.}
}
\]

Esse custo é aceito conscientemente nesta versão.

Não será apresentado como consequência inevitável da metodologia.

---

# PARTE XIII — V7

# 63. Identidade

V7 permanece um experimento humano Classe E independente.

Seu modelo original é:

\[
\boxed{
\Delta RT
=
\alpha+\beta\cdot lag
}
\]

com:

\[
\Delta RT=RT_2-RT_1.
\]

---

# 64. Hipóteses originais

V7 mantém suas próprias hipóteses H1/H2/H3.

Elas não serão alteradas para acomodar N3.

---

# 65. V7 não é V8

Se N3 produzir uma nova previsão humana:

\[
\boxed{
V7\ não\ será redesenhado.
}
\]

Será criado:

\[
\boxed{V8}.
\]

---

# 66. Relação V7–N1a

A relação normativa entre V7-H1 e N1a está congelada em `HUMH_Nucleo_1.9A.md`, seção A12.

V7-H1 é uma **consequência qualitativa Classe E** de N1a, com interpretação simétrica:

- CONVERGENTE;
- INCONCLUSIVO;
- DESCONFIRMATÓRIO.

Este programa N3 não pode alterar essa classificação.

---

# 67. Proibição de equivalência implícita

É proibido usar resultados de V7 ou V8 para promover retrospectivamente V7-H1 a teste quantitativo completo de:

\[
\eta(EH)
=
\frac{\omega}
{1+\iota_{obs}+\kappa EH}.
\]

Os critérios normativos de N1a permanecem os definidos em `HUMH_Nucleo_1.9A.md`.

---

# 68. Liberação de V7

Para fins de cronograma, a **triagem computacional C1 prioritária** é definida como a linha:

\[
S1_{CAL}
\rightarrow
S1_{VAL}
\rightarrow
S2
\rightarrow
S3
\rightarrow
\Delta_{comp}.
\]

V7 será liberado para coleta no **primeiro** dos seguintes eventos:

1. conclusão dessa linha C1 prioritária, com decisão sobre invariância escalar e compressão; ou
2. acionamento de qualquer regra terminal de parada que encerre antecipadamente essa linha.

Assim, por exemplo:

- falha confirmatória de K0 libera V7 imediatamente;
- falha terminal em S2 libera V7 imediatamente;
- falha terminal em S3 libera V7 imediatamente;
- falha terminal da suficiência de compressão libera V7 imediatamente.

As rotas posteriores:

\[
N3T_K\rightarrow C2
\]

e:

\[
N3T_K\rightarrow N3F
\]

**não mantêm V7 suspenso**. Elas podem continuar em paralelo depois da liberação.

Opcionalmente, poderá ser registrado antes da execução um prazo-teto puramente operacional para a triagem C1. Esse prazo, se adotado, será regra de cronograma e não critério científico; sua expiração também libera V7 sem alterar o status das hipóteses ainda não decididas.

---

# 69. Se houver falha ou parada computacional

Se qualquer regra terminal de parada for acionada:

\[
\boxed{
V7\ continua válido
para seus objetivos originais
e é liberado para coleta.
}
\]

Uma falha de N3T\(_K\), de compressão ou de outra etapa computacional não invalida o protocolo original de V7.

A falha de N3F também não altera V7.

## 69.1. Repilotagem técnica antes da coleta humana

Se o adiamento de V7 exigir nova validação técnica antes da coleta, será permitida uma **repilotagem estritamente técnica**.

Podem ser revalidados, por exemplo:

- disponibilidade e características operacionais do pool de recrutamento;
- precificação e viabilidade operacional;
- compatibilidade com versões atuais de navegador;
- deploy e infraestrutura;
- gravação e integridade dos dados;
- funcionamento técnico dos fluxos de participação.

Essa repilotagem **não constitui alteração do desenho confirmatório** desde que preserve integralmente:

- timing científico dos estímulos;
- cálculo de RT;
- número e distribuição de trials;
- randomização;
- lags;
- critérios de exclusão;
- variáveis primárias;
- hipóteses;
- plano de análise.

Qualquer mudança que possa alterar uma dessas propriedades deixa de ser manutenção técnica e deverá ser tratada como alteração substantiva de protocolo, com nova versão e registro apropriado antes da coleta.

A versão do código, o hash e o ambiente técnico validado serão registrados antes da coleta humana.

---

# PARTE XIV — V8

# 70. Condição de existência

V8 somente será criado se os computadores produzirem uma previsão humana:

- nova;
- não tautológica;
- quantitativa;
- congelável.

---

# 71. Exclusões

Não contam como previsão N3 humana:

\[
T^*
=
\frac{|\alpha|}{\beta}
\]

ou:

\[
x
=
lag\frac{\beta}{|\alpha|}
\]

seguido de:

\[
\frac{\Delta RT}{|\alpha|}
=
x-1.
\]

Ambos decorrem algebricamente do modelo linear.

---

# 72. Recurso humano

Uma eventual correspondência de:

\[
R_{eff}
\]

deverá ser funcionalmente justificada.

Não será assumido:

\[
R_{eff}^{human}=|\alpha|.
\]

---

# 73. Taxa humana

Também será necessária justificativa funcional independente para uma variável equivalente a:

\[
\gamma_{manut}.
\]

Compatibilidade dimensional não é suficiente.

---

# 74. Forma de V8

Se N3F sobreviver, a função candidata:

\[
F(x)
\]

será congelada antes do desenho confirmatório humano.

---

# 75. Poder de V8

A análise de poder será dirigida à:

\[
\boxed{
discriminação\ de\ forma
}
\]

e não apenas à detecção de uma inclinação.

---

# 76. Lags de V8

Somente após \(F(x)\) estar congelada serão escolhidos os lags que maximizam a distinção entre:

\[
F_{HUMH}
\]

e seus concorrentes.

---

# PARTE XV — ÁRVORE DE EXECUÇÃO

# 77. Etapa A

Congelar:

\[
\boxed{
HUMH_{1.9A}
=
N1a\land N1b\land N2.
}
\]

---

# 78. Etapa B

Congelar integralmente:

\[
S1,\quad S2,\quad S3
\]

e a família/regra C2.

---

# 79. Etapa C

Gerar hash do desenho.

---

# 80. Etapa D

Rodar:

\[
S1_{CAL}.
\]

---

# 81. Etapa E

Rodar:

\[
S1_{VAL}.
\]

Se falhar:

\[
\boxed{
PARAR\ N3T_K.
}
\]

---

# 82. Etapa F

Rodar S2.

Falha:

\[
\boxed{
PARAR\ N3T_K.
}
\]

---

# 83. Etapa G

Rodar S3.

Falha:

\[
\boxed{
REFUTAR\ a\ universalidade\
de\ N3T_K.
}
\]

---

# 84. Etapa H

Avaliar:

\[
\Delta_{comp}.
\]

Falha:

\[
\boxed{
REFUTAR\ suficiência\
macroscópica.
}
\]

---

# 85. Bifurcação computacional

Se N3T\(_K\) passar:

\[
\boxed{
\begin{array}{cc}
\text{Rota A} & \text{Rota B}\\
C2 & N3F
\end{array}
}
\]

---

# 86. Rota A

Testar transporte de:

\[
K_{N3}
\]

para C2.

Essa rota independe de N3F.

---

# 87. Rota B

Testar existência de:

\[
F(x)
\]

comum.

---

# 88. Após a triagem C1 prioritária

Ao concluir a linha C1 prioritária — ou ao acionar uma regra terminal de parada — V7 é liberado conforme §68.

As rotas C2 e N3F podem continuar em paralelo e não condicionam a liberação de V7.

Há três casos científicos principais.

---

# 89. Caso H-A — N3 fracassa

Executar V7 original.

Não criar V8.

---

# 90. Caso H-B — N3T\(_K\) passa, N3F falha

V7 original pode ser executado.

A rota C2 pode continuar.

Não criar V8 de curva universal.

---

# 91. Caso H-C — N3T\(_K\) e N3F passam

Executar V7 segundo seu protocolo original, se ainda for cientificamente desejado.

Separadamente, avaliar a criação de:

\[
V8
\]

para a previsão nova de N3.

---

# PARTE XVI — O QUE O COMPUTADOR PODE LEVAR A ABANDONAR

# 92. Falha K0

Abandonar:

\[
\boxed{
K_{N3}\text{ constante}
}
\]

na formulação atual.

---

# 93. Falha S2

Abandonar:

\[
\boxed{
\text{transportabilidade transversal de }K
}
\]

nesta versão.

---

# 94. Falha S3

Abandonar a universalidade declarada através de classes de recurso diferentes.

---

# 95. Falha de compressão

Abandonar a afirmação de que:

\[
\{
R_{eff},
\gamma_{manut},
t_{trans}
\}
\]

são aproximadamente suficientes.

---

# 96. Falha N3F

Abandonar a afirmação de forma dinâmica universal.

Não abandonar automaticamente N3T\(_K\).

---

# 97. Ausência de mapeamento humano

Se não existir operacionalização humana independente:

\[
\boxed{
não\ criar\ V8.
}
\]

---

# PARTE XVII — RESULTADOS POSSÍVEIS

# 98. N3T\(_K\) passa apenas em C1

Status:

\[
\boxed{
\text{COMPATÍVEL}.
}
\]

---

# 99. N3T\(_K\) transporta para C2

Status:

\[
\boxed{
\text{SUPORTADA [C2]}.
}
\]

---

# 100. Previsão humana confirmatória adequada

Status:

\[
\boxed{
\text{SUPORTADA [E]}.
}
\]

---

# 101. C2 e E positivos

O status continua SUPORTADA, mas o registro deve declarar:

\[
\boxed{
\text{SUPORTADA [C2+E]}.
}
\]

---

# PARTE XVIII — RESGATES PROIBIDOS

# 102. Núcleo 1.9-A

Os resgates proibidos de N1a/N1b/N2 são normativos e estão congelados em:

`HUMH_Nucleo_1.9A.md`, seção A13.

Este arquivo evolutivo não pode reduzir, ampliar ou reinterpretar essas travas.

---

# 103. N3T\(_K\)

Não será permitido:

- redesenhar S2/S3;
- criar \(K_{S2}\);
- criar \(K_{S3}\);
- redefinir UM;
- redefinir \(R_{eff}\);
- redefinir \(\gamma_{manut}\);
- mudar margens após resultados.

---

# 104. C2

Não será permitido procurar sucessivamente sistemas independentes até encontrar um que passe.

---

# 105. N3F

Não será permitido escolher \(F(x)\) após inspeção humana.

A regra de seleção deve estar congelada previamente.

---

# 106. Humanos

V7 não será retroativamente convertido em V8.

Uma nova pergunta exige um novo experimento.

---

# PARTE XIX — REGRA DE PARADA

# 107. Falha confirmatória

Quando uma etapa prevista para testar uma afirmação necessária de N3T\(_K\) falhar com poder e Gates adequados:

\[
\boxed{
PARAR.
}
\]

Não se prossegue para encontrar uma condição que “funcione melhor”.

---

# 108. Revisão posterior

Uma hipótese sucessora é permitida, mas deverá:

1. receber nova versão;
2. registrar a falha anterior;
3. alterar explicitamente a previsão;
4. poder falhar novamente.

---

# PARTE XX — PRINCÍPIO DE CRONOGRAMA

# 109. Computador primeiro não significa computador superior

A ordem:

\[
computador\rightarrow humano
\]

não representa hierarquia epistemológica.

Na verdade:

\[
E
\]

é mais independente que C1.

A ordem foi escolhida porque:

\[
\boxed{
C1\ é\ barato,\
rápido,\
controlável\
e\ adequado\
para\ eliminar\
formulações\ fracas.
}
\]

---

# 110. Objetivo e valor epistemológico da triagem computacional

O programa deve responder, antes da liberação inicialmente planejada de V7:

1. \(K\) é estável dentro de S1?
2. \(K\) transporta S1→S2→S3?
3. a compressão macroscópica é suficiente?
4. existe uma forma dinâmica comum?
5. existe caminho plausível para C2?
6. sobra alguma previsão realmente nova que justifique V8?

A triagem C1 possui:

\[
\boxed{
\text{forte poder eliminativo}
}
\]

e crédito positivo limitado a:

\[
\boxed{
\text{COMPATÍVEL}.
}
\]

Assim, um resultado negativo adequado pode refutar uma formulação congelada, enquanto um resultado positivo em C1 mostra sobrevivência e compatibilidade, mas não fornece suporte independente.

O benefício esperado de adiar V7 depende, portanto, de quanto a triagem computacional é capaz de **eliminar** formulações antes da etapa humana. Se a engenharia computacional se prolongar sem produzir decisões proporcionais ao custo do adiamento, o cronograma poderá ser revisto pelas regras explícitas do §68, sem alterar hipóteses, margens ou critérios científicos.

---

# 111. O computador não fornece suporte independente antecipadamente

Mesmo que todas as perguntas computacionais sejam positivas:

\[
\boxed{
C1\ continua\ sendo\ C1.
}
\]

O resultado positivo máximo dessa fase permanece:

\[
\boxed{
\text{COMPATÍVEL}.
}
\]

O programa determina quais formulações sobreviveram à triagem e quais merecem transporte para C2 e/ou avaliação humana independente.

---

# PARTE XXI — PRINCÍPIO FINAL

# 112. Núcleo

Congelar agora:

\[
\boxed{
HUMH_{1.9A}
=
N1a\land N1b\land N2.
}
\]

---

# 113. N3

Executar:

\[
\boxed{
S1_{CAL}
\rightarrow
S1_{VAL}
\rightarrow
S2
\rightarrow
S3.
}
\]

---

# 114. Depois

Se sobreviver:

\[
\boxed{
N3T_K\rightarrow C2
}
\]

independentemente de N3F.

E:

\[
\boxed{
N3T_K\rightarrow N3F
}
\]

para decidir se existe uma previsão funcional adicional.

---

# 115. Humanos

V7 é executado para seus objetivos próprios após:

- a conclusão da triagem C1 prioritária; ou
- o acionamento de uma regra terminal de parada; ou
- eventual prazo-teto operacional previamente registrado, se adotado.

V7 não precisa aguardar a conclusão das rotas C2 ou N3F.

Se houver uma previsão N3 humana adicional:

\[
\boxed{
V8.
}
\]

V8 permanece um experimento separado e nunca redefine retrospectivamente V7.

---

# 116. Regra final

Esta versão consolida a formulação “computador primeiro” por uma regra explícita:

\[
\boxed{
\text{rodar o computador primeiro
é uma escolha deliberada de cronograma,
não uma necessidade lógica.}
}
\]

O custo dessa escolha — adiar temporariamente evidência Classe E — é aceito conscientemente.

A vantagem buscada é igualmente explícita:

\[
\boxed{
\text{não levar aos humanos
uma formulação quantitativa
que o próprio programa
já conseguiu refutar.}
}
\]

Portanto, a ordem operacional da versão 2.1 é:

\[
\boxed{
congelar
\rightarrow
programar
\rightarrow
testar
\rightarrow
parar se falhar
\rightarrow
transportar
\rightarrow
somente então coletar humanos.
}
\]
