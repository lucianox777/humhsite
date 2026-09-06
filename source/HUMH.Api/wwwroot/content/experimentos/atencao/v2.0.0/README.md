# HUMH A0/A1 v2.0.0 — publicação autocontida mínima

Versão v2.0.0 regenerada antes de publicação.

## Novo fechamento conceitual

A microdinâmica basal foi congelada a partir da teoria canônica:

`eta0_i(p) = omega_i / (1 + iota_obs_i + kappa*EH(p))`

`p_post = p_pre + eta0_i(p_pre)*(p_target-p_pre)`

Uma demanda concluída validamente executa exatamente uma atualização basal.
Uma demanda não concluída ou expirada executa zero atualização.

## Resultado de ANBC0

A construção reduz localmente a:

`Delta_p = S * G`

onde `S` é o indicador de conclusão válida e `A_i` é a média de `S` sobre as demandas.
Logo, a forma `eta(A,p)=A_i*eta0_i(p)` é derivacional nesta implementação.

Status:

`ANBC0 = FAIL_DERIVATIONAL`

`A1a = MECHANISM_DEMONSTRATION_ONLY [C1]`

`ASEP0_CONFIRMATORY = NOT_AUTHORIZED`

Isso não refuta H-A1S nem a HUMH; apenas impede usar esta simulação como confirmação
independente da separabilidade.

## Próximo bloqueio

Auditar se A1b possui conteúdo coletivo próprio não redutível à identidade local de A1a.
Depois, congelar os parâmetros numéricos restantes.

`scientific_run_authorized = false`
