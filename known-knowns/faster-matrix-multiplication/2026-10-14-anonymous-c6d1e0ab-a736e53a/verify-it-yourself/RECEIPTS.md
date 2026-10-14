# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-a736e53a`)

Command run from package root (`2026-10-14T06:20:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x14x15_m569_Z.json
sha256 matches INDEX.csv (a736e53a74f68425c0211816e0972faf8c027d4845885509b530644e9f64c52b)
PASS: object/4x14x15_m569_Z.json | format=4x14x15 class=Z max_abs=2 rank=569 | ref(Z)=572 saved=3 best_overall=557 valid_ring_upgrade=True
rank 569 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Class | Max Abs Entry | Rank `r` | Live `Z` Bar | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x14x15_m569_Z.json` | `(4, 14, 15)` | `Z` | `2` | **`569`** | `572` | `705,600` | yes | `PASS` |
