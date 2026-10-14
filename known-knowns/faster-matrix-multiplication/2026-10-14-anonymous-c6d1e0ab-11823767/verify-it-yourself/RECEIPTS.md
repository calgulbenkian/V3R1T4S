# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-11823767`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json
sha256 matches INDEX.csv (118237670d742163d9f8caa3fd4e5c6a850fe9570fbb39ce3f32906b427c2a4a)
PASS: 5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json | format=5x5x5 m=93 cr=378 (U=100, V=103, W=175) fv=157 cn=844
cr 378 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/5x5x5_m93_cr378_fv157_cn844_ZT_reduced.json` | `(5, 5, 5)` | `93` | **`378`** | `157` | `844` | `15,625` | yes | `PASS` |
