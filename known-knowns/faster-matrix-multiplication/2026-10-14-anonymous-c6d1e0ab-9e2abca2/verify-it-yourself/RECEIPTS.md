# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-9e2abca2`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json
sha256 matches INDEX.csv (9e2abca2c586a6020b90ae6e020dabb4b00f47dead9e4bea48a804452a8dfff7)
PASS: 4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json | format=4x4x6 m=73 cr=275 (U=71, V=78, W=126) fv=101 cn=534
cr 275 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x4x6_m73_cr275_fv101_cn534_ZT_reduced.json` | `(4, 4, 6)` | `73` | **`275`** | `101` | `534` | `9,216` | yes | `PASS` |
