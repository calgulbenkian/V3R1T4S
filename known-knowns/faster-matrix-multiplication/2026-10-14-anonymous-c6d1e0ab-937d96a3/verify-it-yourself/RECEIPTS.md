# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-937d96a3`)

Command run from package root (`2026-10-14T06:20:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x13x15_m535_ZT.json
sha256 matches INDEX.csv (937d96a3adc5b64e84e86d8a0d9bc0b7e160f22f00f3ca4af7239abb76a281f2)
PASS: object/4x13x15_m535_ZT.json | format=4x13x15 class=ZT max_abs=1 rank=535 | ref(ZT)=536 saved=1 best_overall=520 valid_ring_upgrade=True
rank 535 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Class | Max Abs Entry | Rank `r` | Live `ZT` Bar | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x13x15_m535_ZT.json` | `(4, 13, 15)` | `ZT` | `1` | **`535`** | `536` | `608,400` | yes | `PASS` |
