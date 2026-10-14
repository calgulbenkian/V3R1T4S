# Covering Design Record: `C(45, 14, 3) <= 58`

## What

Verified that claim/C_45_14_3_b58.json (2,807 bytes, SHA-256 3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6) defines a valid plain covering design for C(45, 14, 3) with b = 58 blocks of size 14 over {1, ..., 45} that covers all C(45, 3) = 14,190 3-element subsets, strictly improving by 1 block upon the standing best known upper bound of 59 blocks on both live coveringrepository.com and the La Jolla Covering Repository Zenodo v1.2 archive (and 59 in the dmgordo/LJCR GitHub snapshot).

In this package, the explicit block list is stored at `object/C_45_14_3_b58.json` (identical bytes, SHA-256 `3679cc89320bf75dbc35662d19f4a991ec3f03fb59ee99e0afefe4eee03c95c6`, 2,807 bytes, `58` blocks of size `14` covering all `14,190` `3`-subsets of `1..45`).

## Check It Yourself

From this package folder (`2026-10-14-anonymous-c6d1e0ab-3679cc89/`), run:

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
| `coveringrepository.com` (`m=t=3`) | `C(45, 14, 3)` | `59` | **`58`** | **`-1`** | `https://coveringrepository.com/systems.aspx` | `2026-10-14T08:01:00Z` |
| La Jolla / Gordon (`Zenodo 10.5281/zenodo.10779736` v1.2) | `C(45, 14, 3)` | `59` | **`58`** | **`-1`** | `https://zenodo.org/api/records/19735294/files/coverdata.json/content` | `2026-10-14T08:01:00Z` |
| `dmgordo/LJCR` GitHub (`coverdata.json`) | `C(45, 14, 3)` | `59` | **`58`** | **`-1`** | `https://raw.githubusercontent.com/dmgordo/LJCR/main/coverings/coverdata.json` | `2026-10-14T08:01:00Z` |
| `thebrockchain/covering-designs` | `C(45, 14, 3)` | unlisted | **`58`** | — | `https://raw.githubusercontent.com/thebrockchain/covering-designs/main/README.md` | `2026-10-14T08:01:00Z` |
| `TROPHY_CASE.md` | `C(45, 14, 3)` | unlisted | **`58`** | — | `TROPHY_CASE.md` | `2026-10-14T08:01:00Z` |

## Not Claimed

- Scope: Constructive upper bound `C(45, 14, 3) <= 58` (Schönheim lower bound `L(45, 14, 3) = 45`). Does not claim optimality.
- Checked internally by three independent skeptic subagents (`panel/`) and the standalone exhaustive `14,190`-subset checker shipped here; not peer reviewed.

## Credits

- **D. M. Gordon**, *La Jolla Covering Repository* (`https://dmgordon.org/covering-designs/`, Zenodo `10.5281/zenodo.10779736` v1.2).
- **G. Acerbi**, *Covering Repository* (`https://coveringrepository.com/systems.aspx`).
- Contributor credit: `anonymous-c6d1e0ab`.
