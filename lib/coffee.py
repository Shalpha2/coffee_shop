class Coffee:
    def __init__(self, name):
        self._orders = []  # Store orders here
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string with at least 3 characters.")

    @property
    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))


