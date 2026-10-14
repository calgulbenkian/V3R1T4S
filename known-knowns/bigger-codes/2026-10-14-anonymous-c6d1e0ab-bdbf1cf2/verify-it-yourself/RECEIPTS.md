# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-bdbf1cf2`)

Command run from package root (`2026-10-14T07:32:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/A27_8_10_1740.txt
sha256 matches INDEX.csv (bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe)
file=A27_8_10_1740.txt sha256=bdbf1cf2b34d5a2771172cea5d11fe6abcff25a0de03cc60808796fbe6e0acbe
F format: lines=1740 claimed_M=1740 bad_lines=0
W weight/distinct: bad_weight=0 distinct=1740
B packing: t=7 subsets=208800 distinct=208800 collisions=0
A all-pairs: words=1740 pairs=1512930 min_distance=8 need>=8 bad_pairs=0 histogram={8: 178567, 10: 121676, 12: 676640, 14: 245659, 16: 261670, 18: 24724, 20: 3994}
R record_check: cell=A(27,8,10) M=1740 composite_bar=1737 (Andw=0, Trophy/PR=1737) strict_beat=True
VERDICT: VALID  A(27,8,10) >= 1740
M 1740 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Codewords `M` | Standing Bar (`TROPHY_CASE` / `Andw.html`) | Pairs Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/A27_8_10_1740.txt` | `A(27, 8, 10)` | **`1740`** | `1737` / `1728` | `1,512,930` | yes | `PASS` |
