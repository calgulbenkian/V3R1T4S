# Honesty gate (dimer-constant-cubic-lattice-rigorous-bounds)

status: CONFIRMED_PARTIAL
confirmed_scope: The monomer-dimer entropy h3 of Z^3 (growth of the total number of matchings at unit activity) satisfies h3 <= 0.7860441 by exact integer Collatz-Wielandt on the full 512-state monomer-dimer diagonal-layer matrix at (3,3), below FKLM's 0.7862023450 by 1.58e-4, resting on a written but unpublished extension of He's argument that I re-derived with no gap.

## Gate notes
- Objects: 2 files under object/ (sha256 of each in the claim folder's INDEX.csv and claim.SHA256SUMS).
- Panel verdicts: reproduce `pass: true`, novelty `pass: true`, criterion `pass: true`.
- confirmed_scope is the criterion skeptic's sentence, quoted word for word.
- The three skeptics are Claude Code general-purpose subagents, each started fresh and given only the claim folder; the object's builder (Gemini, Argon) is a different model family from every skeptic.
- Partial win p2: h3 <= 0.7860441 (exact 0.786044083040, rounded up) on the 3D monomer-dimer entropy at unit activity, below the published rigorous 0.7862023450 (Friedland and Peled; Friedland, Krop, Lundow and Markstrom) by 1.58e-4. The extension of He's argument from dimers to monomer-dimers is the author's own and unpublished; the written derivation was checked step by step by the cross-family review and by the criterion and reproduce skeptics, and the bound was recomputed on the full uncompressed 512 x 512 matrix.
- Before the panel, the four derivations were reviewed read-only by a model of a different family (OpenAI gpt-6.1-sol): it found He's Theorem 2.1 applied within its hypotheses, the periodic-slab trap avoided by He's construction, the iterated Collatz-Wielandt direction correct, and both unpublished extensions proved; it saw the derivations only, not the certificates, which the panel then checked.
