context: Claude Code subagent, fresh context [claude-sonnet-5-5]

role: novelty. Cell: cubic-dimer-h3-ub-33. Target: dimer-constant-cubic-lattice-rigorous-bounds.

## Sources fetched (group-wide, novelty_ws/; attempts in FETCHLOG.txt, FETCHLOG2.txt, FETCHLOG3.txt)
Retries were allowed by the operator (2026-10-19); the arXiv export API answered 429 several times and succeeded on later tries (all attempts logged). Times are UTC, 2026-10-19, about 07:12 to 07:28.
- TROPHY_CASE.md, raw.githubusercontent.com/elder-plinius/V3R1T4S/main/TROPHY_CASE.md, 200, sha256 b946f68eb0a6...; no dimer, cubic-lattice or matching-constant row (only a degree-diameter row matched my keyword search).
- known-knowns listing, api.github.com/repos/elder-plinius/V3R1T4S/contents/known-knowns, 200, sha256 8a2927f79954...; 20 folders, none on dimers or lattice constants.
- Pull requests: not fetched from api.github.com; I used the shared snapshot prs_all.json (fetch time 2026-10-19T04:30:31Z, 473 PRs, per the group note). Keyword scan (dimer, cubic, matching, collatz, lundow, monomer, z^3, z^4) found no dimer-constant PR; the only hits are unrelated (Potts colouring bounds #460, #461, #483; stable-marriage; Hadamard; a percolation Z^3 bound #481).
- He, arXiv 2607.28810: abstract pages v1 (sha256 64dc633a6aa8...) and v2 (sha256 9d7fdac30892...), both 200. v1 submitted 30 Jul 2026, v2 11 Aug 2026 (16 KB). Abstract: "bounded above by 0.452130, improving the previous best upper bound of 0.457547 obtained by Lundow (2001)". The listing of arXiv search for the phrase "dimer constant" (arxiv.org/search, 200, sha256 eef85a8c8fa1...) returns 7 results; the only post-2015 dimer-constant paper is He (latest version 10 August 2026). The search "dimer cubic lattice upper bound" returns only He.
- arXiv export API, all:"dimer" AND all:"cubic lattice", newest first (200, sha256 50e6503d7179...): newest relevant item is He; nothing newer on bounds (the only 2026 neighbour is a physics paper on cubic dimer dynamics, 2605.15730).
- arXiv export API monomer-dimer AND entropy (200, sha256 6c82b7a2ef95...): newest rigorous-bound items are 1502.06734 (2015) and math/0603001; nothing in the last 24 months on rigorous monomer-dimer or hypercubic dimer bounds.
- Citations of 2607.28810: Semantic Scholar graph API, 200, sha256 b890c0f15f5c..., returned an empty citation list (offset 0, data empty); OpenAlex title search did not find the paper at all. These sources do not index the paper yet, so the empty list is weak evidence. The arXiv listing searches above are the real check. No citing paper found.
- Csikvari lower bound and Z^4 table: Butera, Federbush, Pernici arXiv 1305.7028 abs page (200), table text from the claim folder's table-record.
- Friedland and Peled arXiv math/0402009 and Friedland, Krop, Lundow, Markstrom arXiv math/0603001 (v3): abs pages and PDFs fetched (200; PDF sha256 1af5cabb56db... and c2aff70b2dca...), converted to text and read at the relevant lines. Also 1502.06734 (PDF sha256 e96a9c6643c4...).
unresolved: Google Scholar or journal-side citation lists for He's paper were not reachable (no browser); Lundow 2001 and Federbush-Friedland 2011 journal texts were not read; the Friedland-Peled entry of Table in math/0402009 was read, not the Journal version. A very new (days old) preprint not yet in the arXiv indexes could still exist.

## Comparator and value read
- Best published rigorous upper bound on the monomer-dimer entropy h3 at unit activity: h3 <= 0.7862023450. Source read: Friedland, Krop, Lundow, Markstrom, arXiv math/0603001 v3 (PDF text, introduction): "The numerical computations in [12] yield the best known upper bound h3 <= 0.7862023450." Reference [12] is Friedland and Peled, arXiv math/0402009; I read its PDF and found the number in its table row for cross-section (4,4) ("(4,4) 805 12.57923752 0.7862023450") and in its statement "0.7652789557 <= h3 <= 0.7862023450 (8.2)". So the comparator in the claim is confirmed at its original source (answers Q3 on the source; that paper was read here).
- Claimed: h3 <= 0.7860441 (unrounded 0.786044083039), margin 1.58e-4, from a 3 x 3 diagonal-layer matrix.
- Newer rigorous upper bound on h3? Searched: arXiv monomer-dimer entropy (API) and the arXiv phrase searches; the newest rigorous items are 1502.06734 (2015, bounds on numbers of matchings of general graphs, conjectural for k = 3, no Z^3 monomer-dimer entropy upper bound stated in the passages I read) and math/0603001 (2008). The Butera-Federbush-Pernici papers give non-rigorous estimates. He (2026) treats only dimers. No paper citing He found. No PR on this target in prs_all.json.

## Propagation test
Does a standard rule give h3 <= 0.78604 from known values? The dimer bounds on l3 are bounds on h3(1) = l3-type quantity at p = 1, and h3 >= h3(1); an upper bound on l3 does not bound h3 from above. Friedland-Peled bounds at other cross-sections are larger. Nothing in the table or pending claims implies this value. The main-win claim (l3) is for a different quantity and does not imply it.

## Open questions answered here
Q2 (is h3 the sup over densities, equal to the box limit): this is mathematical, for the criterion role; novelty-wise the quantity is the same h3 as the comparator (both defined in FKLM, introduction: h_d = sup of h_d(p)). Q3 answered above (no newer bound found; the comparator is Friedland-Peled's (4,4) entry). Q4 (symmetry expansion of the vector): not a novelty matter.

## Caveat
The coverage is arXiv plus citation indexes; journal versions (Federbush-Friedland, J. Stat. Phys. 2011) and Lundow's work were not read, and I did not find any rigorous h3 upper bound there that is stated in the sources I did read. If one existed it would have been cited as the best known in FKLM v3 (2008), which cites FP.

verdict: strictly below the only published rigorous upper bound found (0.7862023450, Friedland-Peled via FKLM) by 1.58e-4 and not implied by any known value; no competing PR or later paper found.

pass: true
