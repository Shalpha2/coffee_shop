class Customer:
    def __init__(self, name):
        self._orders = []  # Store orders here
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee._orders.append(new_order)
        return new_order

    @property
    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    @classmethod
    def most_aficionado(cls, coffee):
        # Dictionary to store total spend per customer
        spend_map = {}
        for order in coffee.orders:
            customer = order.customer
            spend_map[customer] = spend_map.get(customer, 0) + order.price

        if not spend_map:
            return None

        return max(spend_map, key=spend_map.get)


