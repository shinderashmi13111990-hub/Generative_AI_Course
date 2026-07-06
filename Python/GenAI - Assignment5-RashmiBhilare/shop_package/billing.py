# Module to manage functions related to billing
# Calculates the total sum of all prices in a list
def calculate_total(prices):
    return sum(prices)
# Applies a 5% tax to an amount and returns the total
def apply_tax(amount):
    amt_with_tax=amount+(amount*5/100)
    return amt_with_tax