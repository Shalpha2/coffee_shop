from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")
latte = Coffee("Latte")

c1.create_order(latte, 4.5)
c1.create_order(latte, 5.0)
c2.create_order(latte, 6.0)

print(latte.num_orders())          # Output: 3
print(latte.average_price())       # Output: 5.17 (approx)
print(Customer.most_aficionado(latte).name)  # Output: Alice
