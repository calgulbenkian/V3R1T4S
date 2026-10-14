# Run It Yourself

## 1. Verify the Shipped Object (`object/M109_2119202655125403624550373680790052808829003860176536932438843923020304438454497.txt`)

From a fresh shell inside this package directory:

```sh
sh verify-it-yourself/run_checks.sh
```

Expected output:
```text
== Checking object/M109_2119202655125403624550373680790052808829003860176536932438843923020304438454497.txt
sha256 matches INDEX.csv (0108345c2f3cbffdd58f23eef8aba73546583f02062a013a5b64ab95e198faa6)
=== Exact Verification of {-1,+1} Matrix (n=109) ===
File SHA256         : 0108345c2f3cbffdd58f23eef8aba73546583f02062a013a5b64ab95e198faa6
Entries check       : PASS (all 11881 entries in {-1, +1})
Bareiss == CRT check: PASS (exact match across 25 primes)
|det(X)| / 2^108  : 2119202655125403624550373680790052808829003860176536932438843923020304438454497
Previous record D   : 1877483841834222713683125485573890072927341503771574105042244268774869908324352 (source: rokicki_best108.html)
Upper bound B_norm  : 2896497323385832583622927428277996632836928103583147613858951575196511441468179 (ratio R = 0.731643)
Record improvement  : 1.128746x strictly greater than best known record!
PASS: CONFIRMED_SOLUTION (New Hadamard Maximal Determinant Record)
== Running negative control (mutated object must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
