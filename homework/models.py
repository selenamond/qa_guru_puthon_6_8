from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if self.quantity >= quantity > 0:
            return True
        elif quantity <= 0:
            raise ValueError(
                f'Количество запрашиваемого товара {self.name} должно быть больше нуля')

    def buy(self, quantity) -> bool:
        if self.check_quantity(quantity):
            self.quantity -= quantity
            return True
        else:
            raise ValueError(
                f'Количество {self.quantity} товара {self.name} недоступно к покупке')

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count=1) -> dict:
        if product.check_quantity(buy_count):
            if product in self.products:
                self.products[product] += buy_count
            else:
                self.products[product] = buy_count
        return self.products

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

    def buy(self):
        if not self.products:
            raise ValueError('Корзина пустая')
        for product in self.products.keys():
            product.buy(self.products.get(product))
        self.clear()
