# GenAI Assignment 5 - Modules and Packages

## Task 1: Math Utils Module

Summary:
Create a module `math_utils.py` for mathematical calculations. This module contains three functions:
- `add(a, b)` - Returns the sum of two numbers
- `subtract(a, b)` - Returns the difference of two numbers
- `square(n)` - Returns the square of a number

Inputs Required:
- Two integers `a` and `b` for `add()` and `subtract()` operations
- One integer `n` for the `square()` operation

How to Run:
```bash
python main.py
```
Or import and use the module directly:
```python
import math_utils
print(math_utils.add(10, 5))           # Output: 15
print(math_utils.subtract(10, 5))      # Output: 5
print(math_utils.square(4))            # Output: 16
```

## Task 2: String Utils Module

Summary:
Create a module `string_utils.py` for string operations. This module contains three functions:
- `capitalize_words(text)` - Converts the string to uppercase
- `reverse_string(text)` - Reverses the string
- `word_count(text)` - Returns the count of words in the string

Inputs Required:
- One string `text` for all functions (can include spaces and special characters)

How to Run:
```bash
python main.py
```
Or import and use the module directly:
```python
import string_utils
print(string_utils.capitalize_words("Rome was not built in a day"))
# Output: ROME WAS NOT BUILT IN A DAY

print(string_utils.reverse_string("Rome was not built in a day"))
# Output: yad a ni tliub ton saw emoR

print(string_utils.word_count("Rome was not built in a day"))
# Output: 8
```

## Task 3: Shop Package Creation

Summary:
Create a package `shop_package/` with multiple modules to handle e-commerce operations:
- `__init__.py` - Package initialization file that imports functions from submodules
- `discount.py` - Module containing `apply_discount(price, percent)` and `flat_discount(price)`
- `billing.py` - Module containing `calculate_total(prices)` and `apply_tax(amount)`

Inputs Required:
- `price` - Numeric value for the product price
- `percent` - Numeric percentage for percentage-based discount (0-100)
- `prices` - List of numeric prices for total calculation
- `amount` - Numeric value for tax calculation (5% tax applied)

How to Run:
```bash
python main.py
```
Or import and use the package directly:
```python
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

print(disc.apply_discount(1000, 10))      # Output: 900.0
print(disc.flat_discount(1000))           # Output: 950
print(calculate_total([100, 200, 300]))   # Output: 600
print(apply_tax(100))                     # Output: 105.0
```

## Task 4: Using Shop Package

Summary:
Demonstrate the usage of `shop_package` modules in `main.py` using different import methods:
- Import entire module: `import shop_package.discount as disc`
- Import specific functions: `from shop_package.billing import calculate_total`

The main script showcases both import techniques and calls functions from math_utils, string_utils, and shop_package modules.

Inputs Required:
No user input required. The script uses hard-coded values for testing:
- Math operations: integers (10, 5, 4, 23, 6)
- String operations: predefined strings
- Discount operations: prices (1000) and discount percentages (10)
- Billing operations: price lists ([100, 200, 300]) and amounts (100)

How to Run:
```bash
python main.py
```

This will execute all tasks sequentially and display:
- Math operations using both import methods
- String operations from string_utils
- Discount operations from shop_package.discount
- Billing operations from shop_package.billing
