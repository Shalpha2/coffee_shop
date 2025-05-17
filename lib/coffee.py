
class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")

    def add_order(self, order):
        self._orders.append(order)

    @property
    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        return sum(order.price for order in self._orders) / len(self._orders)


if __name__ == "__main__":
    from customer import Customer
    espresso = Coffee("Espresso")
    bob = Customer("Bob")
    bob.create_order(espresso, 3.0)
    print(f"{espresso.name} orders count: {espresso.num_orders()}")
    print(f"Average price: ${espresso.average_price():.2f}")

