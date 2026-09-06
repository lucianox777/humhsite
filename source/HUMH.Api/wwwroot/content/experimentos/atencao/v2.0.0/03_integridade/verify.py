#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys

root = Path(__file__).resolve().parents[1]
sumfile = root / "03_integridade" / "SHA256SUMS.txt"
lockfile = root / "02_dependencias" / "DEPENDENCIES.lock.json"
errors = []

def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

for line in sumfile.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    expected, rel = line.split("  ", 1)
    p = root / rel
    if not p.exists():
        errors.append(f"MISSING: {rel}")
    elif sha256(p) != expected:
        errors.append(f"HASH MISMATCH: {rel}")

lock = json.loads(lockfile.read_text(encoding="utf-8"))
for dep in lock["active_canonical_dependencies"]:
    p = root / dep["path"]
    if not p.exists():
        errors.append(f"ACTIVE DEPENDENCY MISSING: {dep['artifact_id']}")
    elif sha256(p) != dep["sha256"]:
        errors.append(f"CANONICAL HASH MISMATCH: {dep['artifact_id']}")

if errors:
    print("FAIL")
    print("\n".join(errors))
    sys.exit(1)

print("PASS")
print("All materialized files and both active canonical dependencies match their SHA-256 locks.")
