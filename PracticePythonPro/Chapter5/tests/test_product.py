"""
    1. 입력
    2. 결과 식별
    3. 결과 도출
    4. 식별 값 & 도출 값 비교
"""
import unittest
from product import Product


class ProductTestCase(unittest.TestCase):
    def setUp(self):
        self.product = Product("shoes", "S", "white")

    def test_validation_name(self):
        """transform_name_for_sku is upper text."""
        function_result = self.product.transform_name_for_sku
        self.assertEqual(function_result, "SHOES")

    def test_validation_color(self):
        """transform_color_for_sku is upper text."""
        function_result = self.product.transform_color_for_sku
        self.assertEqual(function_result, "WHITE")


if __name__ == "__main__":
    unittest.main()
