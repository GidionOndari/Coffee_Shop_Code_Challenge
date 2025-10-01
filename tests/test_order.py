import pytest
from src.customer import Customer
from src.coffee import Coffee
from src.order import Order


def test_valid_order_creation():
    c = Customer("Gidion")
    coffee = Coffee("Latte")
    o = Order(c, coffee, 5.0)
    assert isinstance(o, Order)
    assert o.price == 5.0
    assert o.customer == c
    assert o.coffee == coffee


def test_order_invalid_customer():
    coffee = Coffee("Espresso")
    with pytest.raises(Exception, match="Customer instance"):
        Order("not_a_customer", coffee, 5.0)


def test_order_invalid_coffee():
    c = Customer("Gidion")
    with pytest.raises(Exception, match="Coffee instance"):
        Order(c, "not_a_coffee", 5.0)


def test_order_invalid_price_type():
    c = Customer("Gidion")
    coffee = Coffee("Cappuccino")
    with pytest.raises(Exception, match="number"):
        Order(c, coffee, "five")


def test_order_price_out_of_range():
    c = Customer("Gidion")
    coffee = Coffee("Mocha")
    with pytest.raises(Exception, match="between 1.0 and 10.0"):
        Order(c, coffee, 20.0)
