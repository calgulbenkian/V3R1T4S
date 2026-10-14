# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-ca6a9077`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu472.txt (SHA-256: ca6a9077d3d117cabe44cb177bfe495846e3e4208c782799631ce082c05d2df7)
=== PACKOMANIA SCU VERIFICATION: N=472 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.067898240894670536184764825826
Candidate r_pair (min ||c_i-c_j||/2): 0.067898240998505114761175793623
Candidate r_bound (1/2 - max |c_i|):  0.067898240998505114761175793623
Candidate exact feasible r* (50+d):   0.06789824099850511476117579362290265
Candidate total_sq_norm (35d):        106.62427411549789099021704912484505038
Contacts (tol=1e-12): pair_contacts=24, boundary_contacts=5, total=29
Posted scu472.txt calibration |r_seed - r_table| = 8.213e-32: PASS
Non-isometry check (max sorted pairwise distance diff = 4.215108e-02): PASS
Radius improvement (r* - r_table):    +0.000000000103834578576410967797 (1.038346e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=472 r*=0.067898240998505114761175793623 verified
```
