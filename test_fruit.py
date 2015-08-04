import unittest
from price_fruit import price_fruit, onsale

class TestFruitPrices(unittest.TestCase):
    """ Tests the price_fruit function """

    def test_price_fruit(self):
        self.assertEqual(price_fruit(['apple']), float(0.60))
        self.assertEqual(price_fruit(['orange']), float(0.25))
        self.assertEqual(price_fruit(['Apple', 'apple', 'orange', 'apple', 'Orange']), float(1.70))
        self.assertEqual(price_fruit(['Apple', 'apple']), float(0.60))
        self.assertEqual(price_fruit(['orange', 'Orange', 'orange']), float(0.50))
        self.assertEqual(price_fruit(['banana']), float(0.00))

    def test_onsale(self):
        current_totals = {"apple": 1, "orange": 5}
        self.assertTrue(onsale("apple", current_totals))
        self.assertTrue(onsale("orange", current_totals))
        current_totals = {"apple": 2, "orange": 6}
        self.assertFalse(onsale("apple", current_totals))
        self.assertFalse(onsale("orange", current_totals))

if __name__ == '__main__':
    unittest.main()