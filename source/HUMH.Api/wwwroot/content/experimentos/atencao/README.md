# HUMH — Experimentos de Atenção

`v2.0.0/` é a árvore corrente A0/A1 pré-publicação. A especificação e a rastreabilidade dessa árvore são os únicos artefatos normativos do experimento; este README é apenas índice e registro de pesquisa.

- A0 ainda não executado; `ANBC0 = FAIL_DERIVATIONAL`; A1a = `MECHANISM_DEMONSTRATION_ONLY [C1]`.
- R9: A1b não possui conteúdo confirmatório independente suficiente no gerador corrente. O candidato D e o testemunho R8 permanecem documentados como auditoria/demonstração, não como confirmação.
- `D_i(W)=W`, `B=1`, workload homogêneo `K_C=2` e `L_A=1`; regime basal homogêneo e barreira síncrona pertencem à construção atual.
- Basal numérico reduzido a `eta_EH0` e `lambda_state`; nenhuma escolha de novos números pode resgatar a classificação científica da construção atual.
- `SCIENTIFIC_RUN_NOT_AUTHORIZED`; A2 não autorizado.

A teoria exibida pelo site permanece `../../teoria.md`; a cópia em `v2.0.0/02_dependencias/` é a dependência canônica hash-locked. O auditor de schedules permanece auxiliar e não autoriza inferência científica.

## Pesquisa prospectiva de substrato independente — R10

**Status:** `CANDIDATE_RESEARCH_ONLY`. Não é seleção confirmatória, alteração do núcleo, mudança de microdinâmica ou autorização de execução. O usuário aprovou continuar buscando um experimento computacional único capaz de confrontar a teoria independentemente. A decisão de desenho será incorporada à Spec e à Trace existentes somente depois de sua auditoria.

### Linhagem teórica e restrição

A teoria canônica §2.4.2 descreve C2C como medições individuais, agregação, ajustes e nova agregação, inclusive Beta/Dirichlet pooling. Isso fornece uma linhagem coletiva, mas não demonstra por si só uma previsão independente: escolher pooling que força consenso e depois medir consenso seria circular. O núcleo 1.9-A, A5–A6, proíbe inserir EH ou κEH diretamente nos agentes e exige confronto fora da amostra com o competidor κ=0. A definição de atenção §§8–16, 23–27, 37–54 e 108–120 exige A_i=U_i/D_i, intervenção local isolada e ausência da relação H-A1S literalmente programada. Não se pode substituir essas exigências por pesos de sociabilidade, número de interações ou CPU.

### Candidato externo identificado

Grace J. Li e Mason A. Porter, *Bounded-confidence model of opinion dynamics with heterogeneous node-activity levels*, Physical Review Research 5, 023179 (21/06/2023), DOI 10.1103/PhysRevResearch.5.023179; preprint arXiv:2206.09490, v2 de 21/03/2023. O estudo é anterior à HUMH e constrói uma extensão independente de Deffuant–Weisbuch com pesos de nós que modificam probabilidades de interação. Seus resultados publicados já mostram tempos de convergência maiores e mais fragmentação com pesos heterogêneos. Portanto, reproduzir essa direção não seria descoberta nova nem confirmação específica da HUMH.

Código original: https://gitlab.com/graceli1/NodeWeightDW . O README público identifica `DW.py` como implementação do modelo, scripts de simulação e dependências Python 3.8.10, python-igraph 0.9.7, NumPy 1.21.3, pandas 1.3.4 e SciPy 1.8.0. A página pública consultada apresentava o commit abreviado `09d648b1`, mas o SHA integral, os bytes do código e a licença ainda não foram verificados. Não se declara o código auditado, reproduzido ou congelado.

O erratum de 18/06/2024, DOI 10.1103/PhysRevResearch.6.029002, corrige rótulos 80-10 para 80-43; os parâmetros e resultados originais permanecem, segundo os autores. Qualquer reprodução deverá usar a versão corrigida, registrar o erratum e não reutilizar os rótulos antigos como se fossem distribuições distintas.

Fontes: https://doi.org/10.1103/PhysRevResearch.5.023179 ; https://arxiv.org/abs/2206.09490 ; https://www.math.ucla.edu/~mason/papers/grace-PRR-2023.pdf ; https://doi.org/10.1103/PhysRevResearch.6.029002 ; https://gitlab.com/graceli1/NodeWeightDW .

### Auditoria necessária antes da seleção

O peso w_i do artigo representa sociabilidade/atividade nominal, não atenção HUMH. Sua dinâmica é de interações diádicas, com receptividade dependente da distância entre opiniões e compromisso entre agentes. Não se pode identificar automaticamente interação selecionada, demanda elegível, atendimento válido e alteração de crença. A adaptação deve preservar a regra interna independente e explicitar como demandas exógenas, deadlines, atendimento e atualizações diádicas se relacionam, inclusive quando um agente rejeita influência ou somente um membro da díade recebe oportunidade. Rejeição por confiança não é automaticamente deadline miss.

