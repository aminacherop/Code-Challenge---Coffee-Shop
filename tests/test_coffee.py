import pytest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee:
    def test_coffee_init(self):
        """Test coffee initialization and name validation"""
        
        c = Coffee("Latte")
        assert c.name == "Latte"
        
        
        with pytest.raises(ValueError):
            Coffee("La")
            
        
        with pytest.raises(TypeError):
            Coffee(123)
    
    def test_coffee_orders(self):
        """Test getting orders for a coffee"""
        coffee = Coffee("Americano")
        customer = Customer("Alice")
        
        
        assert len(coffee.orders()) == 0
        
        
        order = Order(customer, coffee, 2.75)
        

        assert len(coffee.orders()) == 1
        assert coffee.orders()[0] == order
    
    def test_coffee_customers(self):
        """Test getting unique customers for a coffee"""
        coffee = Coffee("Espresso")
        c1 = Customer("Bob")
        c2 = Customer("Charlie")
        
    
        Order(c1, coffee, 2.25)
        Order(c2, coffee, 2.30)
        Order(c1, coffee, 2.20) 
        
        
        customers = coffee.customers()
        assert len(customers) == 2
        assert c1 in customers
        assert c2 in customers
    
    def test_num_orders(self):
        """Test counting the number of orders for a coffee"""
        coffee = Coffee("Cappuccino")
        c1 = Customer("Dave")
        c2 = Customer("Emma")
        
        
        assert coffee.num_orders() == 0
        
    
        Order(c1, coffee, 3.25)
        assert coffee.num_orders() == 1
        
        Order(c2, coffee, 3.50)
        assert coffee.num_orders() == 2
        
        Order(c1, coffee, 3.25)
        assert coffee.num_orders() == 3
    
    def test_average_price(self):
        """Test calculating average price for a coffee"""
        coffee = Coffee("Mocha")
        customer = Customer("Frank")
        
        
        assert coffee.average_price() == 0
        
        
        Order(customer, coffee, 4.00)
        assert coffee.average_price() == 4.00
        
        Order(customer, coffee, 4.50)
        assert coffee.average_price() == 4.25
        
        Order(customer, coffee, 3.50)
        assert coffee.average_price() == 4.00