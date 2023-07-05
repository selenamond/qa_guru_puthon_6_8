import pytest
from homework.models import Product, Cart


@pytest.fixture
def book():
    return Product('book', 100, 'This is a book', 1000)


@pytest.fixture
def pad():
    return Product('pad', 10, 'This is a pad', 100)


@pytest.fixture
def cart():
    return Cart()
