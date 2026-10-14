# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-9f0a232d`)

Command run from package root (`2026-10-14T06:20:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/7x8x15_m570_Z.json
sha256 matches INDEX.csv (9f0a232de00ce5220d75097b9af6986f97d81932fa3e3718e1291d426f4caede)
PASS: object/7x8x15_m570_Z.json | format=7x8x15 class=Z max_abs=2 rank=570 | ref(Z)=571 saved=1 best_overall=557 valid_ring_upgrade=True
rank 570 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Class | Max Abs Entry | Rank `r` | Live `Z` Bar | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/7x8x15_m570_Z.json` | `(7, 8, 15)` | `Z` | `2` | **`570`** | `571` | `705,600` | yes | `PASS` |
