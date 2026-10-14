#!/bin/sh
set -eu
DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
ROOT="$(dirname "$DIR")"
OBJ_EDGES="$ROOT/object/G_14_3_N1117.edges"
OBJ_TXT="$ROOT/object/G_14_3_N1117.txt"
TBL="$DIR/live_general_cells.json"

if command -v sha256sum >/dev/null 2>&1; then
  SHA="sha256sum"
else
  SHA="shasum -a 256"
fi

exp_sha=$(tail -n 1 "$ROOT/INDEX.csv" | cut -d, -f7)
got_edges=$($SHA "$OBJ_EDGES" | cut -d' ' -f1)
got_txt=$($SHA "$OBJ_TXT" | cut -d' ' -f1)
if [ "$got_edges" != "$exp_sha" ] || [ "$got_txt" != "$exp_sha" ]; then
  echo "FAIL: sha256 mismatch (edges=$got_edges txt=$got_txt expected=$exp_sha)" >&2
  exit 1
fi

python3 "$DIR/verify_dd.py" --table-json "$TBL" "$OBJ_EDGES" 14 3
python3 "$DIR/verify_dd.py" --table-json "$TBL" "$OBJ_TXT" 14 3 >/dev/null

# Negative control 1: D-1=2 must fail
if python3 "$DIR/verify_dd.py" --table-json "$TBL" "$OBJ_EDGES" 14 2 >/dev/null 2>&1; then
  echo "FAIL: D-1=2 negative control unexpectedly passed" >&2
  exit 1
fi

echo "ALL CHECKS PASS: G_14_3_N1117.edges verified (Delta=14, D=3, N=1117 > 1116)"
