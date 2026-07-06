# Module to manage functions related to discounts
# Applies a percentage-based discount to a price
def apply_discount(price,percent):
    discounted_price=price-(price*percent/100)
    return discounted_price
# Applies a fixed flat discount to a price
def flat_discount(price):
    return (price-50)