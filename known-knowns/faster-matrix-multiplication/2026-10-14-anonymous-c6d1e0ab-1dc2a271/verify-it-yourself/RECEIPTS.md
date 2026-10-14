# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-1dc2a271`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json
sha256 matches INDEX.csv (1dc2a27122c50cbe852e77aab752edc1d1ec1fc2f6cb9f28a6ea47926acc1a3e)
PASS: 2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json | format=2x8x8 m=100 cr=423 (U=92, V=154, W=177) fv=94 cn=608
cr 423 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/2x8x8_m100_cr423_fv94_cn608_ZT_reduced.json` | `(2, 8, 8)` | `100` | **`423`** | `94` | `608` | `16,384` | yes | `PASS` |
