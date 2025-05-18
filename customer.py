class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    def __str__(self):
     return f"{self.name}"


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        unique_coffees = set(order.coffee for order in self._orders)
        return list(unique_coffees)

    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order

    def total_spent_on_coffee(self, coffee):
        return sum(order.price for order in self._orders if order.coffee == coffee)

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a coffee instance")
        customers = coffee.customers()
        if not customers:
            return None
        max_spent = 0
        top_customer = None

        for customer in customers:
            # helper instance method to calculate how much a specific customer spent
            spent = customer.total_spent_on_coffee(coffee)
            if spent > max_spent:
                max_spent = spent
                top_customer = customer
        return top_customer
    

alice = Customer("Alice")
bob = Customer ("Bob")
charlie = Customer("Charlie")
print(f"   Created: {alice}, {bob}, {charlie}")

