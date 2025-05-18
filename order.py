class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer  
        self.coffee = coffee      
        self.price = price        
        
        
        if hasattr(customer, '_orders'):
            customer._orders.append(self)
        if hasattr(coffee, '_orders'):
            coffee._orders.append(self)
    
    @property
    def customer(self):
        return self._customer  
    
    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("customer must be a Customer object")
        self._customer = value
    
    @property
    def coffee(self):
        return self._coffee  
    
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be a Coffee object")
        self._coffee = value
    
    @property
    def price(self):
        return self._price  
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if not (1.0 <= float(value) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = float(value)






      
        