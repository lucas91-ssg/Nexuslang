#!/usr/bin/env bash
# Nexuslang v0.2 — review tour: ejemplos + tests en un comando
set -e
cd "$(dirname "$0")"
echo "== 1) merhaba.nx ==";  python nexuslang.py examples/merhaba.nx
echo "== 2) hesap.nx ==";    python nexuslang.py examples/hesap.nx
echo "== 3) oyun.nx (girdi: 9, Ada) =="; printf '9\nAda\n' | python nexuslang.py examples/oyun.nx
echo "== 4) unit tests ==";  python -m unittest discover -s tests -v
echo "== DONE: Nexuslang v0.2 tour complete =="
