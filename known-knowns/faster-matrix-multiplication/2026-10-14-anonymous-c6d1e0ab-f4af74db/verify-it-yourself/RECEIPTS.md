# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-f4af74db`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/16x17x18_r2850_Q.json
sha256 matches INDEX.csv (f4af74db369b2724e4ee67c937c5f66381994bfaf4fbfde4cce65da43d330773)
PASS file=16x17x18_r2850_Q.json format=16x17x18 rank=2850 primes=3 log2_bound=71
rank 2850 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/16x17x18_r2850_Q.json` | `(16, 17, 18)` | `Q` | **`2850`** | `2884` | `23,970,816` | yes | `PASS` |
