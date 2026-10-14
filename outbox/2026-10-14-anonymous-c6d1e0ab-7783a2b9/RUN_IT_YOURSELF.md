# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-7783a2b9`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: mixed_z2_r7_g6_N184.json (SHA-256: 7783a2b9dcaf14fc309c663a27ac902e46db4a06bb77959fb7814be6fdcea2ab)
=== MIXED CAGE VERIFICATION: [z=2, r=7; g=6] on N=184 ===
Simple mixed graph (no parallel/opposite links): PASS (|V|=184, |E|=644, |A|=368)
Regularity (in=2, out=2, undir=7 at all 184 vertices): PASS
Strong connectivity: PASS
Exact mixed girth (Alg A: All-roots non-backtracking meet-in-middle): 6
Exact mixed girth (Alg B: Exact integer matrix algebra): 6 (tr(T^3)=0, offdiag((T^2)*(T^2)^T - U^2)=0, tr(T^5)=0)
Explicit 6-cycle witness verified: [0, 92, 18, 110, 36, 109]
RESULT: PASS
```
