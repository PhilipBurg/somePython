import unittest
import calculations


class TestCalculations(unittest.TestCase):

    # test edge cases
    def test_add(self):
        self.assertEqual(calculations.add(10, 5), 15)
        self.assertEqual(calculations.add(-1, 1), 0)
        self.assertEqual(calculations.add(1, -1), 0)
        self.assertEqual(calculations.add(-5, -5), -10)

    def test_subtract(self):
        self.assertEqual(calculations.subtract(20, 10), 10)
        self.assertEqual(calculations.subtract(10, 10), 0)
        self.assertEqual(calculations.subtract(-5, 10), -15)
        self.assertEqual(calculations.subtract(-5, -10), 5)

    def test_multiply(self):
        self.assertEqual(calculations.multiply(2, 2), 4)
        self.assertEqual(calculations.multiply(-2, 2), -4)
        self.assertEqual(calculations.multiply(-2, -2), 4)
        self.assertEqual(calculations.multiply(2, 0), 0)

    def test_divide(self):
        self.assertEqual(calculations.divide(10, 2), 5)
        self.assertEqual(calculations.divide(-1, 1), -1)
        self.assertEqual(calculations.divide(-1, -1), 1)

        # self.assertRaises(ValueError, calculations.divide, 10, 0)
        # doing the same functionality like above but without passing last two args separately
        # using the context manager:
        with self.assertRaises(ValueError):
            calculations.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
