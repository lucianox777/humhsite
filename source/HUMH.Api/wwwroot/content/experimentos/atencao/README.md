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