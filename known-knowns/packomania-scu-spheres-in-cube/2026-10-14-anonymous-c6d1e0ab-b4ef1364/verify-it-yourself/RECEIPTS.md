# Verification Receipts — `2026-10-14-anonymous-c6d1e0ab-b4ef1364`

## Command
```bash
bash verify-it-yourself/run_checks.sh
```

## Exact Output
```text
File: scu812.txt (SHA-256: b4ef136473f35c336af549b452ceb08996ed207204969e68c194e2cbdbea700c)
=== PACKOMANIA SCU VERIFICATION: N=812 in [-1/2, 1/2]^3 ===
Live table author (author.txt): Eckard Specht
Live table radius (radius.txt): 0.056959450361781703936323533204
Candidate r_pair (min ||c_i-c_j||/2): 0.056962823157162590720289755717
Candidate r_bound (1/2 - max |c_i|):  0.056962823157162590720289755717
Candidate exact feasible r* (50+d):   0.05696282315716259072028975571734638
Candidate total_sq_norm (35d):        189.08324279517268456877567117282260657
Contacts (tol=1e-12): pair_contacts=2, boundary_contacts=2, total=4
Posted scu812.txt calibration |r_seed - r_table| = 4.596e-31: PASS
Non-isometry check (max sorted pairwise distance diff = 7.253612e-02): PASS
Radius improvement (r* - r_table):    +0.000003372795380886783966222513 (3.372795e-06)
Threshold check (gain >= 1e-11):      PASS
Partial Win p1 author check:          NO (Eckard Specht)
Queue Rule caveat: Category `scu` has 0 explicit entries on pending-requests.html (08-Oct-2026); caveat noted for unspecified 26-Sep-2026 'Moki & Julio *many* 4666 candidates' bundle.
RESULT: PASS (CONFIRMED_SOLUTION)
PASS: scu N=812 r*=0.056962823157162590720289755717 verified
```
