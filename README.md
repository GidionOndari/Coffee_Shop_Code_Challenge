# Coffee Shop Code Challenge

## Description
A Python OOP project simulating a coffee shop system. Tracks customers, coffee types, purchases, and calculates spending and profits.

---

## Features
- Add/view customers
- Add/view coffee types
- Track customer purchases
- Determine the customer who spent the most on a specific coffee
- Display reports for coffee and customer spending

---

## Installation
```bash
git clone <your-repo-url>
cd coffee-shop-code-challenge
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

---

## Usage
Run the application:
```bash
python app.py
```
Follow the command-line prompts to manage customers, coffee types, and transactions.

---

## Project Structure
```
coffee-shop-code-challenge/
├── app.py
├── controllers/
├── models/
│   ├── coffee.py
│   └── customer.py
├── tests/
├── requirements.txt
└── README.md
```

---

## Example
```python
from models.customer import Customer
from models.coffee import Coffee

latte = Coffee("Latte", 4.5)
alice = Customer("Alice")
alice.buy_coffee(latte)

print(Customer.most_spent_on("Latte").name)  # Outputs top spender
```

---

## Author
Gidion Ondari
