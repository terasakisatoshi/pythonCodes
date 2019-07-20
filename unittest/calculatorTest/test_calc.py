import unittest
from calc import Calculator


class CalculatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup calculator")
        cls.calc = Calculator()
        print("done calculator")

    def test_add(self):
        self.assertEqual(self.calc.add(2, 5), 7)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 5), -3)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 5), 10)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 3), 2)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
