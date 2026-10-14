# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-7fad12e9`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/15x16x16_r2177_Q.json
sha256 matches INDEX.csv (7fad12e946debb23b15ffe57e5fc3f15a8f05c1859510e5aaccb9af5907618aa)
PASS file=15x16x16_r2177_Q.json format=15x16x16 rank=2177 primes=2 log2_bound=51
rank 2177 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/15x16x16_r2177_Q.json` | `(15, 16, 16)` | `Q` | **`2177`** | `2180` | `14,745,600` | yes | `PASS` |
