from coffee import Coffee
from customer import Customer
from order import Order

# Create customers
dorcas = Customer("Dorcas")
shadrack = Customer("Shadrack")
nathan = Customer("Nathan")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
mocha = Coffee("Mocha")

# Create orders
dorcas.create_order(latte, 4.5)
dorcas.create_order(espresso, 3.0)
shadrack.create_order(latte, 5.0)
shadrack.create_order(mocha, 4.0)
nathan.create_order(latte, 4.5)
nathan.create_order(mocha, 4.5)

# Test methods
print("Dorcas's Coffees:", [coffee.name for coffee in dorcas.coffees()])
print("Latte's Customers:", [customer.name for customer in latte.customers()])
print("Latte Order Count:", latte.num_orders())
print("Average Price of Latte: $", round(latte.average_price(), 2))
print("Most Aficionado for Latte:", Customer.most_aficionado(latte).name)
