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

## Auditoria A1b em curso

A divergência interobservador canônica

`D = (1/N) * sum_i |p_i - p_bar|`

fica congelada **somente como candidato primário para auditoria derivacional**.
A análise pré-numérica encontrou um padrão suficiente em que o efeito é forçado
(homogeneidade basal, mesmo estado inicial/alvo e `0 < eta0 < 1`), mas esse padrão não é
uma identidade global de todo o espaço ainda admissível.

Status:

`ADIST0.DERIVATIONAL_CONTENT_AUDIT_PRENUMERIC = CONDITIONAL_NOT_GLOBALLY_FORCED`

`ADIST0.DERIVATIONAL_CONTENT_AUDIT_FINAL = PENDING_BASAL_REGIME_AND_ASSIGNMENT_RULE`

Próximo bloqueio: congelar prospectivamente o regime basal do observador e a regra
exógena de atribuição de atenção; depois repetir a auditoria final. É proibido trocar
`D` por outro outcome apenas para obter uma classificação discriminativa.

`scientific_run_authorized = false`
