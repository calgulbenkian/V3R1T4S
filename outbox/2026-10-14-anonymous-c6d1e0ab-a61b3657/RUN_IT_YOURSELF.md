# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-a61b3657`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: mixed_z2_r9_g6_N294.json (SHA-256: a61b36576b49191399e6881ad34153ac1b9b9893a4513252b583b34916078d93)
=== MIXED CAGE VERIFICATION: [z=2, r=9; g=6] on N=294 ===
Simple mixed graph (no parallel/opposite links): PASS (|V|=294, |E|=1323, |A|=588)
Regularity (in=2, out=2, undir=9 at all 294 vertices): PASS
Strong connectivity: PASS
Exact mixed girth (Alg A: All-roots non-backtracking meet-in-middle): 6
Exact mixed girth (Alg B: Exact integer matrix algebra): 6 (tr(T^3)=0, offdiag((T^2)*(T^2)^T - U^2)=0, tr(T^5)=0)
Explicit 6-cycle witness verified: [0, 147, 13, 160, 78, 194]
RESULT: PASS
```
