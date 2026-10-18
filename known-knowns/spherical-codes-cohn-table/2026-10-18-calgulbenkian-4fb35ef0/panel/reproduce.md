# reproduce report: sc-30-64
context: Claude Code subagent, fresh context [Sonnet 5.5]

Hash check: shasum -a 256 -c claim.SHA256SUMS run inside claim/ printed no failure (all listed files OK). Claim folder copied to rep_ws/; all work done there. No network used.

Definition (quoted from CLAIM.md): "after normalizing each vector to unit length in mpmath at 50 digits the maximum pairwise inner product c* (cosine of the minimal angle) is STRICTLY LOWER (direction: min) than the table's 12-decimal cosine for (d, N) ... by at least 1e-10, AND ... the (d, N) row has NO '&ast;' (proven optimal) mark AND does NOT contain the text 'needs more optimization'".

My checker (written before opening verify-it-yourself/): rep_ws/skeptic/ (script kept outside the claim copy; output saved as rep_ws/skeptic/output.txt). It checks per object file: line count equals N; every line has exactly d comma-separated coordinates; coordinates have at least 20 significant digits; each vector normalised with mpmath at dps=50; ALL N(N-1)/2 pairwise inner products computed in mpmath (no sampling), c* = max; gain = (12-decimal /plain cosine) minus c* >= 1e-10; the plain_rows.csv cosine, the index_rows.html cosine and the cosine in CLAIM.md "Cells compared" agree as strings; the index row has no &ast; star; the row does not contain "needs more optimization"; the kissing-number exclusion (9<=d<=23 and c*<=0.5) does not apply.

Command: python3 -I mychk.py rep_ws   (interpreter: the V3R1T4S venv python). Real output (saved in rep_ws/skeptic/output.txt):
```
(d=30,N=64) lines=64 dim_ok=True min_sigdigits~27 c*=0.03821343143187027599419395 angle_deg=87.8099984399576 table=0.038215865917 gain=2.4344851e-6 gain>=1e-10:True ast=False needs_opt=False cos_consistent=True ref='Pavlos Moros, 2026.' kissing_excl=n/a ROW_OK
rows_ok 1 of 1
```

Then the author's checker: PYTHON=venv-python sh verify-it-yourself/run_checks.sh (run in rep_ws; output saved as rep_ws/skeptic/author_run.txt). Last line: ALL CHECKS PASS. Its sha256 lines: 1 ok, 0 mismatch. Its c* values agree with mine to 20 digits for 1 of 1 rows; mismatches: none.

Not judged here: whether the table value is current, and novelty (other skeptics).
Mismatches: none

pass: true
