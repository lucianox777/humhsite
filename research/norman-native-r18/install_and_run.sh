#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p upstream results dependencies
export DEBIAN_FRONTEND=noninteractive
export R_LIBS_USER="$PWD/dependencies/R-library"
mkdir -p "$R_LIBS_USER"
export R_HOME="$(R RHOME)"
sudo env JAVA_HOME="$JAVA_HOME" PATH="$PATH" R CMD javareconf
Rscript - <<'RS'
options(repos=c(CRAN='https://cloud.r-project.org'),timeout=600)
.libPaths(c(Sys.getenv('R_LIBS_USER'),.libPaths()))
install.packages('BiocManager',Ncpus=2)
BiocManager::install(c('graph','Rgraphviz'),ask=FALSE,update=FALSE,Ncpus=2)
install.packages(c('rJava','gRbase'),Ncpus=2)
install.packages('https://cran.r-project.org/src/contrib/Archive/bnlearn/bnlearn_4.9.1.tar.gz',repos=NULL,type='source')
install.packages('https://cran.r-project.org/src/contrib/Archive/gRain/gRain_1.3.14.tar.gz',repos=NULL,type='source')
for(p in c('rJava','bnlearn','gRain')) stopifnot(requireNamespace(p,quietly=TRUE))
stopifnot(as.character(packageVersion('bnlearn'))=='4.9.1')
stopifnot(as.character(packageVersion('gRain'))=='1.3.14')
writeLines(capture.output(sessionInfo()),'results/R_session_info.txt')
writeLines(system.file('jri',package='rJava'),'results/jri_path.txt')
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
 'https://ccl.northwestern.edu/netlogo/6.2.1/NetLogo-6.2.1-64.tgz' -o dependencies/NetLogo-6.2.1-64.tgz
sha256sum dependencies/NetLogo-6.2.1-64.tgz > results/netlogo_archive.sha256
tar -xzf dependencies/NetLogo-6.2.1-64.tgz -C dependencies
NETLOGO_DIR="$(dirname "$(find "$PWD/dependencies" -name netlogo-headless.sh -type f -print -quit)")"
test -n "$NETLOGO_DIR" && test -f "$NETLOGO_DIR/netlogo-headless.sh"
for name in seed2025_NO_COMMUNICATION seed2025_COMMUNICATION seed2026_NO_COMMUNICATION seed2026_COMMUNICATION; do
  echo "=== Native NormAN: $name ==="
  (cd "$PWD" && bash "$NETLOGO_DIR/netlogo-headless.sh" --model "$PWD/upstream/base-model.nlogo" \
    --setup-file "$PWD/experiments.xml" --experiment "$name" --threads 1 \
    --table "$PWD/results/$name.csv") > "results/$name.stdout.log" 2>&1
  test -s "results/$name.csv"
done
python3 analyze_native.py
python3 - <<'PY'
import hashlib,json,platform
from pathlib import Path
root=Path('.')
files={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root/'results').glob('*')) if p.is_file()}
(root/'results/sha256.json').write_text(json.dumps({'files':files,'python':platform.python_version()},indent=2)+'\n')
PY
