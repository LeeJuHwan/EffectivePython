"""
    ShoppingCart 클래스에 대한 통합 테스트
"""


import unittest
from cart import ShoppingCart
from product import Product


# 1. Unittest
class ShoppingCartTestCase(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.product = Product("shoes", "S", "black")

    def test_cart_init(self):
        self.assertDictEqual({}, self.cart.products)

    def test_add_product(self):
        self.cart.add_product(self.product)
        self.assertDictEqual({"SHOES-S-BLACK": {"quantity": 1}}, self.cart.products)

    def test_add_two_of_a_product(self):
        self.cart.add_product(self.product, quantity=2)
        self.assertDictEqual({"SHOES-S-BLACK": {"quantity": 2}}, self.cart.products)

    def test_add_two_different_products(self):
        product2 = Product("shirt", "M", "gray")

        self.cart.add_product(self.product)
        self.cart.add_product(product2)

        self.assertDictEqual(
            {
                "SHOES-S-BLACK": {"quantity": 1},
                "SHIRT-M-GRAY": {"quantity": 1},
            },
            self.cart.products
        )

    def test_remove_too_many_products(self):
        self.cart.add_product(self.product)
        self.cart.remove_product(self.product, quantity=2)

        self.assertDictEqual({}, self.cart.products)


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

    def test_generate_sku(self):
        self.assertEqual("SHOES-S-WHITE", self.product.generate_sku())

    def test_transform_name_for_sku(self):
        medium_pink_tank_top = Product("tanktop", "M", "pink")
        self.assertEqual("TANKTOP", medium_pink_tank_top.transform_name_for_sku)


# 2.Pytest
class TestProduct:
    def setup_class(self):
        self.product = Product("shoes", "S", "black")

    def test_transform_name_for_sku(self):
        """Is product name upper text?"""
        assert self.product.transform_name_for_sku == "SHOES"

    def test_transform_color_for_sku(self):
        """Is product color upper text?"""
        assert self.product.transform_color_for_sku == "BLACK"

    def test_generate_sku(self):
        """Is validate SKU?"""
        assert self.product.generate_sku() == "SHOES-S-BLACK"
