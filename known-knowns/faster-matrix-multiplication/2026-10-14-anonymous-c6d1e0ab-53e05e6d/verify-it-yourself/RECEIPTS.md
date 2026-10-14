# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-53e05e6d`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/15x16x17_r2313_Q.json
sha256 matches INDEX.csv (53e05e6d257401e1089d7ace8d42b7cbde78f8992e90223791fea6c1df50da57)
PASS file=15x16x17_r2313_Q.json format=15x16x17 rank=2313 primes=2 log2_bound=50
rank 2313 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/15x16x17_r2313_Q.json` | `(15, 16, 17)` | `Q` | **`2313`** | `2448` | `16,646,400` | yes | `PASS` |
