import pytest
from src.coffee import Coffee
from src.customer import Customer
from src.order import Order

def test_valid_coffee():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"
    assert coffee in Coffee.all

def test_invalid_coffee_name_type():
    with pytest.raises(Exception, match="Coffee name must be a string."):
        Coffee(123)

def test_coffee_name_too_short():
    with pytest.raises(Exception, match="Coffee name must be at least 3 characters long."):
        Coffee("ab")

def test_orders_and_customers():
    cust1 = Customer("Gidion")
    cust2 = Customer("Mary")
    coffee = Coffee("Espresso")
    o1 = Order(cust1, coffee, 3.5)
    o2 = Order(cust2, coffee, 4.0)
    
    orders = coffee.orders()
    customers = coffee.customers()
    
    assert o1 in orders and o2 in orders
    assert cust1 in customers and cust2 in customers
    assert coffee.num_orders() == 2
    assert coffee.average_price() == (3.5 + 4.0)/2
    assert coffee.most_aficionado() in [cust1, cust2] 
