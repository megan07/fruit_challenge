import unittest
from price_fruit import price_fruit

class TestFruitPrices(unittest.TestCase):
    """ Tests the price_fruit function """

    def test_price_fruit(self):
        self.assertEqual(price_fruit(['apple']), float(0.60))
        self.assertEqual(price_fruit(['orange']), float(0.25))
        self.assertEqual(price_fruit(['Apple', 'apple', 'orange', 'apple', 'Orange']), float(2.30))
        self.assertEqual(price_fruit(['banana']), float(0.00))

if __name__ == '__main__':
    unittest.main()