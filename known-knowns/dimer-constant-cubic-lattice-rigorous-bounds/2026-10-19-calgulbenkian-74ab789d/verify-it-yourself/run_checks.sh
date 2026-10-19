#!/bin/sh
# Integrity first: every object/ file must match the package SHA256SUMS (added by the orchestrator, 2026-10-19).
_PKG=$(cd "$(dirname "$0")/.." && pwd)
if command -v shasum >/dev/null 2>&1; then _S="shasum -a 256"; else _S="sha256sum"; fi
( cd "$_PKG" && grep "  object/" SHA256SUMS > "${TMPDIR:-/tmp}/objsums.$$" && $_S -c "${TMPDIR:-/tmp}/objsums.$$" >/dev/null 2>&1 ) || { echo "object file sha256 MISMATCH against SHA256SUMS"; echo "FAIL"; exit 1; }
echo "all object/ files match SHA256SUMS"
# Monomer-dimer h3 bound at (3,3).  Python 3.8+ standard library only; runs in under a minute.
cd "$(dirname "$0")" || exit 1
python3 -I check_h3.py
