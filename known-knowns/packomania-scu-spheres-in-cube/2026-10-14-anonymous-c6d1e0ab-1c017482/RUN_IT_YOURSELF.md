# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-1c017482`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu793.txt (SHA-256: 1c017482412f0f9653595e9735da2ebbb6a270defb8cbca9d5c57c0c838167ad)
=== PACKOMANIA SCU VERIFICATION: N=793 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.057356312222008810279000968621
Candidate r_pair (min ||c_i-c_j||/2): 0.057356313101938118309456188665
Candidate r_bound (1/2 - max |c_i|):  0.057356313101938118309456188665
Candidate exact feasible r* (50+d):   0.05735631310193811830945618866516716
Candidate total_sq_norm (35d):        183.72992010940995354940319621837089088
Contacts (tol=1e-12): pair_contacts=1288, boundary_contacts=186, total=1474
Posted scu793.txt calibration |r_seed - r_table| = 1.662e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 4.329656e-02): PASS
Radius improvement (r* - r_table):    +0.000000000879929308030455220044 (8.799293e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=793 r*=0.057356313101938118309456188665 verified
```
