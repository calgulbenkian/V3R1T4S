# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-fd586040`)

Command run from package root (`2026-10-14T08:05:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/C_38_16_3_b25.json
sha256 matches INDEX.csv (fd58604086de7221e9e4ccea5e65d1475e75fc6e34d0efd50edff09080eb9643)
file=C_38_16_3_b25.json PASS kind=plain params=C(38,16,3) blocks=25 schonheim=19 covered=8436/8436
blocks=25 matches INDEX.csv
== Running negative control (deleting one block must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```

| File | Cell | Blocks `b` | Standing Bar | Triples Covered | SHA-256 Matches `INDEX.csv` | Verdict |
|---|---|---|---|---|---|---|
| `object/C_38_16_3_b25.json` | `C(38, 16, 3)` | **`25`** | `26` | `8,436/8,436` | yes | `PASS` |
