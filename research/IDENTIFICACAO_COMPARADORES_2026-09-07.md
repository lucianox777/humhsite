# HUMH — Comparadores: identificação, caminho simples primeiro

Data: 2026-09-07. Status: `NON_NORMATIVE_ENGINEERING_ANALYTIC_ONLY`. Nenhum novo run científico, hipótese, Gate, parâmetro HUMH, alteração normativa ou classificação confirmatória. Não é uma nova versão R.

## Continuidade e decisão

O objetivo é estimar e testar parâmetros e previsões da HUMH como metateoria em substratos adequados, não apenas reproduzir convergência. V3/HUMH, Deffuant, HK e NormAN continuam no programa. A R15 já decidiu não promover a ponte coletiva R13/R14 a estimando confirmatório na V3 atual; preservar esse fechamento. A extensão v0.2.1 permanece C1 e seu instrumento de atenção não é evidência independente. NormAN permanece candidato externo, sem C2 automático.

O caminho mais simples é caracterizar primeiro o Deffuant homogêneo da V3 histórica, depois o HK. Trata-se de ordenação técnica, não seleção por resultado. Antes de alegar independência, confrontar cada implementação com a versão original escolhida.

## Fontes e escopo

- V3 histórica: `source/HUMH.Api/wwwroot/V3_social.html`, blob Git `e0aed20ef398fc05003987a731cf9c042b62f369`.
- R12: `source/HUMH.Api/wwwroot/content/experimentos/atencao/auditorias/V3_R12_Auditoria_PreRun.md`, blob `a95e27626488a28eb1c1f6a6572f3ccb66c77cf8`.
- R14: `source/HUMH.Api/wwwroot/content/experimentos/atencao/auditorias/V3_R14_Sucessora_PreCodigo.md`, blob `052a66dfc0212f93d249628ee3912ab50ab5a116`.
- R15: `source/HUMH.Api/wwwroot/content/experimentos/atencao/auditorias/V3_R15_Decisao_Substrato.md`, blob `20ced3b824a119aeea3574ecf48a2757ff06f5af`.
- Núcleo 1.9-A e os dois artefatos normativos A0/A1 v2.0.0 mantêm toda autoridade. A fonte integral da extensão v0.2.1 não foi recuperada nesta sessão; não declarar nova auditoria byte a byte desse motor.

## Conclusões algébricas

Deffuant histórico: um receptor seleciona vizinho com `|p_j-p_i|<epsilon` e atualiza unilateralmente `p_i^+=p_i+mu_eff(p_j-p_i)`. No modo homogêneo, `mu_eff=mu`; no modo heterogêneo, `mu_eff=mu*influence_j*(1-resistance_i)`. Um evento aceito com drive não nulo permite recuperar o coeficiente nativo. Os fatores do produto não são separáveis sem informação independente. Decisões finitas de elegibilidade delimitam ε, mas não garantem identificação pontual. Ausência de movimento não é necessariamente rejeição.

HK histórico: atualização síncrona pela média de si próprio e vizinhos com distância `<=epsilon`, ponderada por influência quando heterogêneo. Não existe μ livre nessa regra. A razão mudança/drive não constitui estimação independente de uma taxa basal. ε pode ser apenas parcialmente identificado, e pesos comuns são invariantes a escala.

Em ambos, no domínio interior e com decisões/sorteios preservados, uma translação comum conserva diferenças e dinâmica de D, embora possa alterar EH. Esse adversário reforça o cuidado da R14/R15, sem refutar automaticamente N1a. Nenhum coeficiente nativo é κ, ω ou ι_obs por renomeação. A relação basal isolada identifica combinações de escala, conforme parecer anterior; uma ponte coletiva e uma âncora independente continuam necessárias quando o alvo científico requer os parâmetros separados.

## Próximo ato permitido

Instrumentar sem modificar a regra nativa: registrar receptor, fonte, decisão de elegibilidade, estado antes/depois, drive, coeficiente, ordem lógica e parâmetros originais. Confirmar fidelidade da versão independente de Deffuant antes de qualquer alegação C2; usar HK como comparador mecanístico. Não inserir EH, atenção ou pooling para produzir a previsão. Não substituir a atenção A_i=U_i/D_i por velocidade, frequência de mensagem ou coeficiente de crença. A1b exige seu outcome independente e congelamento prospectivo. A2 não autorizado; N3T-K0_CONSTANT e todos os resultados históricos preservados.

## Verificação local

Pacote `HUMH_Comparadores_Identificacao_20260907.zip` foi gerado localmente com parecer, verificador Python/SymPy, JSON e manifesto. Foram aprovados 21 testes algébricos; não foram executadas trajetórias científicas. SHA-256 do pacote local: `90e96a04f275b7252bf716187b4165a3acc508cf05a96390eb9c751129ed9dc2`. O pacote não está incorporado ao repositório por este registro. Status final: `NATIVE_PARAMETERS_RECOVERABLE_NOT_HUMH_IDENTIFIED`.