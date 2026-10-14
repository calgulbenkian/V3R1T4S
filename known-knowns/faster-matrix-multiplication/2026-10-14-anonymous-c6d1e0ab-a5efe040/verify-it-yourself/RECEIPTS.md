# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-a5efe040`)

Command run from package root (`2026-10-14T06:20:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/9x10x14_m816_ZT.json
sha256 matches INDEX.csv (a5efe04017632a0da87598ba3b2509ca66bb6fea965bb71a2faebb2aef582ab1)
PASS: object/9x10x14_m816_ZT.json | format=9x10x14 class=ZT max_abs=1 rank=816 | ref(ZT)=820 saved=4 best_overall=808 valid_ring_upgrade=True
rank 816 matches INDEX.csv
== Running negative control (mutated entry in u[0] must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Class | Max Abs Entry | Rank `r` | Live `ZT` Bar | Brent Equations Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/9x10x14_m816_ZT.json` | `(9, 10, 14)` | `ZT` | `1` | **`816`** | `820` | `1,587,600` | yes | `PASS` |
