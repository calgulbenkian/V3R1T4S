# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-277bfc6a`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu632.txt (SHA-256: 277bfc6a2364e3872f20f42731ccc6e4c5de4cd564814081cf7a3f6398c4b320)
=== PACKOMANIA SCU VERIFICATION: N=632 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.061949671549647706846377765805
Candidate r_pair (min ||c_i-c_j||/2): 0.061949671758524842833475299750
Candidate r_bound (1/2 - max |c_i|):  0.061949671758524842833475299750
Candidate exact feasible r* (50+d):   0.06194967175852484283347529974994156
Candidate total_sq_norm (35d):        144.81439559323754533336816961716098895
Contacts (tol=1e-12): pair_contacts=10, boundary_contacts=4, total=14
Posted scu632.txt calibration |r_seed - r_table| = 5.390e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 2.952880e-02): PASS
Radius improvement (r* - r_table):    +0.000000000208877135987097533945 (2.088771e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=632 r*=0.061949671758524842833475299750 verified
```
