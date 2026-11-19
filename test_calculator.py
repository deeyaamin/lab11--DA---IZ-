# https://github.com/deeyaamin/lab11--DA---IZ-
# Both roles completed by Deeya Amin

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(0, 4), 4)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-2, -3), 1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(-2, 10), -5)
        self.assertAlmostEqual(divide(3, 1), 1 / 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()