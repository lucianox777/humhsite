# HUMH — Núcleo Congelado 1.9-A

**Identidade do objeto:** `HUMH_1.9A`  
**Status:** PRONTO PARA CONGELAMENTO / DEPÓSITO  
**Escopo lógico:** \(N1a \land N1b \land N2\)  
**N3:** não integra este objeto  
**Referente teórico normativo:** `teoria.md`  
**Rótulo de versão no cabeçalho da teoria:** 1.7.2  
**SHA-256 do referente teórico:** `3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b`
**Convenção de bytes:** todos os arquivos deste depósito usam terminação de linha **LF** e codificação **UTF-8 sem BOM**. Os SHA-256 pressupõem exatamente esses bytes.

> Em caso de divergência entre rótulos internos de versão presentes em `teoria.md`, o conteúdo normativo referido por este núcleo é identificado pelo SHA-256 acima. O arquivo teórico deve ser depositado sem alteração junto deste núcleo.

---

# A1. Identidade e alcance do núcleo

O objeto confirmatório congelável é:

\[
\boxed{
HUMH_{1.9A}
=
N1a\land N1b\land N2
}
\]

N3T\(_K\), N3F e qualquer programa posterior de transportabilidade não integram este objeto histórico.

A refutação de uma hipótese sucessora não altera retrospectivamente este núcleo, e uma revisão futura não substitui o resultado obtido por 1.9-A.

---

# A2. Classes epistemológicas e classificação do experimento computacional

A taxonomia operacional adotada por 1.9-A é:

## C1 — substrato construído para o programa

Sistema cuja microdinâmica foi construída pelo pesquisador para testar a HUMH.

**Classificação congelada:** qualquer implementação HTML/JavaScript/Web Workers escrita especificamente para testar N1a, N1b ou N2 é **Classe C1**.

Um resultado positivo C1 pode atingir no máximo:

\[
\boxed{\text{COMPATÍVEL}}
\]

Um resultado negativo C1 pode REFUTAR uma previsão congelada se os Gates técnicos, o poder e as condições confirmatórias forem adequados.

## C2 — substrato computacional independente

Sistema computacional existente independentemente da HUMH, não escrito para produzir suas previsões e selecionado por regra pré-registrada.

Um resultado confirmatório adequado pode atingir:

\[
\boxed{\text{SUPORTADA [C2]}}
\]

## E — substrato externo

Sistema externo cuja microdinâmica não foi escrita para produzir a previsão HUMH, incluindo observadores humanos.

Um resultado confirmatório adequado pode atingir:

\[
\boxed{\text{SUPORTADA [E]}}
\]

Em heterogeneidade do substrato:

\[
C1<C2<E.
\]

---

# A3. Taxonomia de estados de resultado

Os estados globais possíveis para uma hipótese de 1.9-A são:

## REFUTADA

Critério de refutação congelado atingido, com Gates e poder adequados.

## INCONCLUSIVA

O desenho, o poder, a precisão, o suporte comum ou algum Gate técnico são insuficientes para decisão válida.

## NÃO REFUTADA

O teste válido não atingiu o critério de refutação, mas também não satisfaz o critério positivo necessário para classificação superior.

## COMPATÍVEL

Uma previsão confirmatória sobrevive em C1 sob o protocolo congelado. Indica compatibilidade computacional, não suporte independente.

## SUPORTADA

Exige previsão congelada sobrevivendo em substrato independente adequado:

- **SUPORTADA [C2]**
- **SUPORTADA [E]**
- **SUPORTADA [C2+E]**, quando ambas as classes contribuírem.

A taxonomia específica de V7-H1 — CONVERGENTE / INCONCLUSIVO / DESCONFIRMATÓRIO — descreve somente a relação daquele resultado humano com a consequência qualitativa de N1a e não substitui os cinco estados globais acima.

---

# A4. EH e divergência \(D\)

Para sistema binário:

\[
EH=1-|2\bar p-1|
\]

com:

\[
\bar p=\frac1N\sum_i p_i.
\]

EH não mede verdade externa.

Define-se divergência interobservador:

\[
D=\frac1N\sum_i|p_i-\bar p|.
\]

EH e \(D\) são grandezas distintas.

Unanimidade em \(p_i=0{,}5\) e polarização 50/50 em \(p_i\in\{0,1\}\) podem produzir o mesmo \(\bar p\) e o mesmo EH, embora apresentem divergências \(D\) muito diferentes.

---

# A5. N1a — contribuição dinâmica independente de EH

A forma operacional é:

