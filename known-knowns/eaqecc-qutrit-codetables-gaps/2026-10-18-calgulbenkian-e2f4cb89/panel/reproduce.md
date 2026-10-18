# Reproduce report: qutrit-16-4-8-4

context: Claude Code subagent, fresh context
role: reproduce

Step 1: shasum -a 256 -c ../claim.SHA256SUMS run inside the claim folder: every listed file reported OK (0 failures). The claim folder was then copied to rep_ws/ and all work was done there; no network was used.

## Definition (quoted from the criterion in CLAIM.md)
"with s independent generators on Alice's n qutrits, c = rank(S J S^T)/2 (half the rank of the symplectic commutation matrix) and k = n - s + c; the minimum distance d, computed exactly as the minimum weight of vectors in the symplectic dual of span(S) that are not in the isotropic part span(S) ∩ span(S)^perp (the EAQECC definition used by Grassl), is STRICTLY GREATER (direction: max) than the table's d_lower for that (n,k,c), and d <= d_upper. Results for c = 0 are excluded."

## My checker (written before reading verify-it-yourself/)
skeptic/mycheck.py (Python, GF(3) row reduction written from scratch) and skeptic/enum.c (C enumeration). Steps: s = rank(S); G = S J S^T with J = [[0,I],[-I,0]]; c = rank(G)/2; k = n - s + c; the symplectic dual is the GF(3) null space of S J (dimension 2n - s); the isotropic part span(S) ∩ dual is obtained as {S^T y : G y = 0}; a basis of the dual is built with the isotropic part first, then a complement. enum.c visits every coefficient vector of the dual basis (3^dim vectors) whose complement coefficients are not all zero, i.e. every dual vector outside the isotropic part, and takes the minimum symplectic weight (number of positions i with (x_i, z_i) not (0,0)). The count of vectors visited is printed so it can be compared with 3^dim - 3^isotropic_dim.

Calibration (hand-derived, three tiny cases run first): (A) n=3, S = {Z1 Z2^-1, Z2 Z3^-1}: Z1 alone is in the dual and outside span(S), so d=1 (program: s=2, c=0, k=1, d=1). (B) n=3, S = {XXX, ZZZ}: weight 1 is impossible (sum of x-parts = 0 and sum of z-parts = 0), X1 X2^-1 is in the dual and outside span(S), so d=2 (program: d=2). (C) n=2, S = {X1, Z1}: s=2, c=1, k=1, dual = span{X2, Z2}, d=1 (program: s=2, c=1, k=1, d=1). All three matched.

## Command and real output
From rep_ws/skeptic: python -I mycheck.py ./enum calib, then python -I mycheck.py ./enum ../object/*.json (full saved output in rep_ws/skeptic/output.txt):

```
calibA expect s=2 c=0 k=1 d=1: n=3 s=2 rank(SJS^T)=0 c=0 k=1 dual_dim=4 radical_dim=2 | min_weight=1 count_at_min=6 vectors_tested=72
calibB expect s=2 c=0 k=1 d=2: n=3 s=2 rank(SJS^T)=0 c=0 k=1 dual_dim=4 radical_dim=2 | min_weight=2 count_at_min=24 vectors_tested=72
calibC expect s=2 c=1 k=1 d=1: n=2 s=2 rank(SJS^T)=2 c=1 k=1 dual_dim=2 radical_dim=0 | min_weight=1 count_at_min=8 vectors_tested=8
eaqecc_16_4_8_4.json: n=16 s=16 rank(SJS^T)=8 c=4 k=4 dual_dim=16 radical_dim=8 | min_weight=8 count_at_min=6528 vectors_tested=43040160
claimed n,k,c,d: 16 4 4 8
$PY -I mycheck.py ./enum ../object/*.json  3.20s user 0.08s system 97% cpu 3.353 total
```

## Clause-by-clause
- S is an integer matrix over GF(3) with 2n = 32 columns: yes (shape assertion in mycheck.py).
- Independent generators: s equals the number of rows (see output above).
- c = rank(S J S^T)/2 = 4 >= 1 and k = n - s + c = 4: reproduced above, equal to the claimed values.
- Exact minimum distance by exhaustive enumeration: d = 8 (claimed 8). I visited 43040160 = 3^16 - 3^8 vectors (all dual vectors outside the 8-dimensional isotropic part, about 43 million); the minimum weight is 8 (6528 vectors attain it). The C enumeration took 3.2 s. The membership-based numpy second method was run only on the two n=33/34 cells, not on this 3^16 case; here the enumeration visits exactly the required set (count equals 3^16 - 3^8), the three calibrations pass, and the author's separate checker agrees.
- Table comparison, as stated in CLAIM.md for the cell [[16,4,7-9;4]]_3: d_lower = 7 < 8 <= d_upper = 9. I did not fetch the live table (not part of this role).

## Author's own run (after my checker)
PY set to the venv python, bash verify-it-yourself/run_checks.sh from rep_ws (saved in rep_ws/skeptic/author_run.txt); a first run with the system python only failed on a numpy import, which I corrected by setting PY.

```
sha256 matches INDEX.csv (e2f4cb89b2b3c23d00e39c2126d5a3e094a9613fece4ba104dac17084c0e88c7)
== calibration on hand-derived cases
EA n=2 {X1X2, Z1Z2} s,c,k,d = (2, 1, 1, 2) expected (2, 1, 1, 2) OK
EA n=2 {X1, Z1} s,c,k,d = (2, 1, 1, 1) expected (2, 1, 1, 1) OK
cyclic [[5,1,3]]_3 s,c,k,d = (4, 0, 1, 3) expected (4, 0, 1, 3) OK
CALIBRATION PASS
== check_eaqecc.py on object/eaqecc_16_4_8_4.json (table cell dlower-dupper = 7-9)
file eaqecc_16_4_8_4.json n 16 s 16 c 4 k 4 dual_dim 16 isotropic_dim 8
exact minimum distance d = 8 (2.6 s)
  c>=1 True
  d==d_claimed True
  d>table_d_lower(7) True
  d<=table_d_upper(9) True
[[16,4,8;4]]_3 PASS
== negative control: a copy with one matrix entry changed must FAIL
negative control rejected as expected: FAIL
ALL CHECKS PASS
```

## Result
No mismatch. My independent checker and the author's checker agree on s, c, k and d. My exhaustive C enumeration gives d = 8.

pass: true
