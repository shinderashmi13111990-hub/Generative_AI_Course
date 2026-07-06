# Task2: Process Multiple Orders (for loop)

Total_revenue=0
order_count_with_zero_discount=0
order_amount=[1200,2000,800,1750,3000]
print("|----------------|-----------|---------------------|--------------|")
print("|Order Amount    | Discount  | Discounted Amount   | Final Amount |")
print("|----------------|-----------|---------------------|--------------|")
for order in order_amount:
    #print(f"Order amount = {order}")
    
    discount_amt=0
    discount=""
    final_amt=0
    if order>=2000:
        #print("Discount is 15%")
        discount="15%"
        discount_amt=order*15/100
    elif order>=1500 and order<2000:
        discount="10%"
        #print("Discount is 10%")
        discount_amt=order*10/100
    elif order>=1000 and order<1500:
        discount="7%"
        #print("Discount is 7%")
        discount_amt=order*7/100
    else:
        discount="0%"
        #print("Discount is 0%")
        discount_amt=0
        order_count_with_zero_discount+=1

    final_amt=order-discount_amt
    Total_revenue+=final_amt
    #print(f"Discount applied = {discount_amt}")
    #print(f"Final Amount after discount = {final_amt}")
    #print()
    print(f"| {order}           | {discount}       | {discount_amt}               | {final_amt}       |")
    print(f"|----------------|-----------|---------------------|--------------|")


print(f"| Total Revenue  |           |                     | {Total_revenue}       |")
print(f"|----------------|-----------|---------------------|--------------|")
#print(f"Total Revenue = {Total_revenue}")
print()
print(f"Total Orders with 0% discount = {order_count_with_zero_discount}")
print()

