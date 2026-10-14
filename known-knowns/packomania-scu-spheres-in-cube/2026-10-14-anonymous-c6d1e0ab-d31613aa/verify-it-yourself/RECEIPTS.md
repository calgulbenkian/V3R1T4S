# Verification Receipts — `2026-10-14-anonymous-c6d1e0ab-d31613aa`

## Command
```bash
bash verify-it-yourself/run_checks.sh
```

## Exact Output
```text
File: scu470.txt (SHA-256: d31613aa605c97184a2a8650cd9c6141671d413cb35a6802838201698e3091eb)
=== PACKOMANIA SCU VERIFICATION: N=470 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.067898240894670536184764825826
Candidate r_pair (min ||c_i-c_j||/2): 0.067898241049419029535261829608
Candidate r_bound (1/2 - max |c_i|):  0.067898241049419029535261829608
Candidate exact feasible r* (50+d):   0.06789824104941902953526182960800103
Candidate total_sq_norm (35d):        106.20474857724859263866386663746301111
Contacts (tol=1e-12): pair_contacts=352, boundary_contacts=79, total=431
Posted scu470.txt calibration |r_seed - r_table| = 8.213e-32: PASS
Non-isometry check (max sorted pairwise distance diff = 1.961193e-02): PASS
Radius improvement (r* - r_table):    +0.000000000154748493350497003782 (1.547485e-10)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=470 r*=0.067898241049419029535261829608 verified
```
