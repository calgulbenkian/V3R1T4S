# Run It Yourself — `2026-10-14-anonymous-c6d1e0ab-c04fa003`

## One-Command Verification
```bash
bash verify-it-yourself/run_checks.sh
```

## Expected Output
```text
File: mixed_z2_r11_g6_N450.json (SHA-256: c04fa003c1474a615f252960788061395ba80f6bf0681572cd048990467ead63)
=== MIXED CAGE VERIFICATION: [z=2, r=11; g=6] on N=450 ===
Simple mixed graph (no parallel/opposite links): PASS (|V|=450, |E|=2475, |A|=900)
Regularity (in=2, out=2, undir=11 at all 450 vertices): PASS
Strong connectivity: PASS
Exact mixed girth (Alg A: All-roots non-backtracking meet-in-middle): 6
Exact mixed girth (Alg B: Exact integer matrix algebra): 6 (tr(T^3)=0, offdiag((T^2)*(T^2)^T - U^2)=0, tr(T^5)=0)
Explicit 6-cycle witness verified: [0, 225, 8, 233, 170, 226]
RESULT: PASS
```
