# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-e25137a3`)

Command run from package root (`2026-10-14T06:20:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/9x11x14_m889_Z.json
sha256 matches INDEX.csv (e25137a39f9a642d3a93ae58337d80703f5e45c2efc48e96207d7e61aeb101e5)
PASS: object/9x11x14_m889_Z.json | format=9x11x14 class=Z max_abs=2 rank=889 | ref(Z)=900 saved=11 best_overall=882 valid_ring_upgrade=True
rank 889 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Class | Max Abs Entry | Rank `r` | Live `Z` Bar | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/9x11x14_m889_Z.json` | `(9, 11, 14)` | `Z` | `2` | **`889`** | `900` | `1,920,996` | yes | `PASS` |
