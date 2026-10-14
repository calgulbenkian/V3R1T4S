# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-71702210`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu471.txt (SHA-256: 71702210656fae6819da996508da9b9d6383404d274e8405df0a85de342f90b8)
=== PACKOMANIA SCU VERIFICATION: N=471 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.067898240894670536184764825826
Candidate r_pair (min ||c_i-c_j||/2): 0.067898241042897910706805143111
Candidate r_bound (1/2 - max |c_i|):  0.067898241042897910706805143111
Candidate exact feasible r* (50+d):   0.06789824104289791070680514311122914
Candidate total_sq_norm (35d):        106.39607068213042641161339592060476993
Contacts (tol=1e-12): pair_contacts=15, boundary_contacts=2, total=17
Posted scu471.txt calibration |r_seed - r_table| = 8.213e-32: PASS
Non-isometry check (max sorted pairwise distance diff = 3.079186e-02): PASS
Radius improvement (r* - r_table):    +0.000000000148227374522040317285 (1.482274e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=471 r*=0.067898241042897910706805143111 verified
```
