# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-d9b43401`)

Command run from package root (`2026-10-14T07:32:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/A54_8_7_4204.txt
sha256 matches INDEX.csv (d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca)
file=A54_8_7_4204.txt sha256=d9b4340171c56a0ddc034dcb31cb4f568eb9c8e2fecddbb3a1871a0722356fca
F format: lines=4204 claimed_M=4204 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4204
B packing: t=4 subsets=147140 distinct=147140 collisions=0
A all-pairs: words=4204 pairs=8834706 min_distance=8 need>=8 bad_pairs=0 histogram={8: 420462, 10: 1522822, 12: 3790819, 14: 3100603}
R record_check: cell=A(54,8,7) M=4204 composite_bar=4193 (Andw=0, Trophy/PR=4193) strict_beat=True
VERDICT: VALID  A(54,8,7) >= 4204
M 4204 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Codewords `M` | Standing Bar (`TROPHY_CASE` / `Andw.html`) | Pairs Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/A54_8_7_4204.txt` | `A(54, 8, 7)` | **`4204`** | `4193` / `4173` | `8,834,706` | yes | `PASS` |
