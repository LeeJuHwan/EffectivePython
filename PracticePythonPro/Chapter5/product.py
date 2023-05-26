"""
    전자상거래 시스템에서 구매할 상품을 나타낸다.
"""


class Product:
    """재고관리단위(SKU) 생성"""
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    @property
    def transform_name_for_sku(self):
        return self.name.upper()

    @property
    def transform_color_for_sku(self):
        return self.color.upper()

    def generate_sku(self):
        """
        SKU는 상품 속성을 고유하게 식별한다.
        """

        name = self.transform_name_for_sku
        color = self.transform_color_for_sku
        return f"{name}-{self.size}-{color}"
