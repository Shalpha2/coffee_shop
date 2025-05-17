# main.py
#from customer import Customer
#from coffee import Coffee

# Create some customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create some coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Customers place orders
alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)
bob.create_order(latte, 4.0)

# Print orders for each customer
print("Customer Orders:")
for customer in [alice, bob]:
    print(f"{customer.name} has ordered:")
    for order in customer.orders:
        print(f"  - {order.coffee.name}: ${order.price}")
    print()

# Print customers who ordered a coffee
print("Coffee -> Customers:")
for coffee in [latte, espresso]:
    print(f"{coffee.name} has been ordered by:")
    for customer in coffee.customers():
        print(f"  - {customer.name}")
    print()

# Show number of orders and average price for each coffee
print("Coffee Statistics:")
for coffee in [latte, espresso]:
    print(f"{coffee.name} - Orders: {coffee.num_orders()}, Average Price: ${coffee.average_price():.2f}")

# Who is the biggest spender for Latte?
aficionado = Customer.most_aficionado(latte)
if aficionado:
    print(f"\nMost Aficionado for {latte.name}: {aficionado.name}")
else:
    print(f"\nNo orders for {latte.name}.")

