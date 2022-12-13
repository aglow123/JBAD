import unittest
from agmath import quadratic


class QuadraticTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(quadratic(1, 2, 1), (-1, -1))
        self.assertEqual(quadratic(1, -2, 1), (1, 1))
        self.assertEqual(quadratic(-1, -2, -1), (-1, -1))
        self.assertEqual(quadratic(-1, 2, -1), (1, 1))
        self.assertEqual(quadratic(-1, -2, -1), (-1, -1))
        self.assertEqual(quadratic(1, 0, -1), (-1, 1))
        self.assertEqual(quadratic(-1, 0, 1), (-1, 1))
        self.assertEqual(quadratic(1, 2, 0), (-2, 0))
        self.assertEqual(quadratic(1, -2, 0), (0, 2))

    def test_wrong_input(self):
        with self.assertRaises(ValueError):  # bo a=0
            quadratic(0, 1, -1)
        with self.assertRaises(ValueError):  # bo delta ujemna
            quadratic(1, 1, 2)
        with self.assertRaises(TypeError):  # zły typ
            quadratic("1", 2, 1)


if __name__ == '__main__':
    unittest.main()
