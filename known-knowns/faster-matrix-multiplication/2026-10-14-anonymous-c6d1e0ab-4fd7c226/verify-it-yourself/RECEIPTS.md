# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-4fd7c226`)

Command run from package root (`2026-10-14T02:45:00Z`, macOS, Python 3.9.6, Apple clang):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/14x16x16_r2119_Q.json
sha256 matches INDEX.csv (4fd7c2264911e65fcc6cf7074e6100202786a5de6c01b85b9ac6572fdf31ba56)
PASS file=14x16x16_r2119_Q.json format=14x16x16 rank=2119 primes=3 log2_bound=65
rank 2119 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Brent Equations Checked | Primes ($p \approx 2^{30}$) | $\log_2(\prod p)$ | $\log_2(2 L (S + 1))$ | Violations | Nonzero Rank-1 Terms | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| `object/14x16x16_r2119_Q.json` | `(14, 16, 16)` | $224 \times 256 \times 224 = 12,845,056$ | $3$ | $90.0$ | $65$ | $0$ | $2119$ | yes | `PASS` |
