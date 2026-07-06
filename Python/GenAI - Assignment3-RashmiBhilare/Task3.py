# Task3: Lamda Function GST Calculator

# Lambda Function to calculate GST
gst = lambda price:price + (0.18*price)

print(gst(100))

# Lambda Function to calculate discounted amount
discount_price = lambda order_amt,discount:order_amt-(order_amt*discount/100)

# Function to calculate final order amount 
def final_order_amt_calculator(order_amount):
    discount_amt=0
    final_bill_amount=0
   
    if order_amount.isdigit():
        order_amount=int(order_amount)
        if order_amount>=2000:
            print("Discount is 15%")
            discount_amt=discount_price(order_amount,15)
        elif order_amount>=1500 and order_amount<2000:
            print("Discount is 10%")
            discount_amt=discount_price(order_amount,10)
        elif order_amount>=1000 and order_amount<1500:
            print("Discount is 7%")
            discount_amt=discount_price(order_amount,7)
        else:
            print("Discount is 0%")
            discount_amt=discount_price(order_amount,0)
            
        print(f"Order Bill After Discount = {discount_amt}")
        final_bill_amount=gst(discount_amt)
        print(f"Final Bill Amount = {final_bill_amount}")
    else:
        print("Please enter valid order amount")
        exit
    
order_amount=(input("Enter Total Order Amount : "))
final_order_amt_calculator(order_amount)



