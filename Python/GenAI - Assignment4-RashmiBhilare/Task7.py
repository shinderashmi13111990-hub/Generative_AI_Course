# Task 7: Mini Project-Export Discount Prices

# Dictionary of Product name as key and its price as value
prices={
    "Mouse":500,
    "Keyboard":800,
    "Monitor":7000,
    "Pendrive":400,
    "Camera":5000
}

# Take input for discount in percentage
discount_percent=int(input("Enter discount percentage : "))

# Write the Product details in the file 
with open("GenAI - Assignment4-RashmiBhilare/discount_report.txt","w") as file:
    total_discount_price=0
    for product_name,product_price in prices.items():
        dicounted_price=product_price-(product_price*discount_percent/100)    
        total_discount_price+=dicounted_price
        file.write(f"{product_name} | {product_price} | {dicounted_price}\n")
        
    # Write Total Items and Total Discount Price at the end of the file
    file.write(f"Total Items: {len(prices)}\n")
    file.write(f"Average Discounted Price: {total_discount_price/len(prices)}")

# Read the Product details from the file 
with open("GenAI - Assignment4-RashmiBhilare/discount_report.txt","r") as file:
    file_content=file.read()
    print(file_content)
    
        

    
    

