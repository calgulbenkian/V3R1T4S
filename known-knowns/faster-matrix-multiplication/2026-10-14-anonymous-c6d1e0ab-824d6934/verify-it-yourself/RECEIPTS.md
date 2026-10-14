# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-824d6934`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/17x17x18_r2916_Q.json
sha256 matches INDEX.csv (824d69340a8b90327a8efca36e336677839b0f1048f9cfe2459a00277f922d8d)
PASS file=17x17x18_r2916_Q.json format=17x17x18 rank=2916 primes=3 log2_bound=71
rank 2916 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/17x17x18_r2916_Q.json` | `(17, 17, 18)` | `Q` | **`2916`** | `3012` | `27,060,804` | yes | `PASS` |
