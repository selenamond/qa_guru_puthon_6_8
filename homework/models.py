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
                f'Количество {quantity} запрашиваемого товара {self.quantity} должно быть больше нуля')

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
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1) -> dict:
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """

        raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        raise NotImplementedError

    def clear(self):
        self.products = {}

    def get_total_price(self) -> float:
        raise NotImplementedError

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise NotImplementedError


if __name__ == '__main__':
    book = Product(name='book', price=100, description='This is a book', quantity=1000)
    pad = Product(name='pad', price=10, description='This is pad', quantity=100)
