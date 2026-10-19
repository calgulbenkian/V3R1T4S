context: Claude Code subagent, fresh context [claude-sonnet-5-5]
cell: bklc-q4-n160-k11-d102   role: reproduce

claim.SHA256SUMS: 13 files listed, 0 not OK (checked from inside the claim folder).

## Definition (quoted from the claim's own criterion, verbatim)
"Success means a k x n generator matrix over GF(q) with these properties. (1) Rank is exactly k over GF(q), computed independently. (2) The exact minimum distance d is computed by full enumeration of all q^k - 1 nonzero codewords when feasible ..., never by sampling. (3) d is STRICTLY GREATER (direction: max) than the lower bound in the live http://www.codetables.de/ cell for (q,n,k) at verification time, and at most the upper bound. (4) The code is not one of the 7 LinCodeEvolve codes (arXiv:2609.37056) or a code derived from them, and no newer arXiv claim already reaches that d."
GF(4) here: symbol v = a + 2b stands for a + b*w with w*w = w + 1 (as stated in CLAIM.md). Clauses (3) and (4) concern the live table and the literature: I used only the live bounds recorded in table-record/ (no network; currency of the table is another skeptic's job). Clause (4) is not decidable from the folder.

## My checker (written before opening verify-it-yourself/)
rep_ws/skeptic/md4.c: reads the 11 x n matrix (made by my own rep_ws/skeptic/j2t.py from the object), packs each row as two GF(4) bit planes (a and b parts), builds the four multiples of each row (0, r, w*r, w^2*r; w*(a+bw) = b + (a+b)w; it asserts w^2*r = r + w*r), then depth-first enumerates ALL 4^k messages, XOR-accumulating (GF(4) addition), takes the weight as popcount(a OR b), and counts messages that give weight 0 (rank test: none may exist among nonzero messages). Sanity test of the program on the hexacode [6,3,4]_4: it printed min_distance=4, A_d=45, weights 4:45, 6:18 (the known enumerator), and a deliberately broken variant gave d=3.
Range checks: every matrix entry is in 0..3 and every row has length n (asserted in j2t.py and in the C reader).

## Command and real output
    python3 -I skeptic/j2t.py ../claim/object/*.json > skeptic/G.txt && cc -O2 -o skeptic/md4 skeptic/md4.c && skeptic/md4 skeptic/G.txt
n=160 k=11 messages=4194303 expected=4194303 zero_weight_nonzero_msgs=0 rank_k=true min_distance=102 A_d=2958
lowweights: 102:2958 103:2244 104:9792 105:3213

Claimed: d = 102, A_d = 2958, live lower = 101, live upper = 111 (from table-record/). My result: min distance 102, A_d 2958, messages enumerated = 4^11 - 1 (counter equals the expected number), no nonzero message gives the zero word (rank 11). Strictly above live lower: True; at most live upper: True.

## Author's checker, run only after mine (sh verify-it-yourself/run_checks.sh in the copy)
== mindist_gf4.py (exact minimum distance by full enumeration of all 4^11 messages; rank; comparison with the live bounds)
{"n": 160, "k": 11, "messages_nonzero": 4194303, "expected": 4194303, "rank_k": true, "min_distance": 102, "A_d": 2958, "claimed_d": 102}
PASS rank k: True; exact d=102; live lower=101 (d > lower: True); live upper=111 (d <= upper: True); A_d=2958
== second implementation in C (only if a C compiler is available)
n=160 k=11 messages=4194303 rank_deficient=no min_distance=102 A_d=2958
C implementation agrees
== negative control: generator row 2 replaced by a copy of row 1 (rank deficient) (must be rejected)
PASS (negative control rejected)
ALL CHECKS PASS
Agreement with mine: min distance, A_d and rank identical. No mismatch, no missing object, deterministic (both runs repeated the same numbers).

## Notes
Standard rules applied to the batch's [163,11,104]_4 (puncture 3 columns) give d 101, equal to the live lower bound 101, so 102 is not delivered by the rule; only 8 columns (as a multiset up to scalars, same basis) are shared between the two matrices.
Open question on a structurally different method (MacWilliams or Brouwer-Zimmermann): not run; my C program is a third implementation of full enumeration (own GF(4) arithmetic and own packing), so it is independent code but the same idea. Full enumeration of all 4^k codewords is exact, and the criterion allows it when feasible (4^11 is about 4.2 million).

pass: true
