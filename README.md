# Nexuslang 🌉

**Program in your mother tongue. Bridge to Python.**
**Kendi ana dilinde programla. Python'a köprü kur.**

v0.2: full Turkish programs — while (`olduğu sürece`), for-in (`her X için`),
elif (`yoksa`), try/except (`dene/yakala`), input (`oku`), types
(`sayı/metin/ondalık`), booleans (`doğru/yanlış/boş`) and word operators
(`eşittir, büyüktür, küçüktür, farklı, büyük eşittir, küçük eşittir`).
The transpiler is string-safe: reserved words inside strings or comments are untouched.

## Run / Çalıştır (Termux-friendly, no build)
    python nexuslang.py examples/oyun.nx          # tam Türkçe program (girdi ister)
    python nexuslang.py examples/merhaba.nx --emit  # göster üretilen Python'u

## Keyword map v0.2 / Anahtar kelimeler
| Nexuslang (TR) | Python |
|---|---|
| `fonksiyon` | `def` |
| `döndür` | `return` |
| `eğer / yoksa / değilse` | `if / elif / else` |
| `ve / veya / değil` | `and / or / not` |
| `yaz / oku` | `print / input` |
| `doğru / yanlış / boş` | `True / False / None` |
| `sayı / metin / ondalık` | `int / str / float` |
| `aralık / uzunluk` | `range / len` |
| `tekrar N kez:` | `for _ in range(N):` |
| `her X için L:` | `for X in L:` |
| `C olduğu sürece:` | `while C:` |
| `dene / yakala / sonunda` | `try / except / finally` |
| `getir m` | `import m` |
| `değişken x = 1` | `x = 1` |
| `eşittir / farklı / büyüktür / küçüktür` | `== / != / > / <` |

## Reserved words / Ayrılmış kelimeler
Do not use as variable names: the left column above (e.g. `sayı` is `int`,
so name your variable `miktar`, not `sayı`).

## Status / Durum — honest / dürüst
v0.2 alpha: indentation-based transpiler, single-file programs, no classes yet.
Roadmap v0.3: `sınıf` + `ben` (classes/self), Turkish stdlib, and **kabuk** —
a standalone Nexuslang REPL/interpreter (AST + tree-walk, no Python dependency),
with errors explained in Turkish.

## Author
Lucas Guzmán · Buenos Aires · also building NexusShop (Pakistan marketplace)
MIT License (to be added in v0.3)
