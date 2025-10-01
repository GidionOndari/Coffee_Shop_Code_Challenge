from typing import List

class Coffee:
    all = []

    def __init__(self, name: str):
        # validate and set name
        if not isinstance(name, str):
            raise Exception("Coffee name must be a string.")
        name = name.strip()
        if len(name) < 3:
            raise Exception("Coffee name must be at least 3 characters long.")
        self._name = name
        Coffee.all.append(self)

    def __repr__(self):
        return f"<Coffee name={self.name!r}>"

    @property
    def name(self) -> str:
        return self._name  

    # orders that contain this coffee
    def orders(self) -> list:
        from .order import Order
        return [order for order in Order.all if order.coffee is self]

    # unique customers who bought this coffee
    def customers(self) -> list:
        from .order import Order  
        from .customer import Customer
        seen = []
        for order in self.orders():
            c = order.customer
            if c not in seen:
                seen.append(c)
        return seen

    # number of orders for this coffee
    def num_orders(self) -> int:
        return len(self.orders())

    # average price for orders of this coffee
    def average_price(self) -> float:
        orders = self.orders()
        if not orders:
            return 0.0
        total = sum(o.price for o in orders)
        return total / len(orders)

    # who spent the most on this coffee across all orders
    def most_aficionado(self):
        orders = self.orders()
        if not orders:
            return None
        spends = {}
        for order in orders:
            cust = order.customer
            spends[cust] = spends.get(cust, 0.0) + order.price
        return max(spends.items(), key=lambda kv: kv[1])[0]
