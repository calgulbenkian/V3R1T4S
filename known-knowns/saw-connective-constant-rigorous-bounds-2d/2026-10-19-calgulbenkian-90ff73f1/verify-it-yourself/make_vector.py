"""Provenance tool (NOT needed to check the claim): turns a certificate written by the author's generator
(saw_bounds_2d.c, option use_bridges = 1) into the compact object vector of this folder.

Usage: python3 -I make_vector.py CERT_TXT K OUT_BIN [--verify-order]

Only the integer test vector of the certificate is kept (exactly, no rounding); the states and transitions are
dropped because the checker regenerates them.  --verify-order additionally checks, for every state of the
certificate, that its walk has the canonical key of the state with the same index in the checker's own
breadth-first order (this runs the full pass 1 of the checker; slow for large K).
Output: the 8 bytes SAW482V2 followed by one lzma stream of six byte planes (see check_saw482.decode_vector).
"""
import sys, lzma, os
here = os.path.dirname(os.path.abspath(__file__))
cert, K, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
verify = '--verify-order' in sys.argv
sys.argv = [sys.argv[0], 'unused', str(K)]
sys.path.insert(0, here)
import check_saw482 as C

Vs = []
if verify:
    import time
    C.pass1(time.time())
n = 0
with open(cert) as f:
    for line in f:
        if not line.startswith('S '): continue
        head, _ = line.split('|', 1)
        parts = head.split()
        sid = int(parts[1]); v = int(parts[2]); L = int(parts[3])
        assert sid == n, (sid, n)
        if verify:
            pts = [tuple(int(t) for t in w.split(',')) for w in parts[4:4 + L]]
            assert len(pts) == L
            assert C.canon_key(pts) == C.KEYS[sid], 'order mismatch at state %d' % sid
        Vs.append(v); n += 1
print('states', n, 'order verified' if verify else 'order not verified')
assert all(0 < v < (1 << 48) for v in Vs)
raw = b''.join(bytes((v >> (8 * (5 - j))) & 255 for v in Vs) for j in range(6))
blob = b'SAW482V2' + lzma.compress(raw, format=lzma.FORMAT_XZ, preset=9 | lzma.PRESET_EXTREME)
open(out, 'wb').write(blob)
print('wrote', out, len(blob), 'bytes for', len(Vs), 'states')
