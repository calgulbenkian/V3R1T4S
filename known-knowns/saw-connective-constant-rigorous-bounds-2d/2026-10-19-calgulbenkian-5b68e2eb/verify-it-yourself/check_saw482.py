"""Standard-library checker for the (4.8^2) lattice self-avoiding-walk upper bound certificate.

Usage: python3 -I check_saw482.py STATES_BIN K [--limit N]

STATES_BIN is the concatenated object/states_part_*.bin (format: object/AUTOMATON.md).
It REBUILDS every state's transitions from the definition in AUTOMATON.md (lattice, symmetry group,
canonical form, loop-length-K pruning, chord shortcuts), checks the subset-inclusion invariant on
every transition against the decoded target state, and computes the exact maximum of
(P x)_i / x_i by integer cross-multiplication.  Last line: PASS or FAIL.
--limit N processes only the first N states (smoke test; never prints PASS).
"""
import sys, time
from fractions import Fraction

K = int(sys.argv[2])
LIMIT = None
if '--limit' in sys.argv: LIMIT = int(sys.argv[sys.argv.index('--limit') + 1])
BOUND_TO_BEAT = Fraction(182926, 100000) - Fraction(2, 1000000)

# ---------------------------------------------------------------- lattice
OFF = {  # neighbour offsets by vertex type, in the order used by the record format
    'E': ((-1, 1), (-1, -1), (1, 0)), 'N': ((1, -1), (-1, -1), (0, 1)),
    'W': ((1, 1), (1, -1), (-1, 0)), 'S': ((1, 1), (-1, 1), (0, -1))}
TYPE = {(1, 0): 'E', (2, 0): 'W', (0, 1): 'N', (0, 2): 'S'}
NBR_CACHE = {}
def nbrs(p):
    r = NBR_CACHE.get(p)
    if r is None:
        t = TYPE[(p[0] % 3, p[1] % 3)]
        r = tuple((p[0] + a, p[1] + b) for a, b in OFF[t])
        if len(NBR_CACHE) < 3000000: NBR_CACHE[p] = r
    return r
def is_vertex(p): return (p[0] % 3, p[1] % 3) in TYPE

def g(s, x, y):  # the 8 symmetries about the origin
    sx = -x if s & 1 else x
    sy = -y if s & 2 else y
    return (sy, sx) if s & 4 else (sx, sy)

# graph distance by breadth-first search from the four vertex types of the cell at the origin
DT = {}
for rep in TYPE:
    d = {rep: 0}; frontier = [rep]
    for depth in range(1, K + 6):
        nxt = []
        for p in frontier:
            for q in nbrs(p):
                if q not in d: d[q] = depth; nxt.append(q)
        frontier = nxt
    DT[rep] = d
def dist(p, q):
    bx = p[0] - p[0] % 3; by = p[1] - p[1] % 3
    return DT[(p[0] % 3, p[1] % 3)].get((q[0] - bx, q[1] - by), 9999)

fails = []
def check(ok, msg):
    print(('ok   ' if ok else 'FAIL ') + msg, flush=True)
    if not ok: fails.append(msg)

def lattice_checks():
    ok = True
    for x in range(-9, 10):
        for y in range(-9, 10):
            if not is_vertex((x, y)): continue
            for q in nbrs((x, y)):
                ok &= is_vertex(q) and (x, y) in nbrs(q)
            for s in range(8):  # symmetries and translations by 3Z^2 are automorphisms
                gp = g(s, x, y)
                ok &= is_vertex(gp) and sorted(g(s, *q) for q in nbrs((x, y))) == sorted(nbrs(gp))
            ok &= sorted((a + 3, b - 6) for a, b in nbrs((x, y))) == sorted(nbrs((x + 3, y - 6)))
    check(ok, 'lattice: adjacency symmetric and 3-regular; the 8 symmetries about the origin and translations by 3Z^2 are automorphisms (window +-9)')

