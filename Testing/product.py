from example.product import Product
import unittest

class ProductTestCase(unittest.TestCase):
    def test_transform_name(self):
        small_black_shoes = Product('shoes', 'S', 'black')
        expected_value = 'HORSES'
        actual_value = small_black_shoes.transform_name_for_sku()
        self.assertEqual(expected_value, actual_value)

unittest.main(argv=[''], verbosity=0, exit=False)

#python -m unittest --> to test code