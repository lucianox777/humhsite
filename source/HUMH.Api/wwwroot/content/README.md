# HUMH — Índice do depósito metodológico

Este diretório separa fisicamente:

1. a **teoria de referência**;
2. o **núcleo confirmatório congelável**;
3. o **programa experimental N3 ainda evolutivo**.

---

## 1. Referente teórico

Arquivo:

`teoria.md`

Rótulo de versão no cabeçalho:

`1.7.2`

SHA-256:

```text
3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b
```

Este hash, e não apenas o número de versão escrito no documento, identifica o conteúdo teórico normativo utilizado por 1.9-A e 1.9-B.

O arquivo atual contém também notas históricas com rótulos anteriores de versão. Essas notas não mudam o referente: o conteúdo normativo é o arquivo identificado pelo SHA-256 acima.

### Correções aplicadas antes do depósito

1. Blocos de citação (ABNT, APA, BibTeX) corrigidos de `Versão 1.0` para `Versão 1.7.2`, alinhando-os ao cabeçalho. Eram instruções de citação, não notas históricas, e propagariam rótulo incorreto para bibliografias.
2. Inserida a **Nota metodológica posterior (depósito 1.9-A)** reclassificando V1–V6 como Classe C1.
3. Terminação de linha normalizada de CRLF para **LF**, uniformizando o conjunto e reduzindo o risco de quebra de hash por normalização automática.

A nota histórica de rótulo `1.6.0` (seção anterior ao glossário) foi preservada intencionalmente.

### Hash anterior obsoleto do referente teórico

```text
5c8258e1aae5f735d5730ddc93f0f816825c8ec2b23f126aa0c969d10a0a5505
```

Corresponde ao arquivo antes das correções acima. Não deve ser usado como referente.

**Recomendação de depósito:** enviar `teoria.md` exatamente como está agora, sem nova alteração.

---

## 2. Núcleo confirmatório

Arquivo:

`HUMH_Nucleo_1.9A.md`

Escopo:

\[
HUMH_{1.9A}
=
N1a\land N1b\land N2.
\]

SHA-256 desta versão:

```text
baeba8eae26a939b849b1dc0763c69062e2fa61728ddbec31109e72985c8015b
```

Este é o objeto que deve ser tratado como referente imutável de 1.9-A após o depósito.

Ele contém internamente:

- classificação C1/C2/E;
- classificação explícita do experimento WebWorkers como C1;
- taxonomia REFUTADA / INCONCLUSIVA / NÃO REFUTADA / COMPATÍVEL / SUPORTADA;
- N1a com comparação aninhada \(M_0:\kappa=0\) versus \(M_1:\kappa>0\);
- \(s_{min}=0{,}05\);
- \(\delta_\kappa\approx0{,}0763(1+\iota_{obs})\);
- \(\delta_{N1b}=10\%\);
- \(\delta_{sep}=10\%\);
- V7-H1 como consequência qualitativa Classe E, com interpretação simétrica;
- resgates proibidos;
- regra de refutação do núcleo;
- imutabilidade e regra de versionamento.

### Hash anterior obsoleto

Dois hashes anteriores de 1.9-A estão obsoletos:

```text
a6f96a77c2a55e87422c0c25abe717ea823b1e22659decbd299879a56b5b47ea
dfdd673da080b4e1e4038f7a57c2608d48c947f77a1629b9094cfb18bd835991
```

O primeiro correspondia à extração incompleta, sem as travas normativas. O segundo continha as travas, mas apontava para o hash pré-correção de `teoria.md` e não declarava a convenção de bytes. Nenhum dos dois deve ser usado como referente.

---

## 3. Programa Experimental N3

Arquivo:

`HUMH_Programa_N3_1.9B.md`

Status:

**EM DESENVOLVIMENTO / NÃO CONGELADO**

SHA-256 atual, apenas para rastreabilidade desta distribuição:

```text
a9bfd724b7af7849711570798eb8134282fa93fe39093fbd7f4b637041f5a226
```

Esse hash **não** significa congelamento metodológico de 1.9-B.

O programa inclui:

- N3T\(_K\);
- N3F;
- S1-CAL / S1-VAL / Gate K0;
- S2;
- S3;
- compressão;
- rota C2;
- regras de parada;
- V7/V8;
- repilotagem técnica.

As regras de N1a/N1b/N2 não são definidas por este arquivo; ele apenas referencia o núcleo congelado.

---

## 4. Compatibilidade terminológica com `teoria.md`

O arquivo teórico já reconhece, em trechos de síntese, que V1–V6 são validações computacionais/exploratórias que demonstram consistência interna e isomorfismo e não substituem validação empírica independente.

Em seções históricas detalhadas, porém, ainda aparecem expressões como:

