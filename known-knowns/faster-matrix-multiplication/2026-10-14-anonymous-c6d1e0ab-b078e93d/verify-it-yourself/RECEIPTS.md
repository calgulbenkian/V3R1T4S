# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-b078e93d`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/16x17x17_r2553_Q.json
sha256 matches INDEX.csv (b078e93d7574b8328b1cf8f865170e2d8c337ccf09b1c8b29d13462a89481540)
PASS file=16x17x17_r2553_Q.json format=16x17x17 rank=2553 primes=2 log2_bound=50
rank 2553 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/16x17x17_r2553_Q.json` | `(16, 17, 17)` | `Q` | **`2553`** | `2723` | `21,381,376` | yes | `PASS` |
