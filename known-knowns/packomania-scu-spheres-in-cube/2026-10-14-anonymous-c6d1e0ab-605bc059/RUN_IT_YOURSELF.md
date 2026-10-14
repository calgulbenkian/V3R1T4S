# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-605bc059`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu101.txt (SHA-256: 605bc0591017c7a2eec3f7a37ec33b16936a3664a312bcde00b2bdf46e6538c6)
=== PACKOMANIA SCU VERIFICATION: N=101 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.110240604605984488395300868556
Candidate r_pair (min ||c_i-c_j||/2): 0.110240606233695265468856021377
Candidate r_bound (1/2 - max |c_i|):  0.110240606233695265468856021377
Candidate exact feasible r* (50+d):   0.11024060623369526546885602137676858
Candidate total_sq_norm (35d):        21.73222571192743889049858945527687589
Contacts (tol=1e-12): pair_contacts=6, boundary_contacts=4, total=10
Posted scu101.txt calibration |r_seed - r_table| = 6.781e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 3.555072e-02): PASS
Radius improvement (r* - r_table):    +0.000000001627710777073555152821 (1.627711e-09)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=101 r*=0.110240606233695265468856021377 verified
```
