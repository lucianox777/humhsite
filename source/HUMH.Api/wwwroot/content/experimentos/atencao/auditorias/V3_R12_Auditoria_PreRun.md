# HUMH — V3 R12: auditoria pré-run da extensão quantitativa

**Natureza:** registro auxiliar de pesquisa e auditoria, não normativo. **Data:** 2026-09-07. **Estado:** `AUDIT_CLOSED_WITH_SCIENTIFIC_BLOCKERS`; `SCIENTIFIC_RUN_NOT_AUTHORIZED`.

## Referentes

A V3 histórica permanece em `source/HUMH.Api/wwwroot/V3_social.html`, blob `e0aed20ef398fc05003987a731cf9c042b62f369`. A extensão v0.2.1 é C1 e não reproduz a V3 byte a byte. Motor auditado SHA-256 `fe8e71308ae638dbf6f0b05be47a2f313888123d616ca9bb53d8cf16865ec039`; HTML `766f25e179882131af9d01067e9916c3346a46f1a11c388624994cc5923d2839`. Pacote original SHA-256 `fef8b7c2402d2240dab507497db0d3de07dcc2b0dd606ddcd04c0053c432fccd`.

Referentes congelados: definição de atenção `3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a`; teoria `3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b`; núcleo 1.9-A `baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b`; Spec R9 `82a1db0645de24b9d90a98c7b78301677c31a64f364b4525efe0333e053c0adb`; Trace R9 `83282751f3252b224e4045fda08bf022e459321db2acb31e0bb6d174abc9ccdd`.

Relatório completo R12 SHA-256 `b6b4516a45a81b5f13ab0584fc583c5a7bd2c6ee6c9bedc5fd9ff076fe0da6e9`. Pacote de auditoria `HUMH_V3_Auditoria_R12.zip` SHA-256 `df7959151739030c89d4acc174f60a3c75f414f170aa5a49d189fd353a957147`. O pacote contém relatório, verificadores e resultados exclusivamente instrumentais/de auditoria. Nenhum dado bruto de execução foi publicado neste registro.

## Fechamento

A correção de elegibilidade é consistente com o controle local: ausência de fonte C2C não produz demanda nem atualização C2C; A fica indefinida quando D=0. Isso não impede atualizações por causas externas e não confunde ausência de acoplamento com correlação estatística zero. Ruído, capacidade e atenção permanecem conceitualmente distintos. A alteração da definição canônica de demanda não foi presumida.

A regra nativa da extensão tem `r_i=changeRate*(1-resistance_i)` e `delta_i=r_i*(target_i-p_i)`. O estimador por evento recupera essa taxa. A reauditoria das 20 trajetórias existentes encontrou 614 inclinações identificadas, todas iguais às taxas nativas dentro de erro numérico; 186 não identificadas. Isso é identidade mecanística, não evidência independente de κ>0. O drive coletivo atual soma drives de atualizações já realizadas, de modo que a projeção M0/M1 não é um estimando confirmatório independente. Preserva-se o resultado anterior de lambda=0 e RMSE VAL igual nos dois modelos, sem reclassificar N1a.

Os quatro pares A1b existentes falharam no matching de atenção efetiva. O testemunho instrumental já documentado no R8 foi reexecutado apenas com filas e contadores da v0.2.1: 24 configurações, sem crenças, sinais, EH ou outcomes. Para N=40,W=40, capacidade=1, trabalho=2 e deadline=1, o padrão uniforme 0/2 e o heterogêneo 0/4 para metade HIGH e 0/0 para metade LOW produzem D=1600, U=800 e Abar=0.5 em ambos; DA=0 versus 0.5. Oportunidades, trabalho e conclusões coincidem por ciclo. Isso demonstra viabilidade estrutural, não seleciona novos parâmetros científicos nem estabelece conteúdo independente de A1b. O fechamento derivacional R9 permanece intacto.

## Próxima decisão

Antes de outro run científico, explicitar na Spec/Trace existentes o alvo e o estimando coletivo compatíveis com o núcleo, a população elegível, a distinção entre sinais exógenos e conteúdo endógeno do feedback, os comparadores nativos e o controle de tipos/topologia. A1a precisa superar ANBC0 sem identidade de thinning; A1b precisa de matching instrumental prospectivo e conteúdo discriminativo adicional. Não ajustar parâmetros para obter um resultado desejado. Se o substrato não permitir identificar a previsão, registrar incompatibilidade/inconclusividade do desenho e avaliar um substrato independente por regra prospectiva.

A teoria, a V3 histórica, o núcleo 1.9-A e os dois artefatos normativos não foram alterados. Nenhuma hipótese foi confirmada ou refutada nesta auditoria; A2 continua não autorizado. O registro não é um terceiro artefato normativo e não autoriza uma nova execução científica.