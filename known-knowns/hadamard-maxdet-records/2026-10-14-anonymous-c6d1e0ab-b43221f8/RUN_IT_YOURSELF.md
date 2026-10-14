# Run It Yourself

## 1. Verify the Shipped Object (`object/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/M117_73659860230620869930312403886045415232575930948902221537499019577403834332848324440116.txt
sha256 matches INDEX.csv (b43221f8bfb6744869262c930cb7e1845f3a285b7f636cac39cca47844a3a3bb)
=== Exact Verification of {-1,+1} Matrix (n=117) ===
File SHA256         : b43221f8bfb6744869262c930cb7e1845f3a285b7f636cac39cca47844a3a3bb
Entries check       : PASS (all 13689 entries in {-1, +1})
Bareiss == CRT check: PASS (exact match across 27 primes)
|det(X)| / 2^116  : 73659860230620869930312403886045415232575930948902221537499019577403834332848324440116
Previous record D   : 72314994254613394470813334860641212637154205430658679584420251275641935854599391452615 (source: rokicki_best116.html)
Upper bound B_norm  : 100637963222637963009859920958577753795295722943327423237910285617343105697857847003583 (ratio R = 0.731929)
Record improvement  : 1.018597x strictly greater than best known record!
PASS: CONFIRMED_SOLUTION (New Hadamard Maximal Determinant Record)
== Running negative control (mutated object must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
