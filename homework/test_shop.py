import pytest

from homework.models import Product


@pytest.fixture
def book():
    return Product('book', 100, 'This is a book', 1000)


@pytest.fixture
def pad():
    return Product('pad', 10, 'This is a pad', 100)


class TestProducts:

    def test_product_check_quantity(self, book, pad):
        assert book.check_quantity(115)
        assert not book.check_quantity(1001)
        with pytest.raises(ValueError):
            pad.check_quantity(-1)
            pad.check_quantity(0)

    def test_product_buy(self, book, pad):
        assert book.buy(100)
        assert pad.buy(90)

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

    def test_add_product_to_cart(self):
        pass

    def test_remove_product_from_cart(self):
        pass

    def test_remove_product_from_empty_cart(self):
        pass

    def test_clear_cart(self):
        pass

    def test_get_total_price_in_cart(self):
        pass

    def test_buy_cart(self):
        pass
