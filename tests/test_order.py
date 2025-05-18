import pytest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder:
    def test_order_init(self):
        """Test order initialization and validation"""
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        
        order = Order(customer, coffee, 3.50)
        assert order.customer == customer
        assert order.coffee == coffee
        assert order.price == 3.50
        
        
        with pytest.raises(TypeError):
            Order("Not a customer", coffee, 3.50)
            
        
        with pytest.raises(TypeError):
            Order(customer, "Not a coffee", 3.50)
            
    
        with pytest.raises(ValueError):
            Order(customer, coffee, 0.50)
            
    
        with pytest.raises(ValueError):
            Order(customer, coffee, 15.00)
    
    def test_order_relationships(self):
        """Test that order properly establishes relationships"""
        customer = Customer("Bob")
        coffee = Coffee("Espresso")
        
        
        order = Order(customer, coffee, 2.50)
        
    
        assert order in customer.orders()
        assert order in coffee.orders()