# Coffee Shop Domain Modeling

## Overview

This project is a domain modeling challenge that simulates the inner workings of a Coffee Shop using Python and object-oriented programming. The application models three primary entities: `Customer`, `Coffee`, and `Order`, demonstrating one-to-many and many-to-many relationships, data validation, and aggregate behavior through class methods.

## Objectives

* Build Python classes to represent the domain entities.
* Establish and manage relationships between objects.
* Validate and manage data using class methods and properties.
* Implement domain-specific behavior and aggregate methods.

## Project Structure

```
coffee_shop/
├── customer.py
├── coffee.py
├── order.py
├── debug.py
├── Pipfile
├── Pipfile.lock
└── tests/
    ├── test_customer.py
    ├── test_coffee.py
    └── test_order.py
```

## Setup Instructions

1. **Clone the repository** and navigate to the project folder:

   ```bash
   git clone <repo_url>
   cd coffee_shop
   ```
2. **Set up a virtual environment** using pipenv:

   ```bash
   pipenv install
   pipenv shell
   ```
3. **Install dependencies**:

   ```bash
   pipenv install pytest
   ```

## Class Descriptions

### Customer (customer.py)

* **Attributes**: `name` (1 to 15 characters)
* **Methods**:

  * `orders()` - Returns a list of all Order instances for this customer.
  * `coffees()` - Returns a unique list of Coffee instances ordered.
  * `create_order(coffee, price)` - Creates a new Order.
  * `most_aficionado(coffee)` *(Class Method)* - Returns the Customer who spent the most on the given coffee.

### Coffee (coffee.py)

* **Attributes**: `name` (minimum 3 characters)
* **Methods**:

  * `orders()` - Returns a list of all Order instances for this coffee.
  * `customers()` - Returns a unique list of Customer instances who ordered this coffee.
  * `num_orders()` - Returns number of times the coffee has been ordered.
  * `average_price()` - Returns average price of the coffee.

### Order (order.py)

* **Attributes**: `customer`, `coffee`, `price` (1.0 to 10.0)
* **Properties**:

  * `customer` - Returns the Customer instance.
  * `coffee` - Returns the Coffee instance.
  * `price` - Returns the price of the order.

## Data Validation

All attributes are validated to ensure data integrity:

* Customer names must be strings between 1 and 15 characters.
* Coffee names must be at least 3 characters.
* Price must be a float between 1.0 and 10.0.
* Custom exceptions are raised for invalid inputs.

## Testing

Tests are located in the `tests/` directory:

* To run tests:

  ```bash
  pytest
  ```
* Tests include:

  * Validation of properties
  * Relationship methods
  * Class method correctness

## Debugging

The `debug.py` file is provided for interactive testing and experimentation during development.

## Contributing
Fork the repository.

Create a feature branch (git checkout -b feature/your-feature).

Commit changes (git commit -m "Add feature").

Push to the branch (git push origin feature/your-feature).

Open a Pull Request.

## License
This project is licensed under the MIT License.

© 2024 Coffee Shop Domain Model

**Happy Hacking!** ☕
