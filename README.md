# Nexuslang 🌉

**Program in your mother tongue. Bridge to Python.**
**Kendi ana dilinde programla. Python'a köprü kur.**

Nexuslang is a bridge language: you write code with native-language keywords
(Turkish in v0.1; Urdu next on the roadmap), and the transpiler emits clean,
readable Python so learners can cross over to the global ecosystem without
hitting an English wall first.

Nexuslang bir köprü dildir: kodu kendi ana dilinizin anahtar kelimeleriyle
yazarsınız (v0.1'de Türkçe; yol haritasında sırada Urduca), ve transpiler
okunabilir Python üretir — böylece öğrenenler, önce bir İngilizce duvarına
çarpmadan küresel ekosisteme geçebilir.

## Why / Neden
250M+ people in Pakistan and millions more worldwide never think in English.
Nexuslang lets them *think* in their language first, then migrate to
Python/JavaScript with the concepts already solid. Education, not replacement.

## Run / Çalıştır (Termux-friendly, no build)
    python nexuslang.py examples/merhaba.nx        # run
    python nexuslang.py examples/merhaba.nx --emit # show generated Python

## Keyword map (v0.1) / Anahtar kelimeler
| Nexuslang (TR) | Python |
|---|---|
| `fonksiyon` | `def` |
| `döndür` | `return` |
| `eğer` | `if` |
| `değilse` | `else` |
| `ve` / `veya` / `değil` | `and` / `or` / `not` |
| `yaz` | `print` |
| `değişken x = 1` | `x = 1` |
| `tekrar N kez:` | `for _ in range(N):` |

## Status / Durum — honest / dürüst
v0.1 alpha: indentation-based transpiler, Turkish subset, single-file programs.
No packages, no classes yet. Roadmap: Urdu syntax, AST tooling, JS target,
standard library in native keywords, MCP server for AI assistants.

## Author
Lucas Guzmán · Buenos Aires · also building NexusShop (Pakistan marketplace)
MIT License (to be added in v0.2)
