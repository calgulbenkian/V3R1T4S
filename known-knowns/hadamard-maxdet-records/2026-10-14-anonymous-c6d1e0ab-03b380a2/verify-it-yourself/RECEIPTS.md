# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-03b380a2`)

Command run from package root (`2026-10-14T08:15:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/G81_p2.json
sha256 matches INDEX.csv (03b380a2074785deac39cb19b68c0853cd52ea469f7b848600cc756df42c8992)
=== Exact Verification of Frozen Gram Target p2 (n=81) ===
Symmetry & mod-4 congruences : PASS (G_ii = 81, all pairwise/triple congruences hold)
Sylvester PD & Bareiss==CRT  : PASS (all 81 leading principal minors > 0)
sqrt(det G) / 2^80        : 138538465099776000000000000000000000000000000000000000 > D_rec = 107752139522048000000000000000000000000000000000000000 (improvement: 1.285714x)
Realized {-1,+1} rows M0     : PASS (80 rows >= n-2 = 79 satisfy M0 M0^T = G[:80,:80])
Constructive Q Q^T == G      : PASS (exact rational matrix with denominator 10)
Constructive P (n I_n) P^T=G : PASS (n=81=9^2, P = Q/9 has denominator 90)
PASS: CONFIRMED_PARTIAL (p2 Frozen Gram Target)
== Running negative control (mutated object must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
