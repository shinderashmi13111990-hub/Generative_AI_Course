# Task5: Create Product Info File

    
# Ask the user for 3 products & their prices
product_name=[]
product_price=[]
for n in range(3):
    product_name.append(input("Enter Product Name : "))
    product_price.append(int(input("Enter Product Price : ")))

print(product_name)
print(product_price)

# Write the User Inputs into the products.txt File

with open("GenAI - Assignment4-RashmiBhilare/products.txt","w") as file:
    for n in range(3):
        file.write(f"{product_name[n]} | {product_price[n]}\n")
        
# Read the File products.txt and print it in proper format

print(f"|---------------|----------|")
print(f"| Product Name  | Price    |")
print(f"|---------------|----------|")
with open("GenAI - Assignment4-RashmiBhilare/products.txt","r") as file:
    file_lines=file.readlines()
    for line in file_lines:
        product_name,product_price=line.split("|")
        product_name=product_name.replace(" ","")
        product_price=product_price.replace(" ","")
        product_price=product_price.replace("\n","")
        #print(f":{product_name}:")
        #print(f":{product_price}:")
        print(f"| {product_name}           | {product_price}   |")
        print(f"|---------------|----------|")
        
        

        
    