\[
\eta(EH)
=
\frac{\omega}
{1+\iota_{obs}+\kappa EH}.
\]

N1a afirma:

\[
\boxed{\kappa>0}
\]

em magnitude dinamicamente relevante.

A hipótese é sobre a **dinâmica coletiva emergente**, não sobre uma regra inserida diretamente nos agentes. Em um teste confirmatório, os agentes não podem ser programados para consultar EH ou \(\kappa EH\) como causa da própria convergência que será usada para estimar \(\kappa\).

---

# A6. Competidor aninhado obrigatório de N1a

A comparação confirmatória deve incluir explicitamente:

\[
\boxed{
M_0:\kappa=0
}
\]

com:

\[
\eta_0
=
\frac{\omega}
{1+\iota_{obs}},
\]

contra:

\[
\boxed{
M_1:\kappa>0
}
\]

com:

\[
\eta_1(EH)
=
\frac{\omega}
{1+\iota_{obs}+\kappa EH}.
\]

\(M_0\) e \(M_1\) devem usar o mesmo acesso aos dados, o mesmo particionamento CAL/VAL, o mesmo protocolo de ajuste e as mesmas células retidas.

A comparação relevante é **fora da amostra**.

Não conta como evidência de N1a simplesmente observar correlação entre EH e uma variável que já é função de \(\bar p\).

---

# A7. Faixa e efeito mínimo de N1a

A faixa confirmatória é:

\[
a=0{,}20,
\qquad
b=0{,}90,
\]

logo:

\[
\boxed{
EH\in[0{,}20;0{,}90]
}
\]

Mantém-se:

\[
\boxed{s_{min}=0{,}05}
\]

Para:

\[
\eta(EH)
=
\frac{\omega}
{1+\iota_{obs}+\kappa EH},
\]

a redução relativa de velocidade entre \(a\) e \(b\) é:

\[
s_{a,b}
=
1-\frac{\eta(b)}{\eta(a)}
=
\frac{\kappa(b-a)}
{1+\iota_{obs}+\kappa b}.
\]

A margem correspondente é:

\[
\boxed{
\delta_\kappa
=
\frac{
s_{min}(1+\iota_{obs})
}{
(b-a)-s_{min}b
}
}
\]

e, para \(s_{min}=0{,}05\), \(a=0{,}20\), \(b=0{,}90\):

\[
\boxed{
\delta_\kappa
\approx
0{,}0763(1+\iota_{obs})
}
\]

---

# A8. Critério de N1a

N1a exige que o mesmo \(\kappa\):

- generalize para condições retidas;
- atravesse histórias diferentes;
- atravesse condições de recurso;
- atravesse memórias e/ou topologias pré-especificadas;
- forneça contribuição dinâmica não reduzível ao caso aninhado \(M_0\).

Com poder adequado, N1a será REFUTADA se efeitos iguais ou superiores a \(s_{min}\) forem excluídos ou se equivalência estabelecer:

\[
|\kappa|<\delta_\kappa.
\]

Sobrevivência em C1 classifica N1a como, no máximo, COMPATÍVEL.

---

# A9. N1b — suficiência estrutural de EH

N1b afirma:

\[
\boxed{
\iota_{ord}
=
\kappa EH
}
\]

como representação estrutural suficiente no domínio declarado.

O teste adversarial principal compara estados com EH semelhante e divergência \(D\) diferente.

## Indecisão homogênea

\[
EH\approx1,
\qquad
D\approx0.
\]

## Polarização

\[
EH\approx1,
\qquad
D\gg0.
\]

A margem congelada é:

\[
\boxed{
\delta_{N1b}=10\%
}
\]

N1b será REFUTADA se polarização e indecisão diferirem materialmente além dessa margem e um modelo pré-especificado que inclua informação adicional, como \(D\), generalizar materialmente melhor que \(\kappa EH\).

Falha de N1b não implica automaticamente falha de N1a.

---

# A10. N2 — separabilidade das resistências

N2 afirma:

\[
\boxed{
\beta_{total}
=
\iota_{obs}
+
\iota_{ord}.
}
\]

O teste exige estimação separada de:

\[
\iota_{obs}(R_i)
\]

e:

\[
\iota_{ord}(E_j),
\]

seguida de congelamento dos parâmetros.

As células cruzadas:

\[
R_i\times E_j
\]

devem então ser previstas sem reajuste.

A margem congelada é:

\[
\boxed{
\delta_{sep}=10\%.
}
\]

---

# A11. Dependência lógica e sobreidentificação

