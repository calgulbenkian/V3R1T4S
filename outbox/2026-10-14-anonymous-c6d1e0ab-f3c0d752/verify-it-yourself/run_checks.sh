#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$DIR/verify-it-yourself/verify_bklc.py" --self-test
python3 "$DIR/verify-it-yourself/verify_bklc.py" "$DIR/object/win_q4_n158_k11_d100.json"
