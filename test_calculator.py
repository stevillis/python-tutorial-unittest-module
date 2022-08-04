"""Tests for calculator module"""

import unittest

import calculator


class TestCalculator(unittest.TestCase):
    """Test calculator functions"""

    def test_add(self):
        """Test add function"""
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(2, -3), -1)
        self.assertEqual(calculator.add(-2, -3), -5)

    def test_subtract(self):
        """Test subtract function"""
        self.assertEqual(calculator.subtract(4, 2), 2)
        self.assertEqual(calculator.subtract(4, -2), 6)
        self.assertEqual(calculator.subtract(-4, -2), -2)

    def test_mutiply(self):
        """Test mutiply function"""
        self.assertEqual(calculator.multiply(4, 2), 8)
        self.assertEqual(calculator.multiply(4, -2), -8)
        self.assertEqual(calculator.multiply(-4, -2), 8)

    def test_divide(self):
        """Test divide function"""
        self.assertEqual(calculator.divide(4, 2), 2)
        self.assertEqual(calculator.divide(4, -2), -2)
        self.assertEqual(calculator.divide(-4, -2), 2)
        self.assertEqual(calculator.divide(1, 2), 0.5)
        # self.assertRaises(ValueError, calculator.divide, 4, 0)
        with self.assertRaises(ValueError):
            calculator.divide(4, 0)


if __name__ == '__main__':
    unittest.main()
