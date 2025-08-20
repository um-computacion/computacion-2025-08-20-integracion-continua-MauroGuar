import unittest

from src.main import suma


class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(9, 8), 17)
        self.assertEqual(suma(4, 2), 6)
        self.assertEqual(suma(102, 405), 507)


if __name__ == '__main__':
    unittest.main()
