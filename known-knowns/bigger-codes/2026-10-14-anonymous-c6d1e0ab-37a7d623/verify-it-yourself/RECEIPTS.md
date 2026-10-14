# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-37a7d623`)

Command run from package root (`2026-10-14T07:32:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/A55_8_7_4431.txt
sha256 matches INDEX.csv (37a7d62321644d15eb6d70962893f7fbbd59bb36b10230f74ac56902f21dc158)
file=A55_8_7_4431.txt sha256=37a7d62321644d15eb6d70962893f7fbbd59bb36b10230f74ac56902f21dc158
F format: lines=4431 claimed_M=4431 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4431
B packing: t=4 subsets=155085 distinct=155085 collisions=0
A all-pairs: words=4431 pairs=9814665 min_distance=8 need>=8 bad_pairs=0 histogram={8: 438298, 10: 1656042, 12: 4196975, 14: 3523350}
R record_check: cell=A(55,8,7) M=4431 composite_bar=4426 (Andw=0, Trophy/PR=4426) strict_beat=True
VERDICT: VALID  A(55,8,7) >= 4431
M 4431 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Codewords `M` | Standing Bar (`TROPHY_CASE` / `Andw.html`) | Pairs Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/A55_8_7_4431.txt` | `A(55, 8, 7)` | **`4431`** | `4426` / `4417` | `9,814,665` | yes | `PASS` |
