# Task 1: Create and use Module for mathematical calculation : math_utils
import math_utils

print("Using the functions in module by importing the complete module")
sum=math_utils.add(10,5)
print(f"Addition of the numbers : {sum}")

diff=math_utils.subtract(10,5)
print(f"Subtraction of the numbers : {diff}")

square_of_n=math_utils.square(4)
print(f"Square of the number : {square_of_n}")

print()
print("***********************************************************")
print()

print("Using the functions in module by importing the specific function in a module")


from math_utils import add
print(f"Addition of the numbers : {add(23,5)}")

from math_utils import subtract
print(f"Subtraction of the numbers : {subtract(23,5)}")

from math_utils import square
print(f"Square of the number : {square(6)}")

print()
print("***********************************************************")
print()

# Task 1: Create and use Module for string operations: string_utils

import string_utils

print(f"String in capital letters : {string_utils.capitalize_words("Rome was not built in a day")}")
print(f"String in reverse : {string_utils.reverse_string("Rome was not built in a day")}")
print(f"Words in the String : {string_utils.word_count("Rome was not built in a day")}")

print()
print("***********************************************************")
print()

# Task3 : Create a Package shop_package, 
# subtask : create module for managing discount under shop_package
# subtask : create module for managing billing under shop_package

# Task 4 : Call the functions created in dicount and Billing Module from shop_package

import shop_package.discount as disc

print(f"Percentage based Dicounted price : {disc.apply_discount(1000,10)}")
print(f"Flat Discounted Price : {disc.flat_discount(1000)}")

print()
print("***********************************************************")
print()

from shop_package.billing import calculate_total
print(f"Total Price = {calculate_total([100,200,300])}")

from shop_package.billing import apply_tax
print(f"Tax applied price = {apply_tax(100)}")
