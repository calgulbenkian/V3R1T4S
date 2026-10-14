# Verification Receipts — `2026-10-14-anonymous-c6d1e0ab-ab0e5bdc`

## Command
```bash
bash verify-it-yourself/run_checks.sh
```

## Exact Output
```text
File: scu631.txt (SHA-256: ab0e5bdcb3875d14645a826e6fcdb65ed580b92640951785e72e3d33a6c5607f)
=== PACKOMANIA SCU VERIFICATION: N=631 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.061949671549657821193834961183
Candidate r_pair (min ||c_i-c_j||/2): 0.061949671758498235727065581655
Candidate r_bound (1/2 - max |c_i|):  0.061949671758498235727065581655
Candidate exact feasible r* (50+d):   0.06194967175849823572706558165548591
Candidate total_sq_norm (35d):        144.66088490509921937392904833462756305
Contacts (tol=1e-12): pair_contacts=10, boundary_contacts=4, total=14
Posted scu631.txt calibration |r_seed - r_table| = 6.736e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 2.626935e-02): PASS
Radius improvement (r* - r_table):    +0.000000000208840414533230620472 (2.088404e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=631 r*=0.061949671758498235727065581655 verified
```
