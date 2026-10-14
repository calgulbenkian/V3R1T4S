# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-b70300a4`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/14x17x17_r2403_Q.json
sha256 matches INDEX.csv (b70300a45b0a9ae1de0ce9196b43e1c546a49f072943d9f90c139e2686c7ebb9)
PASS file=14x17x17_r2403_Q.json format=14x17x17 rank=2403 primes=2 log2_bound=50
rank 2403 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/14x17x17_r2403_Q.json` | `(14, 17, 17)` | `Q` | **`2403`** | `2456` | `16,370,116` | yes | `PASS` |
