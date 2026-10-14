# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-bed17451`)

Command run from package root (`2026-10-14T06:20:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/9x13x14_m1039_Z.json
sha256 matches INDEX.csv (bed17451925a1e9a484a2848faae3aca36011203fbd9e3277c73d673a8a57daa)
PASS: object/9x13x14_m1039_Z.json | format=9x13x14 class=Z max_abs=2 rank=1039 | ref(Z)=1050 saved=11 best_overall=1024 valid_ring_upgrade=True
rank 1039 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Class | Max Abs Entry | Rank `r` | Live `Z` Bar | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/9x13x14_m1039_Z.json` | `(9, 13, 14)` | `Z` | `2` | **`1039`** | `1050` | `2,683,044` | yes | `PASS` |
