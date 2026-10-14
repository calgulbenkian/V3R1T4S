# Verification Receipts (`2026-10-14-anonymous-c6d1e0ab-eea4180a`)

Command run from package root (`2026-10-14T08:15:00Z`, macOS, Python 3.9.6):

```sh
sh verify-it-yourself/run_checks.sh
```

Output:
```text
== Checking object/M105_402299811033982511699641115457655638247621548505385285611140221022215602176.txt
sha256 matches INDEX.csv (eea4180adc25f6e40db1e7bac9a06f7b63183141abaadbdf7d44c83af403e50b)
=== Exact Verification of {-1,+1} Matrix (n=105) ===
File SHA256         : eea4180adc25f6e40db1e7bac9a06f7b63183141abaadbdf7d44c83af403e50b
Entries check       : PASS (all 11025 entries in {-1, +1})
Bareiss == CRT check: PASS (exact match across 24 primes)
|det(X)| / 2^104  : 402299811033982511699641115457655638247621548505385285611140221022215602176
Previous record D   : 384743747284587846942188483608583600735563257274079045682562818122226665625 (source: rokicki_best104.html)
Upper bound B_norm  : 547882258728472660210324664501712688349467880552241675318385825994770342169 (ratio R = 0.734282)
Record improvement  : 1.045631x strictly greater than best known record!
PASS: CONFIRMED_SOLUTION (New Hadamard Maximal Determinant Record)
== Running negative control (mutated object must FAIL)
negative control rejected as expected
ALL CHECKS PASS
```
