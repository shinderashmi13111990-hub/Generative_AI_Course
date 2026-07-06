# Task3: User Menu (while loop+break/continue)

print("Please select the option from below menu : ")
print("1 - Add order amount to a running list")
print("2 - Show all order and totals after applying discounts")
print("q - Quit")

order_list=[]
total_order_amount=0
while True:
    user_input=input("Enter your choice : ")
    if user_input=="1":
        order_amount=input("Enter Order Amount : ")
        if order_amount.isdigit():
            order_amount=int(order_amount)
            order_list.append(order_amount)
            total_order_amount+=order_amount
        else:
            print("Please enter valid order amount")
    elif user_input=="2":
        if len(order_list)==0:
            print("No orders to show")
        else:
            print(f"Total Orders : {len(order_list)}")
            print(f"Total Order Amount : {total_order_amount}")
            print("--------------------------------------------------")
            for order in order_list:
                print(f"Order amount = {order}")
                discount_amt=0
                final_amt=0
                if order>=2000:
                    print("Discount is 15%")
                    discount_amt=order*15/100
                elif order>=1500 and order<2000:
                    print("Discount is 10%")
                    discount_amt=order*10/100
                elif order>=1000 and order<1500:
                    print("Discount is 7%")
                    discount_amt=order*7/100
                else:
                    print("Discount is 0%")
                    discount_amt=0

                final_amt=order-discount_amt
                print(f"Discount applied = {discount_amt}")
                print(f"Final Amount after discount = {final_amt}")
                print()
                
    elif user_input=="q":
        print("Quitting the program")
        break
    else:
        print("Please select valid option from menu")
        continue