# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-2ea8af5d`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu468.txt (SHA-256: 2ea8af5d391598dc221e4917930da4d42f17f9e541168d1fceed500b11975b89)
=== PACKOMANIA SCU VERIFICATION: N=468 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.067898240894769256234850175248
Candidate r_pair (min ||c_i-c_j||/2): 0.067898241051356515264205650656
Candidate r_bound (1/2 - max |c_i|):  0.067898241051356515264205650656
Candidate exact feasible r* (50+d):   0.06789824105135651526420565065642776
Candidate total_sq_norm (35d):        105.41646713756417691371865363224492625
Contacts (tol=1e-12): pair_contacts=176, boundary_contacts=23, total=199
Posted scu468.txt calibration |r_seed - r_table| = 4.527e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 8.377587e-02): PASS
Radius improvement (r* - r_table):    +0.000000000156587259029355475408 (1.565873e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=468 r*=0.067898241051356515264205650656 verified
```
