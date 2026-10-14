# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-c11e45e7`)

Command run from package root (`2026-10-14T02:45:00Z`, macOS, Python 3.9.6, Apple clang):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/14x14x15_r1715_Q.json
sha256 matches INDEX.csv (c11e45e7d7b5bd90af4d5d4f74e943bd76855bcf80599af30ffb64971485b417)
PASS file=14x14x15_r1715_Q.json format=14x14x15 rank=1715 primes=2 log2_bound=50
rank 1715 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Brent Equations Checked | Primes ($p \approx 2^{30}$) | $\log_2(\prod p)$ | $\log_2(2 L (S + 1))$ | Violations | Nonzero Rank-1 Terms | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| `object/14x14x15_r1715_Q.json` | `(14, 14, 15)` | $196 \times 210 \times 210 = 8,643,600$ | $2$ | $60.0$ | $50$ | $0$ | $1715$ | yes | `PASS` |
