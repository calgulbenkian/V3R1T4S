# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-9daa4b49`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/14x16x17_r2261_Q.json
sha256 matches INDEX.csv (9daa4b495e91e98bb5da76cff692af959885766b07e33042b353e7ea94de7b3d)
PASS file=14x16x17_r2261_Q.json format=14x16x17 rank=2261 primes=2 log2_bound=50
rank 2261 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/14x16x17_r2261_Q.json` | `(14, 16, 17)` | `Q` | **`2261`** | `2306` | `14,500,864` | yes | `PASS` |
