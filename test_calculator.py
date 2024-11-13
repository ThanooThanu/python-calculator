import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(33, 66), 99)

    def testsubtract1(self):
        self.assertEqual(self.calc.subtract(6, -10), 16)
    def testsubtract2(self):
        self.assertEqual(self.calc.subtract(5, 6), -1)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(7, 9), 63)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(60, 5), 12)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(51, 17), 0)

if __name__ == '__main__':
    unittest.main()