O alvo dinâmico de uma interação não é o atrator estacionário comum do gerador R9. Assim, a futura Spec deverá declarar prospectivamente o mapeamento de p_alvo e o estimador de η compatível com o substrato, sem tratar silenciosamente o contrato antigo como se já fosse válido. A separação CANAL_A/CANAL_ETA e a definição canônica de A_i permanecem obrigatórias. B=1, K_C=2 e L_A=1 não são automaticamente transferidos para um substrato externo.

A hipótese individual H-A1S precisa enfrentar um competidor que considere o mecanismo nativo, seleção de interações, estados e exposição efetiva. A1b precisa demonstrar conteúdo incremental além de efeitos já conhecidos de atividade heterogênea e além da dinâmica local programada. Igualar A_bar não iguala necessariamente oportunidade nominal, trabalho, conteúdo ou número de eventos; a comparação deverá registrar essas distinções e impedir correção reativa por outcomes. A classificação C2 só poderá ser considerada depois de verificar independência do núcleo, preservação das regras e ausência de programação da previsão; um wrapper criado para a HUMH não confere C2 automaticamente.

### Próxima decisão técnica

Obter e fixar o código original por SHA integral e hash dos arquivos; verificar licença e erratum; reproduzir a implementação publicada em ambiente isolado; mapear as interfaces de observação, interação e atualização sem alterar a regra nativa; e produzir auditoria de viabilidade de A0, ANBC0 e ADIST0 antes de qualquer trajetória científica HUMH. Caso o mapeamento altere a dinâmica ou torne as previsões tautológicas, registrar a incompatibilidade e não ajustar parâmetros para obter aprovação. Só então integrar um desenho sucessor aos dois documentos normativos existentes, mantendo o experimento único e a identidade v2.0.0 enquanto pré-publicação. Não há coleta, seleção de braços, margens, poder ou resultado científico novo nesta pesquisa.

## R11 — Auditoria da V3 e do conteúdo meta-teórico no modelo externo

**Status:** `PRE_CODE_ANALYTIC_RESEARCH_ONLY`. Esta seção complementa e limita a rota R10. Não altera Spec, Trace, teoria, núcleo, parâmetros, Gates ou resultado científico. Nenhuma trajetória HUMH foi executada e nenhum substrato foi selecionado.

### 1. Exposição anterior e independência

A V3 existente em `source/HUMH.Api/wwwroot/V3_social.html` compara HUMH, Deffuant e Hegselmann–Krause. A inspeção do código mostra que `updateOpinion_Deffuant` escolhe um vizinho dentre os receptivos e altera somente a opinião do agente focal. Com heterogeneidade, usa `effectiveMu = mu * randomNeighbor.influence * (1 - this.resistance)`; sem heterogeneidade, usa `mu`. A V3 também possui regimes de heterogeneidade e parâmetros próprios. Portanto, sua implementação não é a regra diádica simétrica original de Li–Porter. Essa constatação é sobre código, não reavalia os resultados históricos da V3.

O usuário declarou conhecer Deffuant por sua V3, mas não conhecer o estudo de Li–Porter de 2023. Essa exposição deve ser registrada sem transformá-la em desqualificação automática. Uma implementação externa anterior pode continuar sendo C2; a escolha do substrato, das previsões e das células retidas não pode, contudo, explorar resultados já conhecidos para simular independência prospectiva. A HUMH, como meta-teoria funcional, não precisa descobrir um fenômeno social inédito; precisa formular relações que acrescentem conteúdo testável, possam falhar e não sejam apenas nomes novos para mecanismos do substrato.

### 2. Conservação exata do Deffuant simétrico fechado

O artigo de 2023, seção II, equação (1), define, para um par receptivo, `x_i' = x_i + m(x_j-x_i)` e `x_j' = x_j + m(x_i-x_j)`, com `0<m<=1/2`; um par não receptivo não muda. Os pesos de atividade modificam a seleção dos pares, não essa regra de compromisso. Assim, em cada evento, `x_i'+x_j'=x_i+x_j`, e a soma global e a média `pbar=(1/N)sum_i x_i` são invariantes em toda trajetória fechada, independentemente dos pesos, da topologia e da sequência de pares.

Se o mapeamento canônico for `p=pbar`, então `EH=1-|2pbar-1|` também é constante. Isso não impede convergência das opiniões: a dispersão pode diminuir enquanto EH permanece fixa. Em particular, não se deve substituir silenciosamente EH por variância, entropia de clusters ou outro índice para obter uma curva decrescente. A V3 calcula EH a partir da fração de agentes com opinião acima de 0,5; essa operacionalização não é idêntica à EH construída sobre a média contínua das opiniões e não pode ser transplantada sem justificativa normativa.

Consequência de desenho: o Deffuant simétrico fechado não oferece, com esse mapeamento, variação temporal de EH para identificar uma contribuição dinâmica de EH em N1a ou o efeito de atenção sobre EH. Variar a média inicial entre condições não resolve, por si só, o problema de identificação causal. Acrescentar ruído, evidência externa, atualização unilateral ou um atrator para produzir variação de EH seria uma modificação de substrato que exigiria justificativa própria; não é uma correção instrumental neutra.

