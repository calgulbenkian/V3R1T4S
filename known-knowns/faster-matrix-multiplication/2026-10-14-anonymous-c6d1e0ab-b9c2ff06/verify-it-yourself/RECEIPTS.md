# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-b9c2ff06`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/15x15x17_r2257_Q.json
sha256 matches INDEX.csv (b9c2ff0681dca344541f2bb281f4fc6e7ebd9e3762160ba1a29f58a814f2d8af)
PASS file=15x15x17_r2257_Q.json format=15x15x17 rank=2257 primes=2 log2_bound=50
rank 2257 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/15x15x17_r2257_Q.json` | `(15, 15, 17)` | `Q` | **`2257`** | `2320` | `14,630,625` | yes | `PASS` |
