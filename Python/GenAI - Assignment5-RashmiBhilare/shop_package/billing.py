# Module to manage functions related to billing

def calculate_total(prices):
    return sum(prices)

def apply_tax(amount):
    amt_with_tax=amount+(amount*5/100)
    return amt_with_tax