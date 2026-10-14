# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-e18e3a43`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/16x16x17_r2392_Q.json
sha256 matches INDEX.csv (e18e3a43ba7b29da2e9683b93ec8dcfabed75f35c4c6aa515dc8d7f7a4fe183b)
PASS file=16x16x17_r2392_Q.json format=16x16x17 rank=2392 primes=2 log2_bound=51
rank 2392 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/16x16x17_r2392_Q.json` | `(16, 16, 17)` | `Q` | **`2392`** | `2492` | `18,939,904` | yes | `PASS` |
