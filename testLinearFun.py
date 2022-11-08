import unittest
from agmath import linear


class LinearTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(linear(0, 0, 1, 1), (1, 0))
        self.assertEqual(linear(0, 0, 1, -1), (-1, 0))
        self.assertEqual(linear(0, 0, 1, 10), (10, 0))
        self.assertEqual(linear(5, 6, 7, 11), (2.5, -6.5))
        self.assertEqual(linear(0, 5, 7, 5), (0, 5))  # funkcja stala

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            linear(1, 1, 8, "7")
        with self.assertRaises(ValueError):
            linear(5, 5, 5, 5)


if __name__ == '__main__':
    unittest.main()
