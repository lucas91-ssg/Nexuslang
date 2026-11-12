import unittest, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nexuslang import transpile

class TestTranspiler(unittest.TestCase):
    def test_fonksiyon_ve_yaz(self):
        out = transpile('fonksiyon selam(ad):\n    yaz("Merhaba " + ad)\n')
        self.assertIn('def selam(ad):', out)
        self.assertIn('print("Merhaba " + ad)', out)

    def test_kosul_ve_degilse(self):
        out = transpile('eğer x > 3:\n    yaz("büyük")\ndeğilse:\n    yaz("küçük")\n')
        self.assertIn('if x > 3:', out)
        self.assertIn('else:', out)

    def test_while_oldugu_surece(self):
        out = transpile('i < 5 olduğu sürece:\n    i = i + 1\n')
        self.assertIn('while i < 5:', out)

    def test_for_in_her_icin(self):
        out = transpile('her e için liste:\n    yaz(e)\n')
        self.assertIn('for e in liste:', out)

    def test_word_operators(self):
        out = transpile('eğer a eşittir 5 ve b farklı 2:\n    yaz(a)\n')
        self.assertIn('if a == 5 and b != 2:', out)

    def test_string_safe(self):
        out = transpile('yaz("eğer değilse yaz fonksiyon")\n')
        self.assertIn('print("eğer değilse yaz fonksiyon")', out)

    def test_tip_donushum(self):
        out = transpile('değişken n = sayı(oku("v: "))\n')
        self.assertIn('n = int(input("v: "))', out)

    def test_try_except(self):
        out = transpile('dene:\n    yaz("x")\nyakala:\n    yaz("hata")\n')
        self.assertIn('try:', out)
        self.assertIn('except Exception:', out)

    def test_tekrar_kez(self):
        out = transpile('tekrar 3 kez:\n    yaz("t")\n')
        self.assertIn('for _ in range(3):', out)

if __name__ == '__main__':
    unittest.main()
