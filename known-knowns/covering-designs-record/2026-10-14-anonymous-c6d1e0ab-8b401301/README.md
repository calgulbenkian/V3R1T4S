# Covering Design Record: `C(55, 14, 3) <= 97`

## What

Verified that claim/C_55_14_3_b97.json (4,653 bytes, SHA-256 8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb) defines a valid plain covering design for C(55, 14, 3) with b = 97 blocks of size 14 over {1, ..., 55} that covers all C(55, 3) = 26,235 3-element subsets, strictly improving by 2 blocks upon the standing best known upper bound of 99 blocks on both live coveringrepository.com and the La Jolla Covering Repository Zenodo v1.2 archive (and 101 in the dmgordo/LJCR GitHub snapshot).

In this package, the explicit block list is stored at `object/C_55_14_3_b97.json` (identical bytes, SHA-256 `8b401301e40d62ee5d6b1b91d4ce4659e9f1c0489404de6515d090ae6f6ecacb`, 4,653 bytes, `97` blocks of size `14` covering all `26,235` `3`-subsets of `1..55`).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-8b401301/`), run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements**: `python3` (3.8+, standard library only).
- **Rough laptop time**: < 1 second.
- **Expected last line**: `ALL CHECKS PASS`

## Compared To

All criterion sources were fetched live on `2026-10-14` (`08:01:00Z`, one honest GET per source, no retries; see `the-record-we-beat/README.md` and `the-record-we-beat/sources_2026-10-14T08-01-00Z.json`):

| Source | Cell | Listed Upper Bound | Our Block Count `b` | Gain | URL | UTC Fetch Time |
|---|---|---|---|---|---|---|
| `coveringrepository.com` (`m=t=3`) | `C(55, 14, 3)` | `99` | **`97`** | **`-2`** | `https://coveringrepository.com/systems.aspx` | `2026-10-14T08:01:00Z` |
| La Jolla / Gordon (`Zenodo 10.5281/zenodo.10779736` v1.2) | `C(55, 14, 3)` | `99` | **`97`** | **`-2`** | `https://zenodo.org/api/records/19735294/files/coverdata.json/content` | `2026-10-14T08:01:00Z` |
| `dmgordo/LJCR` GitHub (`coverdata.json`) | `C(55, 14, 3)` | `101` | **`97`** | **`-4`** | `https://raw.githubusercontent.com/dmgordo/LJCR/main/coverings/coverdata.json` | `2026-10-14T08:01:00Z` |
| `thebrockchain/covering-designs` | `C(55, 14, 3)` | unlisted | **`97`** | — | `https://raw.githubusercontent.com/thebrockchain/covering-designs/main/README.md` | `2026-10-14T08:01:00Z` |
| `TROPHY_CASE.md` | `C(55, 14, 3)` | unlisted | **`97`** | — | `TROPHY_CASE.md` | `2026-10-14T08:01:00Z` |

## Not Claimed

- Scope: Constructive upper bound `C(55, 14, 3) <= 97` (Schönheim lower bound `L(55, 14, 3) = 83`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive `26,235`-subset checker shipped here; not peer reviewed.

## Credits

- **D. M. Gordon**, *La Jolla Covering Repository* (`https://dmgordon.org/covering-designs/`, Zenodo `10.5281/zenodo.10779736` v1.2).
- **G. Acerbi**, *Covering Repository* (`https://coveringrepository.com/systems.aspx`).
- Contributor credit: `anonymous-c6d1e0ab`.
