# Verification Receipts — `2026-10-14-anonymous-c6d1e0ab-879cb5f7`

## Command
```bash
bash verify-it-yourself/run_checks.sh
```

## Exact Output
```text
File: mixed_z2_r8_g6_N234.json (SHA-256: 879cb5f756b16355b5afb9eb6c9f182e43eccccebd7849cf395070822a051229)
=== MIXED CAGE VERIFICATION: [z=2, r=8; g=6] on N=234 ===
Simple mixed graph (no parallel/opposite links): PASS (|V|=234, |E|=936, |A|=468)
Regularity (in=2, out=2, undir=8 at all 234 vertices): PASS
Strong connectivity: PASS
Exact mixed girth (Alg A: All-roots non-backtracking meet-in-middle): 6
Exact mixed girth (Alg B: Exact integer matrix algebra): 6 (tr(T^3)=0, offdiag((T^2)*(T^2)^T - U^2)=0, tr(T^5)=0)
Explicit 6-cycle witness verified: [0, 117, 9, 126, 35, 141]
RESULT: PASS
```
