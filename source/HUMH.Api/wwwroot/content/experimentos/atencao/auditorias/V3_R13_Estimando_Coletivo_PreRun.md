# HUMH V3 — R13 · Estimando coletivo pré-run

**Status:** `PRE_CODE_COLLECTIVE_ESTIMAND_FEASIBILITY_ONLY`  
**Novo run científico:** não executado  
**Teoria / Núcleo 1.9-A / Spec v2.0.0:** não alterados

## Decisão

A R12 mostrou que o `CANAL_ETA` individual da Spec v2.0.0 recupera a taxa nativa constante da V3 por construção e, portanto, não oferece conteúdo independente suficiente para N1a neste substrato.

O Núcleo 1.9-A, porém, declara N1a como hipótese de dinâmica coletiva emergente e já define a divergência interobservador `D`. A R13 identificou uma ponte coletiva candidata, calculada apenas depois das interações e sem disponibilizar EH/D/atenção aos agentes:

`E_t = U_t(ciclo) / N_elegíveis`

`C_t = (D_t - D_{t+1}) / (E_t D_t)`

Ponte candidata para confronto fora da amostra:

`M0: D_t-D_{t+1} = E_t * theta * D_t + erro`

`M1: D_t-D_{t+1} = E_t * theta * D_t / (1 + lambda*EH_t) + erro`, com `lambda >= 0`.

Esta ponte é **auxiliar e não normativa**. O estimador primário individual já está congelado na definição de atenção; portanto, uso confirmatório da ponte coletiva requer uma **Spec experimental sucessora**, preservando integralmente a v2.0.0 e os resultados R9–R13. Não é necessária mudança da teoria neste ponto.

## Diagnóstico preservado dos dados já expostos

Nenhuma nova trajetória foi gerada. Nas 20 trajetórias exploratórias v0.2.1 já existentes, 328 ciclos tinham interação concluída e `D_t>0`. A cobertura observada de EH foi aproximadamente `0.743–0.999`, inadequada para cobrir prospectivamente toda a faixa congelada de N1a `[0.20,0.90]`.

Aplicada **depois da exposição aos dados**, a ponte coletiva selecionou `lambda=0` em CAL; `M0` e `M1` ficaram idênticos em VAL (RMSE ≈ `0.00218` na escala de `D_t-D_{t+1}`). Isso é `POST_HOC_DIAGNOSTIC_ONLY`, não refutação formal nem base para escolher outra forma que produza resultado favorável.

## Próximo passo obrigatório

Antes de qualquer novo run:

1. escrever uma Spec sucessora pré-código para o estimando coletivo;
2. gerar suporte prospectivo de EH dentro da faixa teórica sem usar outcomes;
3. preservar o adversarial N1b: EH comparável, D diferente;
4. congelar exposição C2C, tipos/capacidade, topologia, canal/ruído e CAL/VAL;
5. manter `NO_ATTENTION_IN_OBSERVER_RULE` e proibir leitura de EH pelos agentes;
6. não escolher parâmetros para apagar o diagnóstico `lambda=0` já observado.

A V3 permanece substrato C1. Um resultado positivo nesse sucessor pode atingir no máximo `COMPATÍVEL`; suporte independente continua exigindo C2/E conforme o Núcleo 1.9-A.
