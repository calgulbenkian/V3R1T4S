# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-0975cd66`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/16x18x18_r2900_Q.json
sha256 matches INDEX.csv (0975cd66f4a942c0d5fd289c59c7d5a0703e86dee33b40911924de746c679de3)
PASS file=16x18x18_r2900_Q.json format=16x18x18 rank=2900 primes=3 log2_bound=71
rank 2900 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/16x18x18_r2900_Q.json` | `(16, 18, 18)` | `Q` | **`2900`** | `2916` | `26,873,856` | yes | `PASS` |
