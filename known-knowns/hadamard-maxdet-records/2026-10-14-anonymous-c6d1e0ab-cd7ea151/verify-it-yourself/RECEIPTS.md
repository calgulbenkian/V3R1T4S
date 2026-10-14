# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-cd7ea151`)

Command run from package root (`2026-10-14T08:15:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/G49_p2.json
sha256 matches INDEX.csv (cd7ea151cb23cea573fc617f983c2ce21a340dda94ec30baf82c4180c170e347)
=== Exact Verification of Frozen Gram Target p2 (n=49) ===
Symmetry & mod-4 congruences : PASS (G_ii = 49, all pairwise/triple congruences hold)
Sylvester PD & Bareiss==CRT  : PASS (all 49 leading principal minors > 0)
sqrt(det G) / 2^48        : 768469522966111493289934848 > D_rec = 635974777627126753067532288 (improvement: 1.208333x)
Realized {-1,+1} rows M0     : PASS (48 rows >= n-2 = 47 satisfy M0 M0^T = G[:48,:48])
Constructive Q Q^T == G      : PASS (exact rational matrix with denominator 6)
Constructive P (n I_n) P^T=G : PASS (n=49=7^2, P = Q/7 has denominator 42)
PASS: CONFIRMED_PARTIAL (p2 Frozen Gram Target)
== Running negative control (mutated object must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