### 3. Testemunho analítico de insuficiência de EH — não é run científico

A mesma regra nativa permite demonstrar que EH não determina sozinha a dinâmica de dispersão. Para uma atualização receptiva simétrica, com `d=x_j-x_i`, a variância populacional `V=(1/N)sum_i(x_i-pbar)^2` satisfaz:

`Delta V = -(2/N)*m*(1-m)*d^2`.

Logo, condicionada ao estado e à distribuição de seleção de pares `P_ij`, a variação esperada é:

`E[Delta V | x,G,w] = -(2*m*(1-m)/N) * sum_{ij} P_ij * 1{|x_i-x_j|<c} * (x_i-x_j)^2`.

V é somente um diagnóstico matemático auxiliar, não uma nova variável teórica HUMH nem outcome primário escolhido. A expressão mostra dependência da geometria de opiniões, da receptividade e da seleção de pares que não são determinadas pela média ou por EH. Os mecanismos nativos já fornecem, portanto, um competidor explicativo obrigatório.

Como testemunho exato, em uma rede completa de três agentes, escolha apenas para a prova `c=1/4` e `m=1/4`. Os estados `(2/5,1/2,3/5)` e `(1/10,1/2,9/10)` têm ambos `pbar=1/2` e `EH=1`, mas o primeiro possui `D=1/15` e o segundo `D=4/15`. No primeiro, todos os pares são receptivos; no segundo, nenhum é. Sob seleção uniforme das três díades, a variação esperada de V é respectivamente `-1/400` e `0`. A aritmética foi conferida com frações exatas, sem simulação científica. Esses números não são braços, parâmetros ou margens propostos.

Esse testemunho é coerente com a pergunta adversarial de N1b do núcleo 1.9-A, mas NÃO constitui refutação formal de N1b: o núcleo exige operacionalização de resistência estrutural, comparação preditiva com modelo adicional, margem, condições retidas e Gates. Também não comprova automaticamente A1b. Ele demonstra somente que o substrato contém informação dinâmica além de EH e que qualquer teste de suficiência precisa enfrentar essa informação.

### 4. Consequência para a seleção do experimento único

Li–Porter permanece candidato externo legítimo, especialmente para uma auditoria adversarial de suficiência estrutural e para estudar o alcance de uma descrição meta-teórica. Não será promovido a substrato primário integrado apenas porque produz fragmentação conhecida. Seus pesos `w_i` não são `A_i=U_i/D_i`; uma oportunidade nominal, uma interação selecionada, uma demanda atendida, uma rejeição por confiança e uma mudança de opinião são eventos distintos.

O próximo candidato prioritário deve permitir aprendizado/atualização a partir de evidência exógena ou outra dinâmica coletiva independente que faça variar o estado coletivo sem inserir EH ou H-A1S diretamente na regra. Modelos preexistentes de aprendizagem bayesiana distribuída ou acumulação de evidência são uma família a investigar, não uma seleção já feita. C2C continua como linhagem teórica, mas pooling que força convergência não será aceito como evidência independente. Antes de escolher implementação ou números, será necessário verificar o mapeamento de `p`, `p_alvo`, EH, demanda elegível, deadline e estimador de taxa, além de um competidor nativo e condições de falha material. Se nenhuma operacionalização preservar simultaneamente a definição de atenção e a dinâmica independente, registrar a incompatibilidade em vez de ajustar a teoria ao código.

O objetivo continua sendo um único protocolo computacional com controles e condições internas, não uma coleção de validações escolhidas após resultados. A0/A1 da construção R9 permanece preservado como demonstração/contrato de medição; qualquer sucessor confirmatório exigirá uma decisão normativa explícita, sem reclassificar resultados históricos. A2 segue não autorizado.

### 5. Estado da obtenção do código externo e fontes

A equação e os resultados publicados foram conferidos no texto do artigo. A página pública do GitLab foi localizada, mas as tentativas de obter `DW.py` por raw/API e o acesso de rede do ambiente de execução não forneceram os bytes. O SHA integral, a licença do repositório e uma reprodução executável continuam pendentes. Não se afirma que a implementação externa foi auditada, clonada ou reproduzida. O erratum de 2024 permanece obrigatório para qualquer reprodução.

Fontes externas: https://arxiv.org/html/2206.09490v2 ; https://doi.org/10.1103/PhysRevResearch.5.023179 ; https://doi.org/10.1103/PhysRevResearch.6.029002 ; https://gitlab.com/graceli1/NodeWeightDW . Fontes internas: `V3_social.html`, núcleo 1.9-A A4–A9, teoria canônica §2.4.2 e definição de atenção §§8–16, 37–54 e 108–120. A fonte externa sustenta a dinâmica e os resultados do modelo; as consequências para a HUMH e a seleção experimental são inferências desta auditoria, não afirmações dos autores de 2023.
