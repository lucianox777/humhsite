# HUMH V3 — R14 · Proposta sucessora pré-código

**Status:** `PRE_CODE_DRAFT_NOT_FROZEN`  
**Run científico novo:** não executado  
**Teoria / Núcleo 1.9-A / Spec e Trace v2.0.0 / V3 histórica:** não alterados.  
**Autoridade:** nota de auditoria, não normativa.

## Decisão

A R13 propôs uma ponte coletiva baseada em D e exposição C2C. A R14 redigiu uma Spec sucessora candidata e sua Traceabilidade, sem aprovar a ponte como estimando confirmatório. A definição de atenção continua fixando o estimador individual; na V3 ele recupera a taxa nativa constante. Não se substitui esse estimador silenciosamente, não se reabre ANBC0 por conveniência e não se altera o Núcleo 1.9-A.

A V3 representa opiniões escalares e médias ponderadas, não o Beta/Dirichlet pooling literal da teoria. O mapeamento formal C2C permanece pendente. Observador e Observado podem ser funções simultâneas, com atualizações assimétricas; ruído, capacidade e atenção são distintos. Sem fonte efetiva não há atualização causada por essa relação C2C. Componentes sem comunicação não serão artificialmente agregados como consenso único.

A ponte R13 permanece fenomenológica e não derivada automaticamente da HUMH:

`Y=D_t-D_{t+1}; E=U_cycle/N_eligible; C=Y/(E*D_t)`.

`M0: Y=E*theta*D+erro`.

`M1: Y=E*theta*D/(1+lambda*EH)+erro`, lambda≥0.

E é densidade auxiliar de conclusões, não atenção, e pode exceder 1. Uma previsão que utiliza E realizado é condicional, não previsão causal prospectiva. O uso confirmatório exige unidade temporal, identificação, informação disponível e comparadores nativos previamente definidos. O competidor N1b com informação adicional D permanece candidato, sem parâmetros escolhidos pelos resultados.

## Adversário matemático adicional

A regra nativa, sem clipping e com pesos dependentes de diferenças, pode ser equivariante a uma translação comum das opiniões. Isso conserva as diferenças e D, mas pode alterar EH. Portanto, uma contração universal diferente apenas por EH enfrenta um adversário estrutural direto. O canal aditivo da v0.2.1 tem clipping, logo a invariância não é declarada global. Não se introduzirão bordas, ruído ou heterogeneidade para produzir lambda positivo.

Outro testemunho exato, com três agentes, taxa 1/4, homofilia zero, sem ruído e atualização síncrona, mostra que a mesma condição inicial p=(0,1/2,1) produz contração C=1/4 no caminho e C=3/8 no grafo completo, com EH=1, D=1/3 e E=1. São exemplos matemáticos, não novas trajetórias científicas nem parâmetros de run.

## Artefatos candidatos locais

- Spec: `01_Spec_V3_Coletiva_v3.0.0_DRAFT.md` — SHA-256 `2006d1d12bf2dcd96a49d9038bf91f4dbbe38387416cef157efc7a58f4fae48e`.
- Trace: `02_Traceabilidade_V3_Coletiva_v3.0.0_DRAFT.json` — SHA-256 `25f6f967b5a5fb6e44eaab6043c3ddbd9bffd4413cd2de276352020cd0221f47`.
- Pacote reproduzível: `HUMH_V3_Sucessora_R14_DRAFT.zip` — SHA-256 `5d6edc79b7857e44d6396f8308be7150ae6760c6d9df09b105eec46425ea1a99`.

O pacote contém os dois documentos candidatos, testemunhos matemáticos exatos, verificador e manifesto. Os arquivos completos do pacote não são incorporados por esta nota ao repositório. Nenhum dado bruto novo ou antigo é publicado aqui.

## Rastreabilidade e estado

Os 11 Gates raízes permanecem os do protocolo vigente. A Trace candidata contém 23 itens e 17 decisões ainda não congeladas: mapeamento C2C; ponte e unidade de eta; conteúdo independente de A1a; coortes/componentes; exposição e horizonte; suporte EH; adversarial N1b; parâmetros nativos; canal; instrumento/agenda; comparadores; identificação; CAL/VAL; poder; integridade; N2; e aprovação prospectiva. As margens do núcleo permanecem inalteradas.

A verificação local dos documentos, referências e hashes passou. Os exemplos exatos não constituem execução científica. A aprovação final ainda exige verificar os bytes correntes da Spec/Trace R9, resolver a adequação do estimando e o conteúdo independente, congelar os campos pendentes e demonstrar poder. R9–R13, inclusive os diagnósticos lambda=0, permanecem registrados. N3T-K0_CONSTANT continua REFUTADA [C1]. A2 continua não autorizado.

**Próximo ato:** revisão científica da proposta e decisão objetiva sobre a adequação da V3. Se não houver conteúdo independente identificável, registrar o limite e avaliar prospectivamente um substrato externo, sem ajustar a teoria ou a microdinâmica para obter o resultado desejado.