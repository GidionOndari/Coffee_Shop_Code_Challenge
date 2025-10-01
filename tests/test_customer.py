import pytest
from src.customer import Customer

def test_valid_customer():
    c = Customer("Gidion")
    assert c.name == "Gidion"

def test_invalid_customer_type():
    with pytest.raises(Exception, match="Customer name must be a string."):
        Customer(123)

def test_customer_name_too_long():
    with pytest.raises(Exception, match="Customer name must be between 1 and 15 characters."):
        Customer("abcdefghijklmnop")

def test_customer_name_empty():
    with pytest.raises(Exception, match="Customer name must be between 1 and 15 characters."):
        Customer("   ")
