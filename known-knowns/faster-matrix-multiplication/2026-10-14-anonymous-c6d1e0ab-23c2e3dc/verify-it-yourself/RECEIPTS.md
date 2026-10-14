# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-23c2e3dc`)

Command run from package root (`2026-10-14T06:25:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/15x15x16_r2129_Q.json
sha256 matches INDEX.csv (23c2e3dca666f4b9e60a3f05f27534f98baba50c924b973bdc59a703f723450e)
PASS file=15x15x16_r2129_Q.json format=15x15x16 rank=2129 primes=2 log2_bound=51
rank 2129 matches INDEX.csv
== Running negative control (mutated vocab entry must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Ring | Rank `r` | Standing Record | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/15x15x16_r2129_Q.json` | `(15, 15, 16)` | `Q` | **`2129`** | `2132` | `12,960,000` | yes | `PASS` |
