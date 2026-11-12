#!/usr/bin/env python3
"""Nexuslang v0.2 — puente: sintaxis turca completa -> Python. Indent-based, string-safe."""
import re, sys, os, tempfile, subprocess

STR = re.compile(r'("[^"]*"|\'[^\']*\'|#[^\n]*)')
LINE_PATTERNS = [
    (re.compile(r'^(\s*)tekrar\s+(\d+)\s+kez\s*:\s*$'), lambda m: m.group(1)+'for _ in range('+m.group(2)+'):'),
    (re.compile(r'^(\s*)her\s+([A-Za-z_\u00C0-\u017F][\w\u00C0-\u017F]*)\s+için\s+(.+?)\s*:\s*$'), lambda m: m.group(1)+'for '+m.group(2)+' in '+m.group(3)+':'),
    (re.compile(r'^(\s*)(.+?)\s+oldu\u011fu s\u00fcrece\s*:\s*$'), lambda m: m.group(1)+'while '+m.group(2)+':'),
    (re.compile(r'^(\s*)yoksa\s+(.+?)\s*:\s*$'), lambda m: m.group(1)+'elif '+m.group(2)+':'),
    (re.compile(r'^(\s*)getir\s+([\w.]+)\s*$'), lambda m: m.group(1)+'import '+m.group(2)),
]
WORD_OPS = [
    (r'\bb\u00fcy\u00fck e\u015fittir\b', '>='), (r'\bk\u00fc\u00e7\u00fck e\u015fittir\b', '<='),
    (r'\be\u015fittir\b', '=='), (r'\bfarkl\u0131\b', '!='),
    (r'\bb\u00fcy\u00fckt\u00fcr\b', '>'), (r'\bk\u00fc\u00e7\u00fckt\u00fcr\b', '<'),
]
KEYWORDS = [
    (r'\bfonksiyon\b', 'def'), (r'\bd\u00f6nd\u00fcr\b', 'return'),
    (r'\be\u011fer\b', 'if'), (r'\bde\u011filse\b', 'else'),
    (r'\bveya\b', 'or'), (r'\bve\b', 'and'), (r'\bde\u011fil\b', 'not'),
    (r'\byaz\b', 'print'), (r'\boku\b', 'input'),
    (r'\bdo\u011fru\b', 'True'), (r'\byanl\u0131\u015f\b', 'False'), (r'\bbo\u015f\b', 'None'),
    (r'\baral\u0131k\b', 'range'), (r'\buzunluk\b', 'len'),
    (r'\bmetin\b', 'str'), (r'\bsay\u0131\b', 'int'), (r'\bondal\u0131k\b', 'float'),
    (r'\bdene\b', 'try'), (r'\byakala\b', 'except Exception'), (r'\bsonunda\b', 'finally'),
]

def transpile(src):
    out = []
    for line in src.splitlines():
        store = []
        def keep(m):
            store.append(m.group(0)); return '\x00%d\x00' % (len(store)-1)
        l = STR.sub(keep, line)
        for pat, fn in LINE_PATTERNS:
            m = pat.match(l)
            if m: l = fn(m); break
        else:
            for p, r in WORD_OPS: l = re.sub(p, r, l)
            for p, r in KEYWORDS: l = re.sub(p, r, l)
            l = re.sub(r'^(\s*)de\u011fi\u015fken\s+', r'\1', l)
        l = re.sub(r'\x00(\d+)\x00', lambda m: store[int(m.group(1))], l)
        out.append(l)
    return "\n".join(out) + "\n"

def main():
    if len(sys.argv) < 2:
        print("Kullan\u0131m: python nexuslang.py dosya.nx [--emit]")
        sys.exit(1)
    src = open(sys.argv[1], encoding='utf-8').read()
    py = transpile(src)
    if '--emit' in sys.argv:
        print(py); return
    with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(py); tmp = f.name
    subprocess.run([sys.executable, tmp])
    os.unlink(tmp)

if __name__ == '__main__':
    main()
