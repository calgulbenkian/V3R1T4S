# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-f55aeeff`)

Command run from package root (`2026-10-14T02:45:00Z`, macOS, Python 3.9.6, Apple clang):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/13x14x14_r1541_Q.json
sha256 matches INDEX.csv (f55aeeff8aa61d1b246890045a1122b4564a8a15e179adc4a2e5b8d65943081d)
PASS file=13x14x14_r1541_Q.json format=13x14x14 rank=1541 primes=2 log2_bound=50
rank 1541 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Brent Equations Checked | Primes ($p \approx 2^{30}$) | $\log_2(\prod p)$ | $\log_2(2 L (S + 1))$ | Violations | Nonzero Rank-1 Terms | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| `object/13x14x14_r1541_Q.json` | `(13, 14, 14)` | $182 \times 196 \times 182 = 6,492,304$ | $2$ | $60.0$ | $50$ | $0$ | $1541$ | yes | `PASS` |
