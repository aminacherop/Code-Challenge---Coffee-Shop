# Coffee Shop Domain Modeling

## Overview
This project implements an object‑oriented domain model for a Coffee Shop system. The model consists of three main entities with established relationships:

- **Customer** – can place many orders and has a many‑to‑many relationship with coffee through orders  
- **Coffee** – can have many orders and has a many‑to‑many relationship with customers through orders  
- **Order** – acts as a join entity, belongs to one customer and one coffee, and establishes the many‑to‑many relationship between customers and coffees  

## Domain Relationships
- A **Customer** can place many **Orders**  
- A **Coffee** can have many **Orders**  
- An **Order** belongs to one **Customer** and one **Coffee**  
- **Customer** and **Coffee** have a many‑to‑many relationship through the **Order** entity  

## Project Structure
```
coffee_shop/
├── customer.py     
├── coffee.py       
├── order.py        
├── debug.py        
├── tests/          
│   ├── test_customer.py
│   ├── test_coffee.py
│   └── test_order.py
├── Pipfile         
└── README.md       
```

## Installation and Setup
1. Clone the repository  
2. Set up the virtual environment:  
   ```bash
   pipenv install
   pipenv shell
   ```  
3. Install testing dependencies:  
   ```bash
   pipenv install pytest
   ```

## Core Functionality

### Customer Class
- Initialized with a name (string, 1–15 characters)  
- Can access all orders placed by the customer  
- Can retrieve a unique list of coffees ordered  
- Can create new orders  
- Class method to find the most devoted customer for a specific coffee  

### Coffee Class
- Initialized with a name (string, minimum 3 characters)  
- Can access all orders for this coffee  
- Can retrieve a unique list of customers who ordered this coffee  
- Can calculate order count and average price  

### Order Class
- Links a Customer and Coffee together  
- Stores the price of the transaction  
- Provides validation for all attributes  

## Testing
Run the included tests with:  
```bash
pytest
```

## License
MIT License  

© 2025
