context: Claude Code subagent, fresh context
role: criterion
cell: [[49,38]] qubit stabilizer code, target codetables-binary-linear, win p1

Read only this cell's claim folder (hashes in claim.SHA256SUMS verified OK). One live fetch per cell was made, saved under criterion_ws/ (a folder shared by the group): codetables.de QECC page, form parameter q=4 (the form's code for qubit codes), n=49, k=38; fetch log in criterion_ws/fetchlog.txt, HTTP 200, page sha256 ff9ff1bf84b2e6675377943e0e48d63951ae2b494371d62617a0fa57254f7eec. Quoted live text: "Bounds on [[49,38]] 2 lower bound: 3 upper bound: 4", construction listed as "[[49, 38, 3]] quantum code". This matches the folder's table-record.

p1, verbatim: "A quantum-code record: an explicit stabilizer code [[n,k,d]] (symplectic self-orthogonality checked exactly, minimum distance computed exactly) whose d is strictly greater than the lower bound in the live codetables.de quantum-code table for that (n,k)."

Clause check (my own program criterion_ws/chk.py, written without opening the author's verifier or receipts; output in criterion_ws/chk_output.txt):
- explicit stabilizer code: met. The entry n=49, k=38 has 11 generators as binary HX/HZ rows and as Pauli strings; the strings match the rows exactly.
- symplectic self-orthogonality checked exactly: met. All pairs of the 11 generators commute.
- independence and k = n - 11: met. GF(2) rank is 11 = n - k.
- minimum distance computed exactly: met. Exhaustive over every Pauli of weight 1, 2 and 3 (all positions, all X/Y/Z choices): none has zero syndrome, so no logical of weight 3 or less (pure to 4). A weight-4 Pauli with zero syndrome and outside the stabilizer group (rank goes from 11 to 12) was found by meet-in-the-middle, so d = 4 exactly. Minimum stabilizer weight is 31, consistent with purity. My output line: 49 38 declared 38 commute True rank 11 n-k 11 strings_match True zero-syndrome wt<=3: 0 wt4 logical found True min wt S 31 dec_dist 4
- d strictly greater than the live lower bound for that (n,k): met. 4 > 3 on the page fetched now.
- d at most the upper bound: met. 4 = 4, so the cell closes.
- Not implied by propagation: met as far as I could test. I fetched the live neighbouring cells (n,k+1), (n-1,k), and the corresponding neighbours of the other five cells: all show lower bound 3 (for example [[36,26]], [[37,27]], [[38,28]], [[39,29]], [[42,32]] to [[49,39]]). Nearby live d=4 cells with n-k = 11 are [[36,25]], [[40,29]], [[50,39]], [[64,53]]; the standard rules (add a qubit, lower k) give from them only cells with larger n and smaller k, which is none of the six. I did not run a full-table closure and rely on the triage agent's closure program for the remainder.
- Bank criterion items (1) to (4) belong to the main win (linear codes over GF(q)) and are not claimed; p1 is the named enumerated partial win. Whether arXiv already has such codes (the newer-claim wording of item 4) is the novelty role's question and cannot be decided from the folder.

Open questions for the panel, criterion-relevant answers:
1. Yes. p1 asks only for an explicit, exactly checked stabilizer code whose d exceeds the live lower bound for its (n,k). It does not require the cell to stay open; meeting the upper bound is allowed and closes the cell.
2. p1 is stated per (n,k) cell. Each of the six has its own live row and its own code, and none follows from another of the six or from a live neighbour by the standard rules. I judge six cell-level records. They share one method and one author, so a panel that counts method-level novelty may count one family; this pass is per cell only.
3. Novelty role's question, not decided here.
4. My program is a third implementation (own syndrome enumeration for weights 1 to 3, own meet-in-the-middle weight-4 search, own GF(2) rank), independent of the triage program and of the folder's checker; it agrees. Weight 1 to 3 exhaustive plus a weight-4 element of the normalizer outside the stabilizer is a complete proof that d = 4.
5. I refetched the live cell (above); it is unchanged (lower 3, upper 4).

Hidden-quantifier hunt: the claim says pure distance 4; the object field certified_pure_distance agrees with my result. No range, exclusion or format clause of p1 is missed. The table-record URL uses form parameter q=4; the page it returns is the qubit [[49,38]] cell. The q=2 form parameter returns "currently not available", so q=4 is the correct route.

confirmed_scope: The object file's entry n=49, k=38 is a qubit stabilizer code [[49,38,4]] (11 independent commuting generators, no logical of weight 3 or less, a weight-4 logical), exactly checked here, and 4 is strictly above the live codetables.de QECC lower bound 3 for [[49,38]] (fetched 2026-10-19) and equals its upper bound; this covers only this cell under p1 and says nothing about novelty against the literature or about the other five cells.
pass: true
