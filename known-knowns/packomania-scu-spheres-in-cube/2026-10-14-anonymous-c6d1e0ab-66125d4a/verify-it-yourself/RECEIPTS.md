# Verification Receipts — `2026-10-14-anonymous-c6d1e0ab-66125d4a`

## Command
```bash
bash verify-it-yourself/run_checks.sh
```

## Exact Output
```text
File: scu467.txt (SHA-256: 66125d4a47294cc7f8c660b9d3b7fb2816badb205eea8f7ec1ab95cbc984e096)
=== PACKOMANIA SCU VERIFICATION: N=467 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.067898240894769256234850175248
Candidate r_pair (min ||c_i-c_j||/2): 0.067898241051356988413398240298
Candidate r_bound (1/2 - max |c_i|):  0.067898241051356988413398240298
Candidate exact feasible r* (50+d):   0.06789824105135698841339824029794391
Candidate total_sq_norm (35d):        105.09606025211294794373871400098661462
Contacts (tol=1e-12): pair_contacts=168, boundary_contacts=23, total=191
Posted scu467.txt calibration |r_seed - r_table| = 3.028e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 2.837370e-03): PASS
Radius improvement (r* - r_table):    +0.000000000156587732178548065050 (1.565877e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=467 r*=0.067898241051356988413398240298 verified
```
