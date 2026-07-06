# Task6 - Combined Utility Function

def process_prices(prices):
    discounted_price=list(map(lambda x:x-x*10/100,prices))
    price_above_300=list(filter(lambda x:x>300,discounted_price))
    return discounted_price,price_above_300

discounted_price,price_above_300=process_prices([100,500,900,50,750])
print(f"Discounted price : {discounted_price}")
print(f"Discounted Prices above 300 : {price_above_300}")