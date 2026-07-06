# Task3: Product Pricing (Dictionaries)

price_dict={'TV':32000,'Shirt':1200,'Lotion':1100,'Cookware':620,'Building Blocks':1200,'Cricket Bat':5000}

# Block to add a new product with price to price_dict
def print_dict(title):
    print(f"\n{title}")
    print("{")
    for item_name,item_price in price_dict.items():
        print(f"\t{item_name} : {item_price}")
    print("}")
    print("\n*********************************")
    
def add_item(item):
    price_dict.update(item)
    
def update_item(key,new_value):
    price_dict[key]=new_value
    
def remove_item(key):
    is_key_present=False
    for items in price_dict.keys():
        if key==items:
            is_key_present=True
            price_dict.pop(key)
            break
    if is_key_present==False:
        print(f"{key} is not present in the dictionary")      
    

# Add a new product with price to price_dict
#price_dict.update({'fountain':5000})
add_item({'Fountain':5000})
print_dict("Dictionary After adding item")
        
# Update the price of existing product 'TV'
#price_dict['TV']=30000
update_item('TV',30000)
print_dict("Dictionary After Updating price of existing item of TV ")

# Remove a product by name
remove_item('Cookware')
print_dict("Dictionary after removal of the product : Cookware")

# Remove a non existing product
remove_item('Toys')
print_dict("Dictionary after removal of the product : Toys")
