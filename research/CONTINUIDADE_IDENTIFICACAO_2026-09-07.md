# HUMH — Continuidade: identificação paramétrica em V3 e NormAN

Data: 2026-09-07. Status: `NON_NORMATIVE_RESEARCH_CONTINUITY`. Este documento registra a orientação expressa pelo pesquisador e uma análise de identificabilidade. Não altera a teoria, o núcleo 1.9-A, a Spec/Trace A0/A1 v2.0.0, os protocolos históricos ou qualquer resultado. Não autoriza coleta científica, não cria Gates ou parâmetros teóricos e não constitui R20.

## 1. Objetivo que deve orientar novas conversas

A HUMH é uma metateoria funcional. O objetivo do programa computacional único é operacionalizar, estimar e testar seus parâmetros e previsões em substratos adequados, inclusive modelos que não foram escritos na linguagem da HUMH. V3 e NormAN foram ambos cogitados. A tarefa não é escolher um simulador que converge, exigir que ele já contenha κ ou acrescentar mecanismos para produzir a previsão. É descobrir que grandezas são observáveis, que parâmetros ou combinações são identificáveis, que intervenções são necessárias e que previsões podem ser confrontadas independentemente.

A V3 permanece candidata C1, não deve ser descartada pelo bloqueio de uma configuração anterior. NormAN permanece candidato externo independente, sem promoção automática a C2 por um port JavaScript. A escolha deve decorrer de mecanismo, identificação e protocolo prospectivo, não da direção dos resultados. Preservar resultados negativos e inconclusivos. Não iniciar nova sequência de demonstrações de convergência ou renomear o experimento único para contornar bloqueios.

A V3 histórica também contém Deffuant e Hegselmann–Krause (HK) como modelos comparadores. Portanto, a comparação do programa não se limita a V3 versus NormAN: é necessário distinguir o mecanismo HUMH implementado na V3, os comparadores Deffuant/HK e o substrato externo NormAN. A presença de comparadores não torna a V3 um substrato independente da HUMH nem valida automaticamente a metateoria.

## 2. Autoridade e referentes

- Teoria canônica: SHA-256 `3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b`.
- Núcleo `HUMH_1.9A`: SHA-256 `baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b`, arquivo `source/HUMH.Api/wwwroot/content/HUMH_Nucleo_1.9A.md`.
- Definição de atenção v1.0.0: SHA-256 `3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a`.
- A0/A1 v2.0.0: somente `HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md` e `HUMH_A0_A1_Traceabilidade_v2.0.0.json` têm autoridade normativa nesta versão. Seus referentes devem ser verificados antes de uma implementação ou revisão.
- R12: `RELATORIO_R12.md`, auditoria da V3 v0.2.1, `AUDIT_CLOSED_WITH_SCIENTIFIC_BLOCKERS`.
- V3 histórica: `source/HUMH.Api/wwwroot/V3_social.html`, blob `e0aed20ef398fc05003987a731cf9c042b62f369`. A extensão v0.2.1 é distinta da V3 histórica.
- NormAN: `NormAN-framework/base-model`, commit `6ad82d26fa9d3c32c9ff4db5a89bba2618c74283`, `base-model.nlogo`, Git blob `43309c80a2d2480502d670849bfe79ade0b8fdfd`. Fonte sob CC BY-NC 4.0.
- R18 original: `research/norman-native-r18/protocol.json` no commit `f9716c2d1a5639f5cc6fea20f5fd637461c962f1`. Reprodução técnica, sem requisito de convergência ou ajuste de κ. A falha de execução nativa não foi reparada pelo port JS; não declarar equivalência nativa sem confronto independente.

## 3. O que cada substrato oferece

### V3 e seus comparadores

