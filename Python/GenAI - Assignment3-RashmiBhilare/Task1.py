# Task1: Basic Function: Price after Discount

def apply_discount(order_amount,discount_percent=5):
    if discount_percent>60:
        print("Discount cannot exceed 60%")    
    else:
        discounted_amt=order_amount*discount_percent/100
        print("Discount Percentage Applied =",discount_percent)
        print("Order Amount after discount =",discounted_amt)

apply_discount(1000,10)
print()
apply_discount(500)
print()
apply_discount(400,70)
    
    