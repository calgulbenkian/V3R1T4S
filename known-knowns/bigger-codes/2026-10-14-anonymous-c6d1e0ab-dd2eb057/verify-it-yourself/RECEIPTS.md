# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-dd2eb057`)

Command run from package root (`2026-10-14T07:32:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/A35_6_6_2218.txt
sha256 matches INDEX.csv (dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e)
file=A35_6_6_2218.txt sha256=dd2eb057e40bc19bbd7f6a2838681200d6d55b4018e9b01a62082c35822e413e
F format: lines=2218 claimed_M=2218 bad_lines=0
W weight/distinct: bad_weight=0 distinct=2218
B packing: t=4 subsets=33270 distinct=33270 collisions=0
A all-pairs: words=2218 pairs=2458653 min_distance=6 need>=6 bad_pairs=0 histogram={6: 133550, 8: 523436, 10: 1087173, 12: 714494}
R record_check: cell=A(35,6,6) M=2218 composite_bar=2217 (Andw=0, Trophy/PR=2217) strict_beat=True
VERDICT: VALID  A(35,6,6) >= 2218
M 2218 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Codewords `M` | Standing Bar (`TROPHY_CASE` / `Andw.html`) | Pairs Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/A35_6_6_2218.txt` | `A(35, 6, 6)` | **`2218`** | `2217` / `2209` | `2,458,653` | yes | `PASS` |
