#!/bin/sh
set -u
HERE=$(cd "$(dirname "$0")/.." && pwd)
OBJ="$HERE/object/code_30_74.json"
OBJ_TXT="$HERE/object/code_30_74.txt"
CHK="$HERE/verify-it-yourself/verify_spherical.py"

if [ ! -f "$OBJ" ] || [ ! -f "$OBJ_TXT" ]; then
  echo "FAIL missing object/code_30_74.json"
  exit 1
fi

if command -v sha256sum >/dev/null 2>&1; then
  SHA="sha256sum"
else
  SHA="shasum -a 256"
fi

fail=0
echo "== Checking object/code_30_74.json"
exp_sha=$(tail -n 1 "$HERE/INDEX.csv" | cut -d, -f7)
got_sha=$($SHA "$OBJ" | cut -d' ' -f1)
if [ "$got_sha" = "$exp_sha" ]; then
  echo "sha256 matches INDEX.csv ($got_sha)"
else
  echo "sha256 MISMATCH (got $got_sha, expected $exp_sha)"
  fail=1
fi

out=$(python3 "$CHK" "$OBJ") || fail=1
echo "$out"
python3 "$CHK" --d 30 --N 74 "$OBJ_TXT" >/dev/null || fail=1

echo "== Running negative control (duplicate point must FAIL)"
neg_ok=$(python3 -c '
import json, os, subprocess, sys, tempfile
obj_path, chk_path = sys.argv[1], sys.argv[2]
with open(obj_path, "r", encoding="utf-8") as f:
    d = json.load(f)
key = "vectors" if "vectors" in d else "points"
d[key][1] = list(d[key][0])
with tempfile.TemporaryDirectory(prefix="neg_ctrl_") as tmp:
    neg_path = os.path.join(tmp, "neg.json")
    with open(neg_path, "w", encoding="utf-8") as f:
        json.dump(d, f)
    r = subprocess.run([sys.executable, chk_path, neg_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
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
