# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-e12d11fa`)

Command run from package root (`2026-10-14T07:32:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/A56_8_7_4691.txt
sha256 matches INDEX.csv (e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1)
file=A56_8_7_4691.txt sha256=e12d11fa604fd790d622442b7d96815ed8b129256b45507a9f09bff518cf27b1
F format: lines=4691 claimed_M=4691 bad_lines=0
W weight/distinct: bad_weight=0 distinct=4691
B packing: t=4 subsets=164185 distinct=164185 collisions=0
A all-pairs: words=4691 pairs=11000395 min_distance=8 need>=8 bad_pairs=0 histogram={8: 438664, 10: 1820540, 12: 4672305, 14: 4068886}
R record_check: cell=A(56,8,7) M=4691 composite_bar=4685 (Andw=0, Trophy/PR=4685) strict_beat=True
VERDICT: VALID  A(56,8,7) >= 4691
M 4691 matches INDEX.csv
== Running negative control (duplicate/colliding codeword must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Codewords `M` | Standing Bar (`TROPHY_CASE` / `Andw.html`) | Pairs Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/A56_8_7_4691.txt` | `A(56, 8, 7)` | **`4691`** | `4685` / `4674` | `11,000,395` | yes | `PASS` |
