#!/bin/sh
# Run from anywhere: sh verify-it-yourself/run_checks.sh
# python3 3.8+, standard library only. Needs about 1.5 GB of memory and about 45 MB of temporary disk.
set -u
HERE=$(cd "$(dirname "$0")/.." && pwd)
TMP=$(mktemp -d 2>/dev/null || mktemp -d -t v3saw)
fail=0
if command -v sha256sum >/dev/null 2>&1; then SHA="sha256sum"; else SHA="shasum -a 256"; fi
WHOLE_EXP=$(grep ' WHOLE ' "$HERE/object/SHA256_PARTS.txt" | cut -d' ' -f1)
echo "== reassemble object/states_part_*.bin and check the whole first"
cat "$HERE"/object/states_part_*.bin > "$TMP/states.bin"
got=$($SHA "$TMP/states.bin" | cut -d' ' -f1)
if [ "$got" = "$WHOLE_EXP" ]; then echo "whole object sha256 matches ($got)"; else echo "whole object sha256 MISMATCH (got $got)"; fail=1; fi
if [ "$fail" -ne 0 ]; then echo "FAIL"; rm -f "$TMP"/*.bin; rmdir "$TMP" 2>/dev/null; exit 1; fi
echo "== the object's definition documents (AUTOMATON.md, THEOREM.md) against their recorded sha256"
for pair in "object/AUTOMATON.md f8b00cd226e1778f098c6df886cbaf71df1b2c8dc1696de079b901675cc9197f" "object/THEOREM.md cbf72720be78a8727821903d2cfaf94b1bf33978b6aeac8bb327b87b785a63dd"; do
  f=${pair% *}; e=${pair#* }; g=$($SHA "$HERE/$f" | cut -d' ' -f1)
  if [ "$g" = "$e" ]; then echo "$f matches"; else echo "$f MISMATCH"; echo "FAIL"; rm -f "$TMP"/*.bin; rmdir "$TMP" 2>/dev/null; exit 1; fi
done
echo "== each part against object/SHA256_PARTS.txt"
bad=0
for f in "$HERE"/object/states_part_*.bin; do
  b=$(basename "$f"); exp=$(grep " $b\$" "$HERE/object/SHA256_PARTS.txt" | cut -d' ' -f1)
  g=$($SHA "$f" | cut -d' ' -f1); [ "$g" = "$exp" ] || { echo "part $b MISMATCH"; bad=1; }
done
[ $bad -eq 0 ] && echo "all parts match" || fail=1
echo "== negative controls (first 3000 states only)"
python3 -I -c "
import sys
b=bytearray(open(sys.argv[1],'rb').read()); b[1:7]=(1).to_bytes(6,'big')   # first state's vector entry set to 1
open(sys.argv[2],'wb').write(bytes(b))" "$TMP/states.bin" "$TMP/neg1.bin"
python3 -I "$HERE/verify-it-yourself/check_saw482.py" "$TMP/neg1.bin" 30 --limit 3000 > "$TMP/neg1.txt" 2>&1
if grep -q '^FAIL bound' "$TMP/neg1.txt"; then echo "negative control 1 (a vector entry set to 1) rejected as expected"; else echo "negative control 1 NOT rejected"; fail=1; fi
python3 -I -c "
import sys
b=open(sys.argv[1],'rb').read()
L=b[0]; n=7+(2*(L-1)+7)//8
open(sys.argv[2],'wb').write(b[n:])   # first record (a seed state) removed
" "$TMP/states.bin" "$TMP/neg2.bin"
python3 -I "$HERE/verify-it-yourself/check_saw482.py" "$TMP/neg2.bin" 30 --limit 3000 > "$TMP/neg2.txt" 2>&1
if grep -q '^FAIL ' "$TMP/neg2.txt"; then echo "negative control 2 (a seed state removed) rejected as expected"; else echo "negative control 2 NOT rejected"; fail=1; fi
echo "== full check: rebuild all transitions, subset-inclusion on each, exact ratio (about 10 minutes)"
python3 -I "$HERE/verify-it-yourself/check_saw482.py" "$TMP/states.bin" 30 2750336 | tee "$TMP/full.txt"
[ "$(tail -n 1 "$TMP/full.txt")" = "PASS" ] || fail=1
rm -f "$TMP"/*.bin "$TMP"/*.txt; rmdir "$TMP" 2>/dev/null
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASS"; else echo "FAIL"; exit 1; fi
