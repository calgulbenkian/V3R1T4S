# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-4448c119`)

Command run from package root (`2026-10-14T03:55:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json
sha256 matches INDEX.csv (4448c119d128c8be762c29223b43d7486bd9bb7acc9633d9d6fd23110445aa72)
PASS: 4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json | format=4x5x7 m=104 cr=395 (U=96, V=116, W=183) fv=161 cn=931
cr 395 matches INDEX.csv
== Running negative control (mutated SLP coefficient must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Format | Rank `m` | Reduced Additions (`cr`) | Fresh Vars (`fv`) | Naive Additions (`cn`) | Brent Monomials Verified | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|---|---|
| `object/4x5x7_m104_cr395_fv161_cn931_ZT_reduced.json` | `(4, 5, 7)` | `104` | **`395`** | `161` | `931` | `19,600` | yes | `PASS` |
