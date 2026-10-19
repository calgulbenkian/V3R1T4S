# Monomer-dimer entropy of the cubic lattice: h3 <= 0.7860441, 1.58e-4 below the published 0.7862023450 (partial win p2)

## What

The monomer-dimer entropy h3 of Z^3 (growth of the total number of matchings at unit activity) satisfies h3 <= 0.7860441 by exact integer Collatz-Wielandt on the full 512-state monomer-dimer diagonal-layer matrix at (3,3), below FKLM's 0.7862023450 by 1.58e-4, resting on a written but unpublished extension of He's argument that I re-derived with no gap.

## Check it yourself

From this package folder, run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: python3 3.8 or later, standard library only. No network.
- **Time**: under one second to a few seconds.
- **Expected last line**: `ALL CHECKS PASS`.

## Compared to

| Source | Cell | Value | URL | UTC fetch time |
|---|---|---|---|---|
| Friedland, Krop, Lundow and Markstrom, arXiv math/0603001 v3 (11 Apr 2008), introduction | h3 upper bound | 0.7862023450 (quoted: "The numerical computations in [FP] yield the best known upper bound") | https://arxiv.org/abs/math/0603001 | 2026-10-19T05:30:56Z (HTTP 200; source archive 05:36:22Z) |
| same | h3 lower bound | 0.7849602275 | same | same |
| Friedland and Peled, arXiv math/0402009 (the paper FKLM cite as [FP]) | where the upper bound comes from | the novelty skeptic found the number 0.7862023450 in its text; the builder did not read it | https://arxiv.org/abs/math/0402009 | 2026-10-19 (novelty skeptic, abstract page and PDF) |
| arXiv export API searches for a newer or citing bound (three queries) | newest items | none newer than He on l3, h3 or l4 | https://export.arxiv.org/api/query | 2026-10-19T06:36:39Z to 06:36:49Z (HTTP 200); the novelty skeptic repeated the search about 07:12 to 07:28Z |

Margin: 0.7862023450 - 0.7860441 = 1.58e-4. Snapshot metadata with HTTP status and page sha256: the-record-we-beat/README.md. The panel's novelty report is panel/novelty.md.

## Not claimed

- This is a partial win (p2 of the target), not the main criterion. It is a bound on the monomer-dimer entropy h3 at unit activity, not on the dimer constant l3.
- It rests on a written but unpublished extension of He's argument from dimers to monomer-dimers (using the 2-lift matching inequality at unit activity on the diagonal layers). The extension is the contributor's own. The cross-family reviewer, the criterion skeptic and the reproduce skeptic each checked the written derivation step by step and found no gap, but it has not been peer reviewed or published.
- The bound was recomputed on the full, uncompressed 512 by 512 monomer-dimer matrix at cross-section (3,3). Only the (3,3) cell is claimed. RESULTS.md-style figures at larger cross-sections in the author's notes are not part of this claim and were not checked.
- The comparator 0.7862023450 is read as quoted in the 2008 paper of Friedland, Krop, Lundow and Markstrom (which attributes it to numerical computations in Friedland and Peled). Whether a later or journal-only rigorous bound exists is not settled: Lundow's work and some journal versions were not read, and the search was arXiv-based.
- Nothing here bounds h3 from below.

## Credits

- **S. Friedland and U. N. Peled**, arXiv math/0402009, https://arxiv.org/abs/math/0402009: the earlier rigorous monomer-dimer entropy computations that FKLM cite for the upper bound 0.7862023450.
- **S. Friedland, P. Krop, P. H. Lundow and K. Markstrom** (as named in the arXiv listing of math/0603001; initials as they appear in the paper), arXiv math/0603001 v3, https://arxiv.org/abs/math/0603001: the definitions of the monomer-dimer entropy and the bounds 0.7862023450 and 0.7849602275 compared against.
- **Qidong He**, arXiv 2607.28810, https://arxiv.org/abs/2607.28810: the diagonal-layer method (Theorem 2.1, Corollary 3.4) that the written extension builds on, and Theorem 2.4 as the author cites it.
- **Csikvari**, as cited by He: the 2-lift matching-polynomial inequality that He's Theorem 2.4 uses. We did not read Csikvari's paper itself.
- The contributor's team (credit name calgulbenkian; the search code was produced by the model Gemini, Argon).
- Contributor credit: `calgulbenkian`.
