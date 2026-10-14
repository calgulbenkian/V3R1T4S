#!/bin/sh
# Standalone verification script for object/A45_8_7_1910.txt.
# Verifies: (1) SHA-256 against INDEX.csv, (2) exact constant weight w=7 and pairwise distance >= 8
# across all 1823095 pairs, (3) claimed size M=1910, and (4) negative control rejection on a mutated copy.
set -u
HERE=$(cd "$(dirname "$0")/.." && pwd)
OBJ="$HERE/object/A45_8_7_1910.txt"
CHK="$HERE/verify-it-yourself/verify_cwc.py"

if [ ! -f "$OBJ" ]; then
  echo "FAIL missing object/A45_8_7_1910.txt"
  exit 1
fi

if command -v sha256sum >/dev/null 2>&1; then
  SHA="sha256sum"
else
  SHA="shasum -a 256"
fi

fail=0
echo "== Checking object/A45_8_7_1910.txt"
exp_sha=$(tail -n 1 "$HERE/INDEX.csv" | cut -d, -f7)
got_sha=$($SHA "$OBJ" | cut -d' ' -f1)
if [ "$got_sha" = "$exp_sha" ]; then
  echo "sha256 matches INDEX.csv ($got_sha)"
else
  echo "sha256 MISMATCH (got $got_sha, expected $exp_sha)"
  fail=1
fi

exp_m=$(tail -n 1 "$HERE/INDEX.csv" | cut -d, -f3)
out=$(python3 "$CHK" "$OBJ" 45 8 7) || fail=1
echo "$out"
echo "$out" | tail -n 1 | grep -q ">= $exp_m" && echo "M $exp_m matches INDEX.csv" || {
  echo "M MISMATCH (expected $exp_m)"
  fail=1
}

echo "== Running negative control (duplicate/colliding codeword must FAIL)"
neg_ok=$(python3 -c '
import os, subprocess, sys, tempfile
obj_path, chk_path = sys.argv[1], sys.argv[2]
with open(obj_path, "r", encoding="utf-8") as f:
    lines = [ln.strip() for ln in f if ln.strip()]
# Replace line 1 with a 1-bit swap of line 0 (distance 2 < d)
w0 = list(lines[0])
i1 = w0.index("1")
i0 = w0.index("0")
w0[i1], w0[i0] = "0", "1"
lines[1] = "".join(w0)
with tempfile.TemporaryDirectory(prefix="neg_ctrl_") as tmp:
    neg_path = os.path.join(tmp, "neg.txt")
    with open(neg_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    r = subprocess.run([sys.executable, chk_path, neg_path, "45", "8", "7"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print("REJECTED" if r.returncode != 0 else "ACCEPTED")
' "$OBJ" "$CHK")

if [ "$neg_ok" = "REJECTED" ]; then
  echo "negative control rejected as expected"
else
  echo "negative control PASSED (BAD)"
  fail=1
fi

if [ "$fail" -eq 0 ]; then
  echo "ALL CHECKS PASS"
  exit 0
else
  echo "CHECK FAIL"
  exit 1
fi
