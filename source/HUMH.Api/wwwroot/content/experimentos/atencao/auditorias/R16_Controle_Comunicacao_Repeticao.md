# HUMH — R16 · Comunicação, repetição e proveniência

**Estado:** `NATIVE_REFERENCE_ENGINEERING_ONLY`  
**Run científico:** não executado; não autorizado  
**Autoridade:** auditoria não normativa. Teoria, Núcleo 1.9-A, definição de atenção, Spec/Trace v2.0.0 e V3 histórica permanecem inalterados.

## Decisão

Uma mensagem repetida é uma nova ocorrência de interação e pode alterar o estado do observador, mas não constitui automaticamente uma nova evidência independente. Seu efeito depende do mecanismo de processamento, memória, estado e demais propriedades do receptor; não se impõe efeito zero nem mudança obrigatória. Sem comunicação ou outro acoplamento entre observadores não há atualização causada por aquela relação C2C. Atualização por fonte externa comum deve ser distinguida de convergência causada por comunicação.

No NormAN original, `receiveShare` atualiza a memória de recência inclusive para evidência já conhecida; a evidência duplicada não é reincorporada ao posterior. Assim, repetição pode afetar o estado de memória e compartilhamentos futuros, embora não altere imediatamente a crença nesse ramo. Isso é uma propriedade nativa do modelo, não uma regra universal da HUMH. O cenário de comunicação sem investigação adicional é descrito explicitamente no artigo de 2025, *Capturing Argument in Agent-Based Models*; não deve ser atribuído indistintamente ao artigo original de 2023.

## Verificação executada

Foi criado um verificador Python de inferência exata para o mundo Vole a partir das CPTs originais, sem alterar seus valores. Ele preserva a identidade das evidências, registra ocorrências repetidas e separa fonte externa de comunicação dirigida. O fixture de duas entidades e cinco mensagens compara ausência de comunicação, fonte comum e troca de evidências; não representa o modelo NetLogo completo. Uma interface sintética comprova que uma segunda recepção pode ter delta não zero sem codificar uma lei HUMH.

**12 testes de engenharia aprovados, nenhuma falha.** Incluem inferência e normalização, referência racional independente, ausência de comunicação, não duplicação de evidência, recência, proveniência do emissor, arestas dirigidas, atualização zero válida e repetição capaz de produzir mudança. Não foram executados NetLogo, R, bnlearn ou gRain. Não houve reprodução dos resultados dos autores nem inferência científica sobre N1a/N1b/N2.

## Integridade e continuidade

Fonte externa: `NormAN-framework/base-model`, commit `6ad82d26fa9d3c32c9ff4db5a89bba2618c74283`, arquivo `base-model.nlogo`, blob Git SHA-1 `43309c80a2d2480502d670849bfe79ade0b8fdfd`. Trecho local Vole SHA-256: `a260037fd92324adff74624611faeff637d4c8f49e9291c0efe05b16a07c6e91`. Licença original CC BY-NC 4.0, preservada com atribuição.

Pacote de auditoria: `HUMH_R16_Controle_Comunicacao.zip`  
SHA-256: `4378e523e417dd9cb3842ffa00a656e1971be3bd6cd480c56f4ae592ab580805`.

O pacote contém relatório, código, trecho original atribuído, testes, fixture JSON e hashes; não é publicado integralmente neste commit. NormAN permanece candidato externo, sem classificação C2 concedida. A V3 continua instrumento C1. Nenhuma nova fórmula de repetição, parâmetro HUMH, Gate ou estimando confirmatório foi criado. A próxima decisão deve estabelecer se há processamento de repetição canonicamente especificado ou independentemente fundamentado que possa ser mapeado sem alterar a microdinâmica para produzir a previsão. A1a/A1b permanecem sem nova classificação; A2 não autorizado. Os resultados e limitações de R9–R15 permanecem preservados.
