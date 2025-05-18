from customer import Customer
from coffee import Coffee
from order import Order

def create_test_data():
    """Create some test data to work with"""
    print("Creating test data...")
    
    
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    print(f"Created customers: {alice.name}, {bob.name}, {charlie.name}")
    
    
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")
    cappuccino = Coffee("Cappuccino")
    mocha = Coffee("Mocha")
    print(f"Created coffees: {espresso.name}, {latte.name}, {cappuccino.name}, {mocha.name}")
    
    
    order1 = Order(alice, espresso, 2.50)
    order2 = Order(alice, latte, 3.50)
    order3 = Order(bob, cappuccino, 4.00)
    order4 = Order(bob, espresso, 2.75)
    order5 = Order(charlie, mocha, 4.50)
    order6 = Order(alice, espresso, 2.50)  
    
    print(f"Created {len(Order._all_orders) if hasattr(Order, '_all_orders') else 6} orders")
    
    return {
        "customers": {
            "alice": alice,
            "bob": bob,
            "charlie": charlie
        },
        "coffees": {
            "espresso": espresso,
            "latte": latte,
            "cappuccino": cappuccino,
            "mocha": mocha
        },
        "orders": [order1, order2, order3, order4, order5, order6]
    }

def test_customer_relationships(data):
    """Test customer relationship methods"""
    alice = data["customers"]["alice"]
    
    print("\n===== CUSTOMER RELATIONSHIPS =====")
    print(f"Alice has placed {len(alice.orders())} orders:")
    for i, order in enumerate(alice.orders(), 1):
        print(f"  {i}. {order.coffee.name} - ${order.price:.2f}")
    
    print(f"\nAlice has ordered {len(alice.coffees())} unique coffees:")
    for i, coffee in enumerate(alice.coffees(), 1):
        print(f"  {i}. {coffee.name}")

def test_coffee_relationships(data):
    """Test coffee relationship methods"""
    espresso = data["coffees"]["espresso"]
    
    print("\n===== COFFEE RELATIONSHIPS =====")
    print(f"Espresso has been ordered {espresso.num_orders()} times")
    print(f"Average price for Espresso: ${espresso.average_price():.2f}")
    
    print(f"\nEspresso has been ordered by {len(espresso.customers())} customers:")
    for i, customer in enumerate(espresso.customers(), 1):
        print(f"  {i}. {customer.name}")

def test_order_creation(data):
    """Test creating new orders"""
    charlie = data["customers"]["charlie"]
    latte = data["coffees"]["latte"]
    
    print("\n===== ORDER CREATION =====")
    print(f"Creating new order for {charlie.name}...")
    
    
    new_order = charlie.create_order(latte, 3.25)
    
    print(f"New order created: {charlie.name} ordered {latte.name} for ${new_order.price:.2f}")
    print(f"Charlie now has {len(charlie.orders())} orders")
    print(f"Latte now has {latte.num_orders()} orders")

def test_most_aficionado(data):
    """Test the most_aficionado class method"""
    espresso = data["coffees"]["espresso"]
    
    print("\n===== MOST AFICIONADO =====")
    top_customer = Customer.most_aficionado(espresso)
    
    if top_customer:
        print(f"The customer who spent the most on Espresso is: {top_customer.name}")
        
        total = sum(order.price for order in top_customer.orders() if order.coffee == espresso)
        print(f"They spent a total of ${total:.2f} on Espresso")
    else:
        print("No customers have ordered Espresso")

def main():
    """Main function to run tests"""
    print("Coffee Shop Domain Model Debug")
    print("=============================")
    
    
    data = create_test_data()
    
    
    test_customer_relationships(data)
    test_coffee_relationships(data)
    test_order_creation(data)
    test_most_aficionado(data)
    
    print("\n===== INTERACTIVE SESSION =====")
    print("Test data is available in the following variables:")
    print("- data['customers']: Dict of Customer objects")
    print("- data['coffees']: Dict of Coffee objects")
    print("- data['orders']: List of Order objects")
    print("\nYou can now interact with these objects.")

    alice = data["customers"]["alice"]
    bob = data["customers"]["bob"]
    charlie = data["customers"]["charlie"]
    espresso = data["coffees"]["espresso"]
    latte = data["coffees"]["latte"]
    cappuccino = data["coffees"]["cappuccino"]
    mocha = data["coffees"]["mocha"]
    
    

if __name__ == "__main__":
    main()