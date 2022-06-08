import unittest

from romanos import RomanNumber


class RomanNumberTest(unittest.TestCase):

    def test_crear_numero_romano(self):
        uno_numero = RomanNumber(1)
        self.assertEqual(uno_numero.valor, 1)
        self.assertEqual(uno_numero.cadena, "I")

        uno_cadena = RomanNumber("I")
        self.assertEqual(uno_cadena.valor, 1)
        self.assertEqual(uno_cadena.cadena, "I")

        self.assertRaises(ValueError, RomanNumber, 4000)
        self.assertRaises(ValueError, RomanNumber, 0)
        self.assertRaises(ValueError, RomanNumber, 1.1)
        self.assertRaises(ValueError, RomanNumber, "XVVI")
        self.assertRaises(ValueError, RomanNumber, "hola")
        self.assertRaises(ValueError, RomanNumber, ValueError)
        self.assertRaises(ValueError, RomanNumber, [])

    def test_representacion_de_cadena(self):
        tres = RomanNumber(3)
        self.assertEqual(str(tres), "III")

    def test_comparaciones(self):
        uno = RomanNumber(1)
        otro_uno = RomanNumber(1)
        dos = RomanNumber(2)

        self.assertEqual(uno, 1)
        self.assertEqual(uno, "I")
        self.assertEqual(uno, otro_uno)
        self.assertNotEqual(uno, dos)
        self.assertGreater(dos, 1)

    def test_suma(self):
        uno = RomanNumber(1)
        dos = RomanNumber(2)

        self.assertEqual(uno + dos, 3)
        self.assertEqual(uno + 3, 4)
        self.assertEqual(dos + "VI", 8)

        self.assertEqual(3 + uno, 4)
        self.assertEqual("VI" + dos, 8)


if __name__ == '__main__':
    unittest.main()