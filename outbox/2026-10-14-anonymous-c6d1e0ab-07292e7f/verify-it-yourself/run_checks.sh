#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_bklc.py" --self-test
python3 "$DIR/verify-it-yourself/verify_bklc.py" "$DIR/object/opt_win_q2_n174_k17_d72.json"
