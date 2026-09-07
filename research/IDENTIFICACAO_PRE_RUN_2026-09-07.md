# HUMH — Parecer de identificabilidade pré-run

Data: 2026-09-07. Status: `NON_NORMATIVE_IDENTIFICATION_REVIEW`. Este registro complementa `research/CONTINUIDADE_IDENTIFICACAO_2026-09-07.md`. Não é R20, não altera teoria, núcleo 1.9-A, Spec/Trace v2.0.0 ou resultados históricos, não abre A2 e não autoriza execução científica.

## Objetivo e escopo

A HUMH é uma metateoria. O programa computacional único deve operacionalizar, estimar e testar seus parâmetros e previsões em substratos adequados, incluindo modelos que não usam a terminologia HUMH. Considerar V3, seus comparadores Deffuant/HK e NormAN, sem exigir que contenham κ explicitamente e sem introduzir a previsão desejada nas regras. A V3 permanece C1; a presença de comparadores não torna a implementação independente. O port NormAN não equivale automaticamente à execução nativa.

## Fontes e limites

V3 histórica: `source/HUMH.Api/wwwroot/V3_social.html`, blob `e0aed20ef398fc05003987a731cf9c042b62f369`. Foram verificadas as rotinas históricas de atualização HUMH, Deffuant e HK. R12: extensão v0.2.1, motor SHA-256 `fe8e71308ae638dbf6f0b05be47a2f313888123d616ca9bb53d8cf16865ec039`; seus achados são herdados, pois os bytes integrais da extensão não foram recuperados nesta sessão. R14: `source/HUMH.Api/wwwroot/content/experimentos/atencao/auditorias/V3_R14_Sucessora_PreCodigo.md`, proposta não congelada. NormAN: commit `6ad82d26fa9d3c32c9ff4db5a89bba2618c74283`, blob `43309c80a2d2480502d670849bfe79ade0b8fdfd`, CC BY-NC 4.0. Permanecem autoridades o núcleo 1.9-A e os dois artefatos normativos A0/A1 v2.0.0.

Referências externas: Deffuant et al. (2000), *Mixing beliefs among interacting agents*, DOI 10.1142/S0219525900000078; Hegselmann e Krause (2002), *Opinion dynamics and bounded confidence: models, analysis and simulation*, JASSS 5(3), artigo 2, https://www.jasss.org/5/3/2.html. A linhagem publicada não homologa automaticamente as adaptações da V3.

## Identificação estrutural

Para h=EH, η=ω/(1+ι_obs+κh) implica 1/η=a+bh, a=(1+ι_obs)/ω e b=κ/ω. O jacobiano tem posto máximo 2; com h constante, posto 1. A transformação (ω,1+ι_obs,κ)→c(ω,1+ι_obs,κ), para c>0 admissível, preserva as taxas. Logo, a relação isolada não separa os três parâmetros. Com escala ω conhecida independentemente e por fundamento justificado, ι_obs=ωa−1 e κ=ωb. Sem escala, ρ=b/a=κ/(1+ι_obs) e s=ρ(h_b−h_a)/(1+ρh_b) são identificáveis em condições apropriadas. A faixa e o efeito mínimo históricos de N1a, 0,20–0,90 e 5%, correspondem a ρ_min=10/131. Isto apenas reexpressa a margem congelada; não cria outro parâmetro científico ou critério.

## Mecanismos e adversários

A V3 histórica usa alvo ponderado e taxa local por tipo. R12 mostrou que a inclinação local da extensão recupera exatamente essa taxa, não κ independente. O Deffuant histórico usa um receptor, vizinho elegível por ε e atualização unilateral com μ, influência da fonte e resistência do receptor. O HK histórico utiliza média síncrona de si e vizinhos elegíveis. São adaptações; seus parâmetros nativos não equivalem automaticamente a resistências canônicas. O NormAN recalcula posteriores bayesianos para evidência nova e atualiza recência também para repetições; não contém κ, ω, ι_obs ou atenção HUMH explicitamente.

A R14 já registrou o adversário de translação: no interior de regras que dependem apenas de diferenças, F(p+c1)=F(p)+c1. Assim, D pode conservar toda sua trajetória enquanto EH muda. O testemunho matemático foi reproduzido para a regra ponderada e estendido aos comparadores históricos sob elegibilidade preservada. Não se declara invariância global diante de clipping, bordas ou outros termos. EH também não determina D: (1/2,1/2,1/2,1/2) e (0,0,1,1) têm EH=1, mas D=0 e D=1/2. Esses fatos são adversários de suficiência, não refutações científicas automáticas de N1a/N1b.

R13/R14 preservam a ponte fenomenológica Y=D_t−D_{t+1}, E=U_cycle/N_eligible e C=Y/(E D_t). E é densidade auxiliar de conclusões, não atenção. Sua utilização realizada torna a projeção condicional, não previsão prospectiva a partir apenas de inputs exógenos. A ponte permanece candidata, não substitui a definição canônica.

## Próxima decisão do programa único

Priorizar a revisão de suficiência da ponte R14 e a recuperação dos bytes da extensão V3 v0.2.1. Verificar estado/drive coletivo independente, informação preditiva disponível antes do outcome, suporte de EH, escala identificável e controles de composição, topologia, exposição e conteúdo. Se não houver identificação adequada, registrar o limite da V3 e avaliar prospectivamente NormAN e implementações independentes Deffuant/HK sem reprogramar a previsão. A1b permanece condicionado ao outcome da linhagem, matching, margens, amostra e critérios prospectivos exigidos em ADIST0. N2 requer estimação separada de componentes e previsão cruzada sem reajuste. Preservar ANBC0, A2 não autorizado e N3T-K0 histórico.

Um verificador local, `verify_identification.py`, aprovou 14 testes de álgebra simbólica e aritmética exata, incluindo posto do jacobiano, simetria de escala, recuperação de combinações, margem histórica, translação e distinção EH/D. Nenhum simulador científico foi executado. Constantes ilustrativas não são estimativas HUMH. O pacote completo de parecer e verificador foi entregue na conversa de 2026-09-07 sob o nome `HUMH_Identificacao_PreRun_20260907.zip`; este registro não afirma sua publicação como arquivo no repositório.