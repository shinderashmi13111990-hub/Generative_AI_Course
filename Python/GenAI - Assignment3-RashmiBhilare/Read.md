# Assignment 3 - Task Summary

## Task 1: Basic Function - Price after Discount
- Created a function apply_discount() to calculate and print the discount amount for an order.
- Behavior: prints the discount percentage and the discounted amount. If `discount_percent > 60`, it prints an error message.
- Inputs required: numeric `order_amount`, optional numeric `discount_percent`.

## Task 2: Recursive Function - Factorial
- Creted a recursive function factorial() to compute the factorial of a non-negative integer.
- Behavior: Needs non negative number to calculate factorial. If user enters negative number , it gives error
- Inputs required: Need to pass an integer 

## Task 3: Lambda Function GST Calculator
- Summary: 
1) Created lambda funtion to calculate GST
2) Created lambda function to calculate the discounted amount
3) Created a function which calls the lambda functions created to apply discounts and GST to a user-entered order amount.
- Behavior: validates input digits, applies a discount tier based on order amount, prints the bill after discount, then applies 18% GST and prints the final amount.
- Inputs required: user-entered `order_amount` as digits.

## Task 4: Using `map()` - Apply GST to List of Prices
- Used map() with a lambda to add 18% GST to each price in a hard-coded list.
- Behavior: prints the original prices list and the new list after GST.
- Inputs required: a list of integer which will be passed price list.

## Task 5: Using `filter()` - Filter Expensive Products
- Used filter() with lambdas to separate prices above 500 and prices less than or equal to 500.
- Behavior: prints two filtered lists.
- Inputs required: a list of integer which will be passed price list.

## Task 6: Combined Utility Function
- Defined a function process_prices() to apply a 10% discount to each price using map(), then filters discounted prices above 300 with filter().
- Behavior: returns both the discounted price list and the filtered list of prices greater than 300.
- Inputs required: a list of integer which will be passed price list.

## Task 7: Mini Problem - Menu using Functions
- Summary: Implements a simple menu-driven program with functions to add a price, compute average price, and compute maximum price from a list.
- Behavior: repeatedly prompts the user for a menu choice until `q` is entered, and updates or reports on the price list.If any invalid input is entered then the user will be asked to enter valid option
- Inputs required:
  - menu option: `1`, `2`, `3`, or `q`

