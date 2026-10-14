# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-3536e50d`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
VALID PACKING: d=4 N=170
  r* (25 digits) = 0.2156450594683900081281903
  r_pair         = 0.2156450643699256506885231 (pair (8, 69))
  r_wall         = 0.2156450594683900081281903 (sphere 162)
  total_sq_norm  = 95.6294526810582612158986949
  contacts       = 150 wall, 459 pair, 10 rattlers (tol=1e-7)
  r_table(d=4, N=170) = 0.215589695168 (author: Eckard Specht)
  gain (r* - r_table)  = +0.0000553643003900081281903 (+5.536430e-05)
  max sorted pairwise-distance diff vs posted hsp4-170.txt (raw_d=4) = 9.031040e-03
  non_isometric (> 1e-8) = True
  >>> RECORD CONFIRMED: beats live table by 5.536430e-05 >= 1e-10 and is non-isometric! <<<
PASS: hsp4 N=170 r*=0.2156450594683900081281903 verified
```
