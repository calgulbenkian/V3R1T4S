# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-d6ed9de8`)

Command run from package root (`2026-10-14T02:45:00Z`, macOS, Python 3.9.6, Apple clang):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/13x13x14_r1499_Q.json
sha256 matches INDEX.csv (d6ed9de8a92340b0c420c42344c915b8232853aef5ecee342fef7fa0c558a5f3)
PASS file=13x13x14_r1499_Q.json format=13x13x14 rank=1499 primes=2 log2_bound=50
rank 1499 matches INDEX.csv
== Running negative control (mutated coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Brent Equations Checked | Primes ($p \approx 2^{30}$) | $\log_2(\prod p)$ | $\log_2(2 L (S + 1))$ | Violations | Nonzero Rank-1 Terms | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| `object/13x13x14_r1499_Q.json` | `(13, 13, 14)` | $169 \times 182 \times 182 = 5,597,956$ | $2$ | $60.0$ | $50$ | $0$ | $1499$ | yes | `PASS` |
