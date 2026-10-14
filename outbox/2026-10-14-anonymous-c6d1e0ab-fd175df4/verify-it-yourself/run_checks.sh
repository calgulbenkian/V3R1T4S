#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_bklc.py" --self-test
python3 "$DIR/verify-it-yourself/verify_bklc.py" "$DIR/object/opt_win_q2_n171_k17_d70.json"