A V3 histórica é uma página comparativa de HUMH, Deffuant e Hegselmann–Krause. A regra HUMH é uma atualização em direção a média ponderada de sinais, com taxa por tipo. Deffuant usa confiança limitada por pares e parâmetro μ; HK usa média de agentes elegíveis segundo limiar ε, aplicada de forma síncrona. O código histórico também oferece heterogeneidade compartilhada e parâmetros específicos por modelo. É necessário auditar as adaptações efetivamente implementadas antes de chamá-las de versões canônicas independentes de Deffuant ou HK. Os rótulos de superioridade, equivalência e validação científica presentes na interface histórica não são, por si, evidência confirmatória da HUMH.

A extensão V3 v0.2.1 acrescenta instrumentação, filas, capacidade, deadlines e canais. A R12 verificou que a inclinação individual recupera a taxa nativa constante; portanto esse estimador não identifica contribuição independente de EH. O matching de A1b é instrumentalmente viável, mas o conteúdo coletivo independente ainda não está estabelecido. Não interpretar quantidade de updates, inclinação nativa ou resultado exploratório como confirmação. Verificar na fonte da extensão quais comparadores e componentes históricos foram preservados antes de atribuir-lhe integralmente a interface V3 histórica.

### NormAN

O modelo original usa inferência bayesiana sobre evidências, comunicação entre agentes e memória de recência. Evidência conhecida pode ser recebida novamente e atualizar recência sem recalcular o posterior. O port R18 reproduz a configuração Vole em JS com inferência exata, mas não o fluxo aleatório bit a bit nem toda a implementação NetLogo/R. Não contém atenção HUMH, κ, ω ou ι_obs explicitamente. Isso não exclui uma ponte metateórica; exige estabelecê-la. O posterior de outro agente, o consenso e o posterior completo do mundo não podem ser declarados automaticamente `p_target` da A1.

### Papel dos comparadores

Deffuant e HK são alternativas mecanísticas úteis para verificar se uma previsão atribuída à HUMH também decorre de regras clássicas de interação. Não presumir que qualquer um deles seja um padrão-ouro universal, que menor EH represente verdade externa ou que ausência de diferença estatisticamente significativa prove equivalência. Comparações devem usar medidas, condições, parâmetros e critérios prospectivos adequados à pergunta. A implementação comparativa original pode continuar servindo como referência de engenharia, sem promover automaticamente seus resultados ou rótulos históricos.

## 4. Resultado analítico de identificabilidade — não é estimação empírica

A forma basal canônica é η=ω/(1+ι+κh), com h=EH. Se η e h forem observáveis e o alvo/drive for conhecido independentemente, então:

`1/η = a + b h`, com `a=(1+ι)/ω` e `b=κ/ω`.

Com variação informativa de h, no máximo a e b são identificáveis a partir dessa relação isolada. A transformação `(ω, 1+ι, κ) -> (cω, c(1+ι), cκ)`, para c>0 admissível, deixa todas as taxas iguais. Logo, nenhum número de observações perfeitas da mesma relação separa automaticamente os três parâmetros. Com h constante, apenas a combinação `a+b h` é identificável. Restrições de domínio podem limitar os valores admissíveis, mas não fornecem por si uma normalização de escala.

O quociente `b/a=κ/(1+ι)` e a redução relativa `s=1-η(h_b)/η(h_a)=b(h_b-h_a)/(a+b h_b)` são invariantes à escala. Podem servir como diagnósticos de identificação e relevância sem estimar κ absoluto. Não substituir a hipótese congelada κ>0, suas margens ou o contrato de N2 por um novo parâmetro. Se ω for conhecido por uma calibração independente e justificada, então `ι=ωa-1` e `κ=ωb`; se a escala permanecer desconhecida, reportar apenas combinações identificáveis. Uma calibração basal não pode ser inventada ou inferida da mesma taxa que se pretende decompor.

## 5. Matriz de trabalho

