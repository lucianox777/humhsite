#!/usr/bin/env bash
set -euo pipefail

BASE='source/HUMH.Api/wwwroot/content'
OLD_ZIP="$BASE/HUMH_A0_A1_v2.0.0_Publicacao_Autocontida.zip"
TARGET="$BASE/experimentos/atencao/v2.0.0"
STAGE='.github/humh-stage'
WORKFLOW='.github/workflows/humh-materialize-a0a1-v2.yml'

[ -f "$OLD_ZIP" ] || { echo "Base package not found: $OLD_ZIP" >&2; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/unzip" "$TMP/work"

python3 - "$OLD_ZIP" "$TMP/unzip" <<'PY'
from pathlib import Path
from zipfile import ZipFile
import sys
with ZipFile(sys.argv[1]) as z:
    z.extractall(sys.argv[2])
PY

SRC="$TMP/unzip/HUMH_A0_A1_v2.0.0_Publicacao_Autocontida"
[ -d "$SRC" ] || { echo "Unexpected base ZIP layout" >&2; exit 1; }
cp -a "$SRC/." "$TMP/work/"

cat "$STAGE"/part-* > "$TMP/update.patch.bz2"
bzip2 -dc "$TMP/update.patch.bz2" > "$TMP/update.patch"
(
  cd "$TMP/work"
  patch --batch --forward -p1 < "$TMP/update.patch"
  python3 03_integridade/verify.py
)

# Frozen R3 identities.
echo 'b27152f19c6aa2f9f9c98417c4ee970db33091a53b5bf842b3562e5e6fd40e34  01_experimento/HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md' > "$TMP/expected.sha256"
echo 'f2ddafaf62b9c4d5e2faef8096382a2262459508a7fbaba75328bb63e792542f  01_experimento/HUMH_A0_A1_Traceabilidade_v2.0.0.json' >> "$TMP/expected.sha256"
echo '3f89058c0931515abe94f56393733cdebed8f49a35003ae1b17949686540bb7a  02_dependencias/HUMH_Definicao_Atencao_Observacional_Efetiva_v1.0.0.md' >> "$TMP/expected.sha256"
echo '3ce6c097a11c7c33cc94439e44d2ec2821b60affbfedec8401cc9572d58bf23b  02_dependencias/teoria.md' >> "$TMP/expected.sha256"
(cd "$TMP/work" && sha256sum -c "$TMP/expected.sha256")

rm -rf "$TARGET"
mkdir -p "$TARGET"
cp -a "$TMP/work/." "$TARGET/"
cat > "$TARGET/HUMH_A0_A1_v2.0.0.sha256" <<'EOF'
b27152f19c6aa2f9f9c98417c4ee970db33091a53b5bf842b3562e5e6fd40e34  HUMH_A0_A1_Especificacao_Experimental_v2.0.0.md
f2ddafaf62b9c4d5e2faef8096382a2262459508a7fbaba75328bb63e792542f  HUMH_A0_A1_Traceabilidade_v2.0.0.json
EOF

mkdir -p "$BASE/experimentos/atencao"
cat > "$BASE/experimentos/atencao/README.md" <<'EOF'
# HUMH — Experimentos de Atenção

O diretório `v2.0.0/` contém a árvore materializada corrente do desenho A0/A1 pré-publicação.

Status científico corrente:

- `ANBC0 = FAIL_DERIVATIONAL`;
- `A1a = MECHANISM_DEMONSTRATION_ONLY [C1]`;
- `ASEP0_CONFIRMATORY = NOT_AUTHORIZED`;
- próximo bloqueio: auditoria do conteúdo coletivo independente de A1b;
- `SCIENTIFIC_RUN_NOT_AUTHORIZED`.

A teoria exibida pelo site continua sendo `../../teoria.md`. A cópia de `teoria.md` dentro de `v2.0.0/02_dependencias/` é uma dependência canônica hash-locked do experimento e não substitui a fonte do site.

O arquivo histórico `../../HUMH_A0_A1_v2.0.0_Publicacao_Autocontida.zip` antecede o fechamento R3 e não deve ser tratado como a árvore corrente.
EOF

# Remove only the temporary materialization mechanism from the final repository.
git rm -r --ignore-unmatch "$STAGE" "$WORKFLOW"
git add "$BASE/experimentos/atencao"

if git diff --cached --quiet; then
  echo 'Nothing to commit.'
  exit 0
fi

git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git commit -m 'materialize HUMH attention experiment v2.0.0 R3'
if [ "${HUMH_DRY_RUN:-0}" = '1' ]; then
  echo 'DRY_RUN_PUSH'
else
  git push origin HEAD:main
fi
