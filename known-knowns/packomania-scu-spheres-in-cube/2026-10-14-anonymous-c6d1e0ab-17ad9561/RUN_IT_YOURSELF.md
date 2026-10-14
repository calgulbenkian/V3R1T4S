# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-17ad9561`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: scu1596.txt (SHA-256: 17ad9561bd7a7f216eac6525ed3ed67de13668b78707c2187c5421ae4f40d589)
=== PACKOMANIA SCU VERIFICATION: N=1596 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Michael Goldberg
Live table radius (radius.txt): 0.045385736359615385798733074995
Candidate r_pair (min ||c_i-c_j||/2): 0.045873685240229747068212434815
Candidate r_bound (1/2 - max |c_i|):  0.045873685240229747068212434815
Candidate exact feasible r* (50+d):   0.04587368524022974706821243481491718
Candidate total_sq_norm (35d):        366.11422410010331946383182229634907980
Contacts (tol=1e-12): pair_contacts=6420, boundary_contacts=565, total=6985
Posted scu1596.txt calibration |r_seed - r_table| = 4.257e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 4.792249e-02): PASS
Radius improvement (r* - r_table):    +0.000487948880614361269479359820 (4.879489e-04)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          YES (Michael Goldberg)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION + PARTIAL WIN p1)
PASS: scu N=1596 r*=0.045873685240229747068212434815 verified
```