def canon_key(walk):
    """Canonical key of a walk (list of points, oldest first, head last): bytes of the coordinates from head backwards."""
    L = len(walk); ax, ay = walk[-1]
    rx = ax % 3; ry = ay % 3
    tx = ax - (-1 if rx == 2 else rx); ty = ay - (-1 if ry == 2 else ry)
    cands = list(range(8))
    for i in range(L - 1, -1, -1):
        x = walk[i][0] - tx; y = walk[i][1] - ty
        vals = [(g(s, x, y), s) for s in cands]
        m = min(v for v, _ in vals)
        cands = [s for v, s in vals if v == m]
        if len(cands) == 1: break
    s = cands[0]
    out = bytearray()
    for i in range(L - 1, -1, -1):
        x, y = g(s, walk[i][0] - tx, walk[i][1] - ty)
        out.append(x + 64); out.append(y + 64)
    return bytes(out)

def decode(blob, off):
    """Record at offset off -> (points oldest first, V, next offset)."""
    L = blob[off]
    V = int.from_bytes(blob[off + 1:off + 7], 'big')
    nb = (2 * (L - 1) + 7) // 8
    bits = int.from_bytes(blob[off + 7:off + 7 + nb], 'big')
    p = (-1, 0); pts = [p]
    for i in range(L - 1):
        d = (bits >> (2 * i)) & 3
        p = nbrs(p)[d]; pts.append(p)
    pts.reverse()
    return pts, V, off + 7 + nb

def prune_key(walk):
    wL = len(walk); head = walk[-1]; start = 0
    while start < wL - 2:
        if (wL - 1 - start) + dist(walk[start], head) <= K: break
        start += 1
    return canon_key(walk[start:])

def chords(walk, depth, min_a, cands, maxc=64):
    wL = len(walk)
    idx = {p: i for i, p in enumerate(walk)}
    for a in range(min_a, wL - 3):
        bs = sorted(b for b in (idx.get(q) for q in nbrs(walk[a])) if b is not None and a + 2 <= b <= wL - 2)
        for b in bs:
            sx = walk[:a + 1] + walk[b:]
            key = prune_key(sx)
            if key not in cands and len(cands) < maxc: cands.append(key)
            if depth < 3 and (len(sx) - 1) + dist(sx[0], sx[-1]) > K:
                chords(sx, depth + 1, a, cands, maxc)

def invariant(vset, A, target):
    """exists sigma = (symmetry, translation in 3Z^2) with sigma(A) = head(target) and V(target) within sigma(V + A)."""
    hj = target[-1]
    for s in range(8):
        ga = g(s, *A)
        tx = hj[0] - ga[0]; ty = hj[1] - ga[1]
        if tx % 3 or ty % 3: continue
        img = {(g(s, *q)[0] + tx, g(s, *q)[1] + ty) for q in vset}
        img.add(hj)
        if all(t in img for t in target): return True
    return False

