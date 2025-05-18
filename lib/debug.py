from coffee import Coffee
from customer import Customer
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")
charlie = Customer("Charlie")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
mocha = Coffee("Mocha")

# Create orders
alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)
bob.create_order(mocha, 4.0)
charlie.create_order(latte, 4.5)
charlie.create_order(mocha, 4.5)

# Test methods
print("Alice's Coffees:", [coffee.name for coffee in alice.coffees()])
print("Latte's Customers:", [customer.name for customer in latte.customers()])
print("Latte Order Count:", latte.num_orders())
print("Average Price of Latte: $", round(latte.average_price(), 2))
print("Most Aficionado for Latte:", Customer.most_aficionado(latte).name)
