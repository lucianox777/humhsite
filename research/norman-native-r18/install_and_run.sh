#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

mkdir -p upstream results dependencies
export DEBIAN_FRONTEND=noninteractive
export R_LIBS_USER="$PWD/dependencies/R-library"
mkdir -p "$R_LIBS_USER"
export R_HOME="$(R RHOME)"

sudo env JAVA_HOME="$JAVA_HOME" PATH="$PATH" R CMD javareconf

Rscript - <<'RS' 2>&1 | tee results/R_bootstrap.log
options(repos=c(CRAN='https://cloud.r-project.org'), timeout=600)
.libPaths(c(Sys.getenv('R_LIBS_USER'), .libPaths()))

install_checked <- function(label, expr) {
  cat("\n=== INSTALL:", label, "===\n")
  tryCatch(
    {
      force(expr)
      cat("=== INSTALL OK:", label, "===\n")
    },
    error=function(e) {
      cat("=== INSTALL FAILED:", label, "===\n", conditionMessage(e), "\n")
      quit(status=41, save="no")
    }
  )
}

install_checked("BiocManager",
                install.packages("BiocManager", Ncpus=2))
if (!requireNamespace("BiocManager", quietly=TRUE))
  stop("BiocManager unavailable after installation")

install_checked("Bioconductor graph + Rgraphviz",
                BiocManager::install(c("graph","Rgraphviz"),
                                     ask=FALSE, update=FALSE, Ncpus=2))

install_checked("rJava",
                install.packages("rJava", Ncpus=2))

# Historical pair used with gRain 1.3.14 in R 4.3-era environments.
install_checked("gRbase 1.8.9",
                install.packages(
                  "https://cran.r-project.org/src/contrib/Archive/gRbase/gRbase_1.8.9.tar.gz",
                  repos=NULL, type="source"
                ))

install_checked("bnlearn 4.9.1",
                install.packages(
                  "https://cran.r-project.org/src/contrib/Archive/bnlearn/bnlearn_4.9.1.tar.gz",
                  repos=NULL, type="source"
                ))

install_checked("gRain 1.3.14",
                install.packages(
                  "https://cran.r-project.org/src/contrib/Archive/gRain/gRain_1.3.14.tar.gz",
                  repos=NULL, type="source"
                ))

required <- c(
  rJava="rJava",
  graph="graph",
  Rgraphviz="Rgraphviz",
  gRbase="gRbase",
  bnlearn="bnlearn",
  gRain="gRain"
)
for (p in required) {
  if (!requireNamespace(p, quietly=TRUE))
    stop("PACKAGE_NOT_AVAILABLE_AFTER_INSTALL: ", p)
}

expected <- c(
  gRbase="1.8.9",
  bnlearn="4.9.1",
  gRain="1.3.14"
)
actual <- vapply(names(expected), function(p)
  as.character(packageVersion(p)), character(1))

cat("\n=== FROZEN PACKAGE VERSIONS ===\n")
print(actual)

for (p in names(expected)) {
  if (!identical(actual[[p]], expected[[p]]))
    stop("VERSION_MISMATCH ", p, ": expected ", expected[[p]],
         ", got ", actual[[p]])
}

writeLines(capture.output(sessionInfo()), "results/R_session_info.txt")
writeLines(capture.output(installed.packages()[,
  c("Package","Version","LibPath"), drop=FALSE]),
  "results/R_installed_packages.txt")
writeLines(system.file("jri", package="rJava"), "results/jri_path.txt")
RS

export LD_LIBRARY_PATH="$(cat results/jri_path.txt):$R_HOME/lib:${LD_LIBRARY_PATH:-}"
mkdir -p "$HOME/.netlogo/6.2.1/r"
printf 'r.home=%s\njri.home.paths=%s\n' "$R_HOME" "$(cat results/jri_path.txt)" > "$HOME/.netlogo/6.2.1/r/user.properties"
export JAVA_TOOL_OPTIONS="-Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djava.library.path=$(cat results/jri_path.txt):$R_HOME/lib"

curl --fail --location --retry 3 --silent --show-error \
  'https://raw.githubusercontent.com/NormAN-framework/base-model/6ad82d26fa9d3c32c9ff4db5a89bba2618c74283/base-model.nlogo' \
  -o upstream/base-model.nlogo

python3 prepare_native.py upstream/base-model.nlogo

curl --fail --location --retry 3 --silent --show-error \
 'https://raw.githubusercontent.com/NormAN-framework/base-model/6ad82d26fa9d3c32c9ff4db5a89bba2618c74283/license.md' \
 -o upstream/license.md

curl --fail --location --retry 3 --silent --show-error \
 'https://ccl.northwestern.edu/netlogo/6.2.1/NetLogo-6.2.1-64.tgz' \
 -o dependencies/NetLogo-6.2.1-64.tgz

sha256sum dependencies/NetLogo-6.2.1-64.tgz > results/netlogo_archive.sha256
tar -xzf dependencies/NetLogo-6.2.1-64.tgz -C dependencies

NETLOGO_DIR="$(dirname "$(find "$PWD/dependencies" -name netlogo-headless.sh -type f -print -quit)")"
test -n "$NETLOGO_DIR" && test -f "$NETLOGO_DIR/netlogo-headless.sh"

for name in seed2025_NO_COMMUNICATION seed2025_COMMUNICATION seed2026_NO_COMMUNICATION seed2026_COMMUNICATION; do
  echo "=== Native NormAN: $name ==="
  (cd "$PWD" && bash "$NETLOGO_DIR/netlogo-headless.sh" \
    --model "$PWD/upstream/base-model.nlogo" \
    --setup-file "$PWD/experiments.xml" \
    --experiment "$name" \
    --threads 1 \
    --table "$PWD/results/$name.csv") \
    > "results/$name.stdout.log" 2>&1
  test -s "results/$name.csv"
done

python3 analyze_native.py

python3 - <<'PY'
import hashlib, json, platform
from pathlib import Path
root = Path(".")
files = {
    str(p): hashlib.sha256(p.read_bytes()).hexdigest()
    for p in sorted((root/"results").glob("*"))
    if p.is_file()
}
(root/"results/sha256.json").write_text(
    json.dumps({"files": files, "python": platform.python_version()}, indent=2) + "\n"
)
PY
