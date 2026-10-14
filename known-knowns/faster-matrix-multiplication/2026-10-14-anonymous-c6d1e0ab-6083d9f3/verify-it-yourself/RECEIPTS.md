# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-6083d9f3`)

Command run from package root (`2026-10-14T06:20:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x13x15_m533_Z.json
sha256 matches INDEX.csv (6083d9f3d15c408b83094f0d8d2f48ce60ecb549856051182174e92f00aa5596)
PASS: object/4x13x15_m533_Z.json | format=4x13x15 class=Z max_abs=2 rank=533 | ref(Z)=536 saved=3 best_overall=520 valid_ring_upgrade=True
rank 533 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Class | Max Abs Entry | Rank `r` | Live `Z` Bar | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x13x15_m533_Z.json` | `(4, 13, 15)` | `Z` | `2` | **`533`** | `536` | `608,400` | yes | `PASS` |
