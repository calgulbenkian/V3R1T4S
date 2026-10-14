# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-4743db7c`)

Command run from package root (`2026-10-14T07:32:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/A52_8_7_3802.txt
sha256 matches INDEX.csv (4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c)
file=A52_8_7_3802.txt sha256=4743db7cec4929d05cba257484e8cce16c1f304d94efdb0b82d6870f191e473c
F format: lines=3802 claimed_M=3802 bad_lines=0
W weight/distinct: bad_weight=0 distinct=3802
B packing: t=4 subsets=133070 distinct=133070 collisions=0
A all-pairs: words=3802 pairs=7225701 min_distance=8 need>=8 bad_pairs=0 histogram={8: 390656, 10: 1289145, 12: 3118070, 14: 2427830}
R record_check: cell=A(52,8,7) M=3802 composite_bar=3799 (Andw=0, Trophy/PR=3799) strict_beat=True
VERDICT: VALID  A(52,8,7) >= 3802
M 3802 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Codewords `M` | Standing Bar (`TROPHY_CASE` / `Andw.html`) | Pairs Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/A52_8_7_3802.txt` | `A(52, 8, 7)` | **`3802`** | `3799` / `3797` | `7,225,701` | yes | `PASS` |
