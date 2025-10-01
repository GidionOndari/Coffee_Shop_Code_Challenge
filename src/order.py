from .coffee import Coffee

class Order:
    all = []

    def __init__(self, customer, coffee, price):
        from .customer import Customer  # local import to avoid circular import

        if not isinstance(customer, Customer):
            raise Exception("Order must be created with a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise Exception("Order must be created with a Coffee instance.")

        try:
            price_val = float(price)
        except Exception:
            raise Exception("Order price must be a number (float).")

        if price_val < 1.0 or price_val > 10.0:
            raise Exception("Order price must be between 1.0 and 10.0.")

        self._price = price_val
        self._customer = customer
        self._coffee = coffee
        Order.all.append(self)

    def __repr__(self):
        return f"<Order {self.customer.name!r} - {self.coffee.name!r} @ {self.price:.2f}>"

    @property
    def price(self):
        return self._price  

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