Se:

\[
\kappa\approx0,
\]

então a componente estrutural:

\[
\iota_{ord}=\kappa EH
\]

perde conteúdo.

A mesma falha não deverá ser contada como duas refutações estatisticamente independentes de N1a e N2.

N1a precede logicamente a interpretação plena de N2.

---

# A12. V7-H1 como consequência qualitativa Classe E de N1a

A relação entre V7-H1 e N1a é congelada como:

\[
\boxed{
\text{V7-H1 = consequência qualitativa Classe E de N1a}
}
\]

A previsão qualitativa é:

\[
EH\uparrow
\Rightarrow
RT\uparrow.
\]

V7-H1:

- não estima diretamente \(\kappa\);
- não testa sozinho a forma racional completa de \(\eta(EH)\);
- não substitui \(\delta_\kappa\);
- não substitui \(s_{min}\);
- não transforma automaticamente \(EH\rightarrow RT\) em validação quantitativa de N1a.

A interpretação é simétrica:

- resultado na direção prevista, com evidência adequada: **CONVERGENTE**;
- precisão ou poder insuficientes: **INCONCLUSIVO**;
- efeito em direção contrária, ou ausência suficientemente estabelecida segundo critério pré-registrado: **DESCONFIRMATÓRIO** para a consequência qualitativa de N1a.

Um resultado DESCONFIRMATÓRIO deve acompanhar qualquer alegação posterior sobre N1a, mas **não constitui, por si só, refutação formal de N1a ou de 1.9-A**, cujos critérios quantitativos permanecem os de A8.

A operacionalização estatística de “evidência adequada”, “ausência suficientemente estabelecida” e “inconclusivo” deverá ser congelada no protocolo humano antes da coleta.

---

# A13. Resgates proibidos

Após o congelamento de 1.9-A, são proibidos os seguintes resgates pós-resultado:

1. reduzir ou redefinir \(s_{min}\), \(\delta_\kappa\), \(\delta_{N1b}\) ou \(\delta_{sep}\);
2. alterar a faixa confirmatória \(EH\in[0{,}20;0{,}90]\) para excluir células desfavoráveis;
3. reclassificar células CAL como VAL, ou VAL como CAL, após inspeção dos resultados;
4. reajustar \(\kappa\), \(\iota_{obs}\) ou \(\iota_{ord}\) utilizando células retidas;
5. modificar \(M_0\) ou remover a comparação aninhada \(\kappa=0\) depois dos resultados;
6. acrescentar \(D\), novas covariáveis, interações ou parâmetros para salvar N1b e ainda chamar o resultado de confirmação da mesma formulação congelada;
7. alterar retrospectivamente as condições de polarização/indecisão ou a definição de \(D\);
8. reinterpretar \(\kappa\approx0\) como confirmação conceitual de N1a;
9. redefinir \(\iota_{ord}\) após resultados para preservar N2;
10. excluir topologias, recursos, memórias ou históricos confirmatórios apenas porque produziram falha;
11. invocar o caráter de “meta-teoria” para dispensar o caso aninhado \(M_0\), os dados retidos ou os critérios de equivalência;
12. promover V7-H1 de consequência qualitativa a teste quantitativo direto depois de observar os dados;
13. contar uma mesma falha causal como múltiplas refutações independentes quando houver dependência lógica declarada;
14. apagar ou substituir historicamente uma previsão refutada por uma versão sucessora.

Uma hipótese sucessora é permitida, mas deverá receber nova identidade/versionamento, preservar a falha anterior e poder falhar novamente.

---

# A14. Regra de refutação do núcleo

Como:

\[
HUMH_{1.9A}
=
N1a\land N1b\land N2,
\]

a refutação confirmatória válida de qualquer componente refuta:

\[
\boxed{
HUMH_{1.9A}
}
\]

como formulação congelada.

Isso não impede a criação de uma versão posterior, mas a nova versão não altera o status histórico de 1.9-A.

---

# A15. Imutabilidade, hash e depósito

Este arquivo deve ser depositado como objeto independente.

Depois do congelamento:

- qualquer alteração em N1a, N1b ou N2 exige nova versão;
- este arquivo original deve permanecer preservado;
- o referente teórico `teoria.md` deve permanecer associado pelo SHA-256 informado no cabeçalho;
- resultados negativos devem permanecer registrados;
- alterações no programa N3 1.9-B não modificam este núcleo.

O SHA-256 deste arquivo é calculado **somente após a gravação final dos bytes** e deve ser registrado no `README.md` do depósito.
