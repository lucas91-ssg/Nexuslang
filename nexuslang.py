#!/usr/bin/env python3
"""Nexuslang v0.1 — puente: sintaxis nativa (TR) -> Python. Indent-based, subconjunto alpha."""
import re, sys, os, tempfile, subprocess

KEYWORDS = [
    (r'\bfonksiyon\b', 'def'),
    (r'\bdöndür\b', 'return'),
    (r'\beğer\b', 'if'),
    (r'\bdeğilse\b', 'else'),
    (r'\bveya\b', 'or'),
    (r'\bve\b', 'and'),
    (r'\bdeğil\b', 'not'),
    (r'\byaz\b', 'print'),
]

def transpile(src):
    out = []
    for line in src.splitlines():
        m = re.match(r'^(\s*)tekrar\s+(\d+)\s+kez\s*:\s*$', line)
        if m:
            out.append(m.group(1) + 'for _ in range(' + m.group(2) + '):')
            continue
        line = re.sub(r'^(\s*)değişken\s+', r'\1', line)
        for pat, rep in KEYWORDS:
            line = re.sub(pat, rep, line)
        out.append(line)
    return "\n".join(out) + "\n"

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python nexuslang.py dosya.nx [--emit]")
        sys.exit(1)
    src = open(sys.argv[1], encoding='utf-8').read()
    py = transpile(src)
    if '--emit' in sys.argv:
        print(py)
        return
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(py)
        tmp = f.name
    subprocess.run([sys.executable, tmp])
    os.unlink(tmp)

if __name__ == '__main__':
    main()
