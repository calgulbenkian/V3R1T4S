# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-82f6c819`)

Command run from package root (`2026-10-14T02:45:00Z`, macOS, Python 3.9.6, Apple clang):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/13x14x15_r1646_Q.json
sha256 matches INDEX.csv (82f6c819ed1d02c0bd1aad307a76b7bea80f2852aeab041132f584c6e1800be2)
PASS file=13x14x15_r1646_Q.json format=13x14x15 rank=1646 primes=2 log2_bound=49
rank 1646 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Brent Equations Checked | Primes ($p \approx 2^{30}$) | $\log_2(\prod p)$ | $\log_2(2 L (S + 1))$ | Violations | Nonzero Rank-1 Terms | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| `object/13x14x15_r1646_Q.json` | `(13, 14, 15)` | $182 \times 210 \times 195 = 7,452,900$ | $2$ | $60.0$ | $49$ | $0$ | $1646$ | yes | `PASS` |
