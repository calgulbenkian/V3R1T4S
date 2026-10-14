# Verification Receipts — `2026-10-14-anonymous-c6d1e0ab-6d1b8f32`

## Command
```bash
bash verify-it-yourself/run_checks.sh
```

## Exact Output
```text
File: scu630.txt (SHA-256: 6d1b8f3299eaf5e0b15af9d921eeb470326b168ce651e3d13588e931498384b8)
=== PACKOMANIA SCU VERIFICATION: N=630 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.061949671549650065797038760848
Candidate r_pair (min ||c_i-c_j||/2): 0.061949671758532088700924620370
Candidate r_bound (1/2 - max |c_i|):  0.061949671758532088700924620370
Candidate exact feasible r* (50+d):   0.06194967175853208870092462036991002
Candidate total_sq_norm (35d):        144.39991568215544915436883960303828671
Contacts (tol=1e-12): pair_contacts=10, boundary_contacts=4, total=14
Posted scu630.txt calibration |r_seed - r_table| = 9.098e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 2.829947e-02): PASS
Radius improvement (r* - r_table):    +0.000000000208882022903885859522 (2.088820e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=630 r*=0.061949671758532088700924620370 verified
```