| Alvo | V3 / Deffuant / HK | NormAN | Identificação/pendência |
| --- | --- | --- | --- |
| A0, A_i=U_i/D_i | Instrumento e contadores já implementados na extensão v0.2.1; verificar sua aplicação aos comparadores | Necessita contrato de demandas exógenas, conclusões e deadlines; mensagens nativas são endógenas | Separar demanda, oportunidade, capacidade e taxa de crença; respeitar A0 e ANBC0 |
| ω, ι_obs | Taxas e resistências nativas recuperáveis conforme a implementação, mas não equivalem automaticamente aos parâmetros canônicos | Posteriores e respostas a evidências podem caracterizar dinâmica basal efetiva | Definir alvo/drive e escala independente; não declarar parâmetros individuais sem identificação |
| κ / N1a | Inclinação local HUMH constante na V3 auditada; examinar alternativas Deffuant/HK sem inserir EH nas regras | Inferência bayesiana permite caracterizar resposta, mas não há κ nativo | Definir dinâmica coletiva emergente e previsão independente; comparar M0 κ=0 com M1 e testar fora da amostra |
| N1b | Comparadores podem gerar distribuições distintas com mesma EH; controlar estado e história | Evidências compartilhadas podem produzir estados semelhantes em média com diferentes distribuições individuais | Comparar suficiência de EH com alternativa pré-especificada, conforme núcleo 1.9-A |
| N2 | Tipos, limiares e resistências nativas podem fornecer condições, não identificação canônica automática | Evidências e histórico podem alterar resposta por razões probabilísticas distintas | Estimar separadamente componentes do observador e estruturais e prever células cruzadas sem reajuste |
| A1b | Matching de atenção viável na R12; outcome independente pendente; não presumir equivalência da instrumentação entre modelos | Instrumento A0 ainda não implementado | Mesma Abar, DA distinto, demanda/estado/topologia/composição preservados; conteúdo coletivo e critérios prospectivos |
| Mudança A→B e N3T | Exigem desenho próprio compatível com a hipótese selecionada | O mundo pode ser manipulado apenas por protocolo explícito | Não inserir mudança ou memória para garantir convergência; não abrir A2 nem substituir N3T-K0 |

## 6. Próxima ação do programa único

Primeiro, auditar os bytes atuais da extensão V3 v0.2.1, dos comparadores Deffuant/HK e do port NormAN, recuperando fontes completas e seus manifestos. Construir mapa código→observável→referente canônico, marcando lacunas e distinguindo instrumentação de hipótese. Depois, testar identificabilidade estrutural e recuperação sintética sem usar outcomes científicos para escolher parâmetros. Para NormAN, caracterizar a inferência e a identidade de evidências antes de decidir uma ponte para o alvo basal; para V3, aproveitar o instrumento A0 já existente sem promover sua taxa nativa a κ. Os comparadores devem permitir verificar explicações alternativas, não ser tratados como prova automática de superioridade ou confirmação.

A próxima decisão de desenho deve ser prospectiva: verificar se algum substrato permite dinâmica coletiva independente, contraste informativo de EH, estimação de resistência observacional e estrutural e predição retida. Se for necessária uma nova operacionalização, registrar exatamente o que ela acrescenta e revisar a Spec/Trace por sua regra-mãe antes de nova coleta. Não criar um novo Gate científico por conveniência. Manter A1a como demonstração de mecanismo na construção congelada que falhou ANBC0; A1b só avança com seu conteúdo independente. Preservar A2 não autorizado e a classificação histórica de N3T-K0.

## 7. Uso em novas conversas

Ao retomar o projeto, começar por este objetivo e pelos substratos V3/NormAN, incluindo os comparadores Deffuant/HK, consultar as fontes atuais e os documentos normativos, e não repetir a sequência de reproduções de convergência como se fosse o objetivo final. Esta nota é memória de continuidade do projeto, não uma atualização forçada da Memória automática do ChatGPT. Não contém novos resultados empíricos nem substitui artefatos normativos.