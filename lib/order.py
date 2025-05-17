class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value  # Removed type checking

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        self._coffee = value  # Removed type checking

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")


if __name__ == "__main__":
    from customer import Customer
    from coffee import Coffee
    alice = Customer("Alice")
    latte = Coffee("Latte")
    order = Order(alice, latte, 4.5)
    print(f"Order: {order.customer.name} ordered {order.coffee.name} for ${order.price}")

