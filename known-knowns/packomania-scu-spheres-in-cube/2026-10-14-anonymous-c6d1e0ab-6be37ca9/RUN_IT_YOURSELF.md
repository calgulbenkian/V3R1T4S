# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-6be37ca9`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu466.txt (SHA-256: 6be37ca99afd5dd53f5719e2a5be83c417c385742c2696ed4187ec9cfe334105)
=== PACKOMANIA SCU VERIFICATION: N=466 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.067898240894769256234850176022
Candidate r_pair (min ||c_i-c_j||/2): 0.067898241051355201396095879180
Candidate r_bound (1/2 - max |c_i|):  0.067898241051355201396095879180
Candidate exact feasible r* (50+d):   0.06789824105135520139609587917999422
Candidate total_sq_norm (35d):        104.66500305989197775279693817989790399
Contacts (tol=1e-12): pair_contacts=162, boundary_contacts=23, total=185
Posted scu466.txt calibration |r_seed - r_table| = 7.346e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 4.059495e-02): PASS
Radius improvement (r* - r_table):    +0.000000000156585945161245703158 (1.565859e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=466 r*=0.067898241051355201396095879180 verified
```
