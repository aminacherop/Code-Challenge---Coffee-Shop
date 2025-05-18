import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_init(self):
        """Test customer initialization and name validation"""
        
        c = Customer("Alice")
        assert c.name == "Alice"
        
    
        with pytest.raises(ValueError):
            Customer("")
            

        with pytest.raises(ValueError):
            Customer("ThisNameIsTooLongForACustomer")
            
    
        with pytest.raises(TypeError):
            Customer(123)
    
    def test_customer_orders(self):
        """Test getting orders for a customer"""
        customer = Customer("Bob")
        coffee = Coffee("Latte")
        
        
        assert len(customer.orders()) == 0
        

        order = Order(customer, coffee, 3.50)
        
    
        assert len(customer.orders()) == 1
        assert customer.orders()[0] == order
    
    def test_customer_coffees(self):
        """Test getting unique coffees for a customer"""
        customer = Customer("Charlie")
        latte = Coffee("Latte")
        espresso = Coffee("Espresso")
        
    
        Order(customer, latte, 3.50)
        Order(customer, espresso, 2.50)
        Order(customer, latte, 3.75)  
        
        
        coffees = customer.coffees()
        assert len(coffees) == 2
        assert latte in coffees
        assert espresso in coffees
    
    def test_create_order(self):
        """Test creating an order through the customer"""
        customer = Customer("Dave")
        coffee = Coffee("Mocha")
        
        
        order = customer.create_order(coffee, 4.00)
        
    
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 4.00
        assert order in customer.orders()
        assert order in coffee.orders()
    
    def test_most_aficionado(self):
        """Test the most_aficionado class method"""

        c1 = Customer("Emma")
        c2 = Customer("Frank")
        c3 = Customer("Grace")
        

        cappuccino = Coffee("Cappuccino")
        
        
        assert Customer.most_aficionado(cappuccino) is None
        
    
        Order(c1, cappuccino, 3.50)  
        Order(c2, cappuccino, 3.50)  
        Order(c2, cappuccino, 3.50)  
        Order(c3, cappuccino, 4.00) 
        
    
        assert Customer.most_aficionado(cappuccino) == c2