# Task4: Combined Operations

# Created list of tuples 'catalog'
catalog=[('TV',32000,'Electronics'),('Shirt',1200,'Apparel'),('Lotion',400,'Skin Care'),('Dress',620,'Apparel'),('Palazzo',900,'Apparel'),('Sunscreen',800,'Skin Care')]
print(catalog)

# Creating dictionary category_to_products that maps each category to a list of product names in the category
category_to_products={'Electronics':['TV'],'Apparel':['Shirt','Dress','Palazzo'],'Skin Care':['Lotion','Sunscreen']}
print(category_to_products)

# Print all the products that belong to the category that has the maximum number  of Products
for item_keys,item_values in category_to_products.items():    
    print(f"{item_keys}:{len(item_values)}")

# Find the category key that has the longest list of products
max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

# Get the products for that specific category
best_products = category_to_products[max_category]

# Print the result
print(best_products)