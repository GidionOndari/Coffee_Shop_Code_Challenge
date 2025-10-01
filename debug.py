from src.customer import Customer
from src.book import Book
from src.order import Order

c1 = Customer("Gidion")
b1 = Book("Python 101")
o1 = Order(c1, b1, 9.0)

print(c1)
print(b1)
print(o1)
