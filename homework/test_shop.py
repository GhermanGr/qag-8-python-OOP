"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 5, 5)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity_at_limit(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity) == True

    def test_product_check_quantity_over_limit(self, product):
        assert product.check_quantity(product.quantity + 1) == False

    def test_product_buy_quntity_decrease(self, product):
        # TODO напишите проверки на метод buy
        initial_quantity = product.quantity
        product.buy(product.purchase_quantity)
        assert product.quantity == initial_quantity - product.purchase_quantity

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(product.quantity + 1)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
