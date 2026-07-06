# Task1 : Discount Rules (if/elif/else)

discount_amt=0
order_amount_after_discount=0
tax_amount=0
final_bill_amount=0
order_amount=(input("Enter Total Order Amount : "))
if order_amount.isdigit():
    order_amount=int(order_amount)
    if order_amount>=2000:
        print("Discount is 15%")
        discount_amt=order_amount*15/100
    elif order_amount>=1500 and order_amount<2000:
        print("Discount is 10%")
        discount_amt=order_amount*10/100
    elif order_amount>=1000 and order_amount<1500:
        print("Discount is 7%")
        discount_amt=order_amount*7/100
    else:
        print("Discount is 0%")
        discount_amt=0
        
    order_amount_after_discount=order_amount-discount_amt
    print(f"Discount applied = {discount_amt}")
    print(f"Order Amount after discount = {order_amount_after_discount}")
    tax_amount=order_amount_after_discount*5/100
    print(f"Tax applied = {tax_amount}")
    final_bill_amount=order_amount_after_discount+tax_amount
    print(f"Final Bill Amount = {final_bill_amount}")
else:
    print("Please enter valid order amount")