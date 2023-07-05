import pytest


class TestProducts:

    def test_product_check_quantity(self, book, pad):
        assert book.check_quantity(115)
        assert not book.check_quantity(1001)
        with pytest.raises(ValueError):
            pad.check_quantity(-1)
            pad.check_quantity(0)

    def test_product_buy(self, book, pad):
        book.buy(100)
        pad.buy(90)
        assert book.quantity == 900
        assert pad.quantity == 10

    def test_product_buy_more_than_available(self, pad, book):
        with pytest.raises(ValueError):
            book.buy(1001)
            pad.buy(101)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product_to_cart(self, cart, book):
        cart.add_product(book, 10)
        assert cart.products[book] == 10

    def test_remove_all_product_from_cart(self, cart, book):
        cart.add_product(book, 10)
        cart.remove_product(book, 10)
        assert cart.products == {}

    def test_remove_more_product_than_cart_have(self, cart, pad):
        cart.add_product(pad, 1)
        cart.remove_product(pad, 2)
        assert cart.products == {}

    def test_remove_one_product_from_several_in_cart(self, cart, book):
        cart.add_product(book, 10)
        cart.remove_product(book, 1)
        assert cart.products[book] == 9

    def test_clear_cart(self, cart, book, pad):
        cart.add_product(book, 1)
        cart.add_product(pad, 2)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price_in_cart(self, cart, book, pad):
        cart.add_product(book, 10)
        cart.add_product(pad, 22)
        assert cart.get_total_price() == 1220

    def test_buy_products_in_cart(self, cart, book):
        cart.add_product(book, 1)
        cart.buy()

        assert book.quantity == 999

    def test_buy_product_more_than_available(self, cart, book):
        cart.add_product(book, 2000)
        with pytest.raises(ValueError):
            cart.buy()

    def test_buy_empty_cart(self, cart):
        with pytest.raises(ValueError):
            cart.buy()