- `VALIDADO`;
- `PASSOU INTEGRALMENTE`;
- `VALIDAÇÃO MATEMÁTICA COMPUTACIONAL`.

Para evitar ambiguidade, na taxonomia metodológica atual esses resultados devem ser interpretados como:

\[
\boxed{
\text{demonstrações C1 de consistência/compatibilidade computacional}
}
\]

e não como validação independente da HUMH.

Essa reclassificação não apaga nem modifica os resultados históricos; apenas aplica um padrão epistemológico posterior e mais rigoroso.

### Nota recomendada para futura revisão de `teoria.md`

> **Nota metodológica posterior:** nas versões iniciais, os termos “VALIDADO” e “PASSOU INTEGRALMENTE” indicavam satisfação dos critérios computacionais internos então definidos. Na taxonomia metodológica posterior, esses experimentos são classificados como C1 e, portanto, demonstram consistência/compatibilidade computacional, não validação independente da HUMH. O objeto confirmatório congelado vigente está definido em `HUMH_Nucleo_1.9A.md`.

Não é necessário modificar `teoria.md` para identificar o referente do depósito atual, pois o SHA-256 acima fixa exatamente o arquivo utilizado.

---

## 5. V7-H1 e N1a

A relação está congelada em `HUMH_Nucleo_1.9A.md`, seção A12:

\[
\boxed{
\text{V7-H1 = consequência qualitativa Classe E de N1a}
}
\]

Interpretação:

- direção prevista com evidência adequada → **CONVERGENTE**;
- precisão/poder insuficientes → **INCONCLUSIVO**;
- direção contrária ou ausência suficientemente estabelecida → **DESCONFIRMATÓRIO**.

Um resultado DESCONFIRMATÓRIO deve ser reportado junto de alegações posteriores sobre N1a, embora não constitua sozinho a refutação formal da N1a quantitativa.

---

## 6. Nomes de arquivo e rastreabilidade

Os nomes canônicos deste conjunto são:

```text
teoria.md
HUMH_Nucleo_1.9A.md
HUMH_Programa_N3_1.9B.md
README.md
```

Ao enviar para OSF ou outro repositório, confirmar os **nomes reais após o upload**. Caso a plataforma sanitize pontos, espaços ou caracteres, atualizar este índice para o nome efetivamente depositado, sem alterar o conteúdo dos arquivos congelados.

A identidade científica do conteúdo congelado é garantida pelo hash; o nome do arquivo garante navegabilidade.

---

## 6.1. Convenção de bytes

Todos os arquivos deste depósito usam:

- terminação de linha **LF**;
- codificação **UTF-8 sem BOM**.

Os SHA-256 registrados pressupõem exatamente esses bytes. Ferramentas que normalizam quebras de linha automaticamente (por exemplo `git` com `core.autocrlf=true`) alteram o conteúdo e invalidam os hashes. Ao versionar em git, usar `.gitattributes` com `*.md -text` ou `text eol=lf`.

---

## 6.2. Cadeia de integridade

Este `README.md` registra os hashes, mas não é ele próprio hasheado — ele é mutável por construção, pois precisa acomodar hashes sucessores.

A garantia final de integridade do conjunto é o **Registration do OSF**, que congela o componente inteiro com timestamp e identificador persistente. A cadeia é:

\[
\text{Registration OSF}
\;\rightarrow\;
\text{README (índice + hashes)}
\;\rightarrow\;
\text{arquivos congelados}.
\]

Um revisor deve verificar os hashes contra os arquivos depositados, e não confiar apenas nos valores transcritos aqui.

---

## 7. Regra de versionamento

1. Após o depósito, `HUMH_Nucleo_1.9A.md` permanece imutável.
2. Qualquer alteração em N1a/N1b/N2 exige nova identidade e novo hash.
3. `HUMH_Programa_N3_1.9B.md` continua evolutivo até seu próprio congelamento.
4. Falhas confirmatórias permanecem registradas.
5. Uma versão sucessora nunca apaga a previsão anterior.
6. O referente teórico deve ser identificado pelo hash exato do arquivo usado.

---

## 8. Próxima etapa executiva

Após o depósito de 1.9-A, a próxima etapa é especificar **S1 antes do código**.

A especificação deverá congelar pelo menos:

- definição operacional de UM;
- \(R_{eff}\);
- \(\gamma_{manut}\);
- \(t_{trans}\);
- famílias de parâmetros;
- seeds;
- divisão S1-CAL / S1-VAL;
- procedimento de estimação de \(K_{N3}\);
- Gate K0;
- censura;
- logs;
- exclusões técnicas.

Só depois dessa especificação deverá começar a implementação confirmatória.
