# Task7 - Mini Problem : Menu using Functions

def add_price(prices_list,price):
    prices_list.append(price)

def get_average_price(prices_list):
    total=0
    avg=0
    for price in prices_list:
        total+=price
    avg=total/len(prices_list)
    return avg

def get_max_price(prices_list):
    return max(prices_list)    
        
print("Menu Options")
print("1 - Add price")
print("2 - Show Average price")
print("3 - Show Maximum price")
print("q - Quit")

prices_list=[]
while True:
    option= input("Enter your choice :")
    if option=="1":
        price=int(input("Enter price :"))
        add_price(prices_list,price)
    elif option=="2":
        print(f"Average price of the cart : {get_average_price(prices_list)}")
    elif option=="3":
        print(f"Maximum price in the cart: {get_max_price(prices_list)}")
    elif option=="q":
        exit
    else:
        print("Enter valid option from the menu")
        continue
    
    
    