def main():
    t0 = time.time()
    blob = open(sys.argv[1], 'rb').read()
    lattice_checks()
    # ---- load the state list
    index = {}; Vs = []; offs = []; noncanon = []
    off = 0
    while off < len(blob):
        pts, V, nxt = decode(blob, off)
        key = bytearray()
        for x, y in reversed(pts): key.append(x + 64); key.append(y + 64)
        key = bytes(key)
        if key in index: check(False, 'duplicate state at offset %d' % off); break
        if canon_key(list(pts)) != key: noncanon.append(off)
        index[key] = len(Vs); Vs.append(V); offs.append(off); off = nxt
    N = len(Vs)
    check(not noncanon, 'every stored state is in canonical form and states are distinct (non-canonical: %d)' % len(noncanon))
    print('states read: %d, bytes %d, load %.0fs' % (N, len(blob), time.time() - t0), flush=True)
    check(min(Vs) > 0, 'all test-vector entries are positive integers (min %d, max %d)' % (min(Vs), max(Vs)))
    # ---- seeds: every directed edge of the lattice is equivalent to one of two seed states
    seed_sq = canon_key([(1, 0), (0, 1)]); seed_oct = canon_key([(1, 0), (2, 0)])
    check(seed_sq in index and seed_oct in index, 'both seed states (square edge, octagon edge) are in the list')
    edge_keys = set()
    for x in range(-12, 13):
        for y in range(-12, 13):
            if is_vertex((x, y)):
                for q in nbrs((x, y)): edge_keys.add(canon_key([(x, y), q]))
    check(edge_keys == {seed_sq, seed_oct}, 'all directed edges in window +-12 reduce to the two seed states (%d classes)' % len(edge_keys))
    heads = set()
    for x in range(-12, 13):
        for y in range(-12, 13):
            if is_vertex((x, y)): heads.add(canon_key([(x, y)]))
    check(len(heads) == 1, 'all vertices in the window are equivalent under the symmetry group (vertex-transitive): %d class' % len(heads))
    # ---- rebuild transitions
    best_n, best_d, best_i = 0, 1, -1
    ntrans = 0; ninv = 0; bad_missing = 0; bad_inv = 0; multi = 0; nonc0 = 0; maxcand = 0
    limit = N if LIMIT is None else min(N, LIMIT)
    for i in range(limit):
        pts, V, _ = decode(blob, offs[i])
        vset = set(pts); head = pts[-1]; L = len(pts)
        total = 0
        for A in nbrs(head):
            if A in vset: continue
            ex = pts + [A]
            ntrans += 1
            k0 = prune_key(ex)
            cands = [k0]
            if (len(ex) - 1) + dist(ex[0], A) > K:
                chords(ex, 1, 0, cands)
                newL = len(ex)
                for start in range(0, newL - 2):
                    if (newL - 1 - start) + dist(ex[start], A) <= K: break
                    key = canon_key(ex[start:])
                    if key in index and key not in cands and len(cands) < 32: cands.append(key)
            maxcand = max(maxcand, len(cands))
            if len(cands) > 1: multi += 1
            ok = [c for c in cands if c in index]
            if k0 not in index or len(ok) != len(cands):
                bad_missing += 1
                if bad_missing < 4: print('   candidate missing from the state list at state', i)
                if k0 not in index: continue
            jbest = min((index[c] for c in ok), key=lambda j: Vs[j])
            if jbest != index[k0]: nonc0 += 1
            tpts, _, _ = decode(blob, offs[jbest])
            ninv += 1
            if not invariant(vset, A, tpts):
                bad_inv += 1
                if bad_inv < 4: print('   invariant FAILS at state', i)
            total += Vs[jbest]
        if total * best_d > best_n * V: best_n, best_d, best_i = total, V, i
        if i % 250000 == 0 and i: print('   ... %d states, %.0fs' % (i, time.time() - t0), flush=True)
    print('transitions rebuilt %d, with more than one candidate %d, using a candidate other than the plain suffix %d, max candidates %d' % (ntrans, multi, nonc0, maxcand))
    check(bad_missing == 0, 'every candidate target is in the state list (missing: %d)' % bad_missing)
    check(bad_inv == 0, 'subset-inclusion invariant holds on all %d chosen transitions (failures: %d)' % (ninv, bad_inv))
    r = Fraction(best_n, best_d)
    print('exact max (P x)_i / x_i = %d / %d = %s = %.12f  (state index %d)' % (best_n, best_d, r, float(r), best_i))
    check(r < BOUND_TO_BEAT, 'bound %s < 1.82926 - 2e-6 (exact rational comparison)' % r)
    if LIMIT is not None:
        print('SMOKE TEST ONLY (--limit)'); return 2
    check(N == int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else True, 'state count %d' % N)
    check(K == 30 and N == 2750336, 'loop length K = 30 and 2,750,336 states, as claimed (K = %d, N = %d)' % (K, N))
    check(r == Fraction(849051343, 464433440), 'bound equals the claimed 849051343/464433440 exactly (got %s)' % r)
    print('elapsed %.0f s' % (time.time() - t0))
    print('PASS' if not fails else 'FAIL (%d)' % len(fails))
    return 0 if not fails else 1
if __name__ == '__main__':
    sys.exit(main())
