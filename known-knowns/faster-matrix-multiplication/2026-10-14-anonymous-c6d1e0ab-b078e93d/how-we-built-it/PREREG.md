# Pre-Registration — Lens 1 (`representation-absorber`)

- **Frozen (UTC)**: `2026-10-14T04:30:15Z`
- **Hypothesis**: Applying 1-step, 2-step, and 3-step generalized rank-1 slice projections (`peel_census` + `project`) to the LITA square schemes `17x17x17_r2723.npz` ($\langle 17, 17, 17 : 2723 \rangle$) and `18x18x18_r3031.npz` ($\langle 18, 18, 18 : 3031 \rangle$), followed by multi-round exact rational Khatri–Rao nullspace absorption (`compute_exact_nullspace` + Rado–Edmonds `matroid_maxkill`), will produce new record bilinear schemes strictly beating both `fmm_sota.json` and `fmm.univ-lille.fr` on multiple formats with $17 \le \max(n, m, p) \le 18$ (Partial Win `p1`), and we also test alternative axis peels toward $\langle 15, 15, 16 \rangle$.
- **Evaluation**: Standalone exact CRT Brent equation checker `verify_brent.py` over $\mathbb{Q}$.
