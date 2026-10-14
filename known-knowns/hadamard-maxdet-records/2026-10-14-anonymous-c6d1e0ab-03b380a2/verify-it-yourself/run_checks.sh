#!/bin/sh
set -u
HERE=$(cd "$(dirname "$0")/.." && pwd)
OBJ="$HERE/object/G81_p2.json"
CHK="$HERE/verify-it-yourself/verify_maxdet.py"

if [ ! -f "$OBJ" ]; then
  echo "FAIL missing object/G81_p2.json"
  exit 1
fi

if command -v sha256sum >/dev/null 2>&1; then
  SHA="sha256sum"
else
  SHA="shasum -a 256"
fi

fail=0
echo "== Checking object/G81_p2.json"
exp_sha=$(tail -n 1 "$HERE/INDEX.csv" | cut -d, -f7)
got_sha=$($SHA "$OBJ" | cut -d' ' -f1)
if [ "$got_sha" = "$exp_sha" ]; then
  echo "sha256 matches INDEX.csv ($got_sha)"
else
  echo "sha256 MISMATCH (got $got_sha, expected $exp_sha)"
  fail=1
fi

out=$(python3 "$CHK" --table "$HERE/verify-it-yourself/maxdet_table.json" --gram "$OBJ") || fail=1
echo "$out"

echo "== Running negative control (mutated object must FAIL)"
neg_ok=$(python3 -c '
import json, os, subprocess, sys, tempfile
obj_path, chk_path, tbl_path, is_gram = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] == "1"
with tempfile.TemporaryDirectory(prefix="neg_ctrl_") as tmp:
    neg_path = os.path.join(tmp, os.path.basename(obj_path))
    if not is_gram:
        with open(obj_path, "r", encoding="utf-8") as f:
            lines = [ln for ln in f.read().splitlines() if ln.strip() and not ln.strip().startswith("#")]
        lines[1] = lines[0]
        with open(neg_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        cmd = [sys.executable, chk_path, "--table", tbl_path, neg_path]
    else:
        with open(obj_path, "r", encoding="utf-8") as f:
            d = json.load(f)
        d["G"][0][0] += 2
        with open(neg_path, "w", encoding="utf-8") as f:
            json.dump(d, f)
        cmd = [sys.executable, chk_path, "--table", tbl_path, "--gram", neg_path]
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    print("REJECTED" if r.returncode != 0 else "ACCEPTED")
' "$OBJ" "$CHK" "$HERE/verify-it-yourself/maxdet_table.json" "1")

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
