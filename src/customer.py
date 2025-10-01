from .order import Order
from .coffee import Coffee

class Customer:
    all = []

    def __init__(self, name):
        self._name = None
        self.name = name  
        Customer.all.append(self)

    def __repr__(self):
        return f"<Customer name={self.name!r}>"
# name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Customer name must be a string.")
        value = value.strip()
        if len(value) < 1 or len(value) > 15:
            raise Exception("Customer name must be between 1 and 15 characters.")
        self._name = value
# orders for this customer
    def orders(self):
        return [order for order in Order.all if order.customer is self]
# unique coffees bought by this customer
    def coffees(self):
        seen = []
        for order in self.orders():
            if order.coffee not in seen:
                seen.append(order.coffee)
        return seen
# create an Order connecting this customer to a coffee at price
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise Exception("create_order requires a Coffee instance.")
        return Order(self, coffee, price)
