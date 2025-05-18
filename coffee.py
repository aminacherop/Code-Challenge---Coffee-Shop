class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value) < 3:
         raise ValueError("Coffee name must be at least 3 characters long")
        self._name = value

    def orders(self):
        return self._orders

    def customers(self):
        unique_customers = set(order.customer for order in self._orders)
        return list(unique_customers)

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0

        total_price = sum(order.price for order in self._orders)
        return total_price/len(self._orders)




espresso = Coffee("Espresso")
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino",)
print(f"Created coffees: {espresso.name}, {latte.name}, {cappuccino.name}")



print("\nAverage prices:")
print(f"Espresso: ${espresso.average_price():.2f}")  
print(f"Latte: ${latte.average_price():.2f}")  
print(f"Cappuccino: ${cappuccino.average_price():.2f}")  


mocha = Coffee("Mocha")
print(f"\nMocha (no orders):")
print(f"Number of orders: {mocha.num_orders()}")
print(f"Average price: ${mocha.average_price():.2f}")
print(f"Customers: {mocha.customers()}")