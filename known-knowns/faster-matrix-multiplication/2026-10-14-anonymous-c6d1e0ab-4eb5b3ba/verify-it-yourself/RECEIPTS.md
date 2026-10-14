# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-4eb5b3ba`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/17x18x18_r2968_Q.json
sha256 matches INDEX.csv (4eb5b3ba86815ff31b05fbb949342c14d177914edd72c52b2d41937bd04c63c8)
PASS file=17x18x18_r2968_Q.json format=17x18x18 rank=2968 primes=3 log2_bound=71
rank 2968 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/17x18x18_r2968_Q.json` | `(17, 18, 18)` | `Q` | **`2968`** | `3031` | `30,338,064` | yes | `PASS` |
