# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-a3151b1a`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/15x17x17_r2463_Q.json
sha256 matches INDEX.csv (a3151b1a973de743875f597a306179204d17a61b3147991c1167e73a7806d7b9)
PASS file=15x17x17_r2463_Q.json format=15x17x17 rank=2463 primes=2 log2_bound=49
rank 2463 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/15x17x17_r2463_Q.json` | `(15, 17, 17)` | `Q` | **`2463`** | `2622` | `18,792,225` | yes | `PASS` |
