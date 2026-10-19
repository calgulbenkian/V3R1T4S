context: Claude Code subagent, fresh context [Sonnet 5.5]

# reproduce: dna-gc-n13-d9-w6

Definition (from CLAIM.md): a list of 52 quaternary words, each of length 13 over {A,C,G,T}, exactly 6 letters from {C,G}, all distinct, pairwise Hamming distance >= 9.

## Method
- Folder check: claim.SHA256SUMS verified from inside claim/ (all entries OK).
- Copied claim/ to rep_ws/. Wrote my own checker (rep_ws/skeptic scripts, run with python -I) from the definition above BEFORE opening verify-it-yourself/. The checker reads object/ as raw bytes, splits on newline, and tests: line count equals the claimed 52; all words distinct; each word has length 13, only letters A,C,G,T, exactly 6 letters in {C,G}; minimum pairwise Hamming distance over all pairs i<j (full enumeration, not a sample).
- Only then ran the author's verify-it-yourself/run_checks.sh (copy in rep_ws/).

## My checker output (rep_ws/skeptic/output.txt)
```
== dna-gc-n13-d9-w6 params n=13 d=9 w=6 rc=0 size=52
bytes 728 ends_newline True CR False
lines 52 claimed 52
min Hamming 9 min RC dist (incl x=y) n/a
RESULT OK
```

## Author's run_checks.sh
Output ended with: checker verdict PASS (VALID=True, size=52, w=6); both negative controls rejected; ALL CHECKS PASS. It agrees with my checker on every property.

## Mismatches
None. Not judged here: whether the value is current or new (other skeptics).

Open questions for the panel concerning reproduction: the CLAIM.md question on whether an independent re-implementation agrees on all conditions (GC count w = floor(n/2), pairwise distance) is answered: yes, agrees, all conditions hold exactly with the claimed size 52.

pass: true
