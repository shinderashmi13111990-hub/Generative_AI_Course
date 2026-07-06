# Module to manage functions related to discounts

def apply_discount(price,percent):
    discounted_price=price-(price*percent/100)
    return discounted_price

def flat_discount(price):
    return (price-50)