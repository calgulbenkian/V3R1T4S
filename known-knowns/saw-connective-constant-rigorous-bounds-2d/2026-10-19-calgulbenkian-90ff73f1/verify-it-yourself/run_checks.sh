#!/bin/sh
_PKG=$(cd "$(dirname "$0")/.." && pwd)
if command -v shasum >/dev/null 2>&1; then _S="shasum -a 256"; else _S="sha256sum"; fi
( cd "$_PKG" && grep "  object/" SHA256SUMS > "${TMPDIR:-/tmp}/objsums.$$" && $_S -c "${TMPDIR:-/tmp}/objsums.$$" >/dev/null 2>&1 ) || { echo "object file sha256 MISMATCH against SHA256SUMS"; echo "FAIL"; exit 1; }
# Run from anywhere: sh verify-it-yourself/run_checks.sh
# python3 3.8+, standard library only (no numpy, no network).  See REPRODUCE.md for memory and time.
set -u
HERE=$(cd "$(dirname "$0")/.." && pwd)
TMP=$(mktemp -d 2>/dev/null || mktemp -d -t v3saw)
fail=0
if command -v sha256sum >/dev/null 2>&1; then SHA="sha256sum"; else SHA="shasum -a 256"; fi
echo "== reassemble object/vector_part_*.bin and check the whole first"
WHOLE_EXP=$(grep ' WHOLE ' "$HERE/object/SHA256_PARTS.txt" | cut -d' ' -f1)
cat "$HERE"/object/vector_part_*.bin > "$TMP/vector.bin"
got=$($SHA "$TMP/vector.bin" | cut -d' ' -f1)
if [ "$got" = "$WHOLE_EXP" ]; then echo "whole object sha256 matches ($got)"; else echo "whole object sha256 MISMATCH (got $got)"; fail=1; fi
echo "== each part against object/SHA256_PARTS.txt"
bad=0
for f in "$HERE"/object/vector_part_*.bin; do
  b=$(basename "$f"); exp=$(grep " $b\$" "$HERE/object/SHA256_PARTS.txt" | cut -d' ' -f1)
  g=$($SHA "$f" | cut -d' ' -f1); [ "$g" = "$exp" ] || { echo "part $b MISMATCH"; bad=1; }
done
[ $bad -eq 0 ] && echo "all parts match" || fail=1
echo "== known-answer test: loop length 22 (39367 states, bound 138688915658/75566571101 = 1.835321010829), a few seconds"
python3 -I "$HERE/verify-it-yourself/check_saw482.py" "$HERE/known-answer/vector_k22.bin" 22 | tee "$TMP/ka.txt"
[ "$(tail -n 1 "$TMP/ka.txt")" = "PASS" ] || fail=1
echo "== negative controls (known-answer vector with state 0 set to 1)"
python3 -I -c "
import sys, lzma
b = open(sys.argv[1], 'rb').read()
raw = bytearray(lzma.decompress(b[8:])); N = len(raw) // 6
raw[5 * N + 0] = 1; raw[4 * N + 0] = 0; raw[3 * N + 0] = 0; raw[2 * N + 0] = 0; raw[1 * N + 0] = 0; raw[0] = 0   # state 0 (a seed) gets the entry 1
open(sys.argv[2], 'wb').write(b[:8] + lzma.compress(bytes(raw)))" "$HERE/known-answer/vector_k22.bin" "$TMP/neg1.bin"
python3 -I "$HERE/verify-it-yourself/check_saw482.py" "$TMP/neg1.bin" 22 > "$TMP/neg1full.txt"
if grep -q '^FAIL bound equals' "$TMP/neg1full.txt" && [ "$(tail -n 1 "$TMP/neg1full.txt")" != "PASS" ]; then echo "negative control (a vector entry changed to 1) rejected as expected"; else echo "negative control NOT rejected"; fail=1; fi
echo "== full check at the claimed loop length K = 32: regenerate 8,135,148 states, rebuild all transitions, subset-inclusion on each, exact ratio (see REPRODUCE.md for time)"
python3 -I "$HERE/verify-it-yourself/check_saw482.py" "$TMP/vector.bin" 32 | tee "$TMP/full.txt"
[ "$(tail -n 1 "$TMP/full.txt")" = "PASS" ] || fail=1
rm -f "$TMP"/*.bin "$TMP"/*.txt; rmdir "$TMP" 2>/dev/null
if [ "$fail" -eq 0 ]; then echo "ALL CHECKS PASS"; else echo "FAIL"; exit 1; fi
