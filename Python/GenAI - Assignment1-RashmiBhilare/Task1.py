# Task1: Product Collections (Lists & Tuples)

# Create list name "products"
products=['TV','Shirt','Lotion','Cookware','Building Blocks','Cricket Bat']

# Created tuple name "sample_pro" 
sample_product=('Pen',10,'Stationary')

# Printing second product which is at index 1
print("Second product is ",products[1])

# Printing last product which is at index 5
print("Last product is ",products[5])

# Appended 2 products to list and printed the list
products.append('Mixer Grinder')
products.append('Lipstick')
print(products)

# Convert sample_product into list, changed the price to 20 and converted back into tuple
sample_product_list=list(sample_product)
print(sample_product_list)
sample_product_list[1]=20
print(sample_product_list)
sample_product=tuple(sample_product_list)
print(sample_product)