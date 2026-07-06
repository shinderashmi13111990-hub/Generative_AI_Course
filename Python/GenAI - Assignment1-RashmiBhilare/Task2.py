# Task2: Categories (Sets)

# Created a set of categories
categories_set={'Electronics','Apparel','Skin Care','Kitchen','Toys','Sports','Stationary','Beauty Products'}
print(categories_set) # This will print 8 unique categories

# Added new catergories
categories_set.add('Decoratives') # This will be added as it is unique
categories_set.add('Stationary') # This will be ignore as it already exists in the set
print(categories_set)  # This will print 9 categories even though we added 10

# Checking if 'Stationary' exists in set 
print(f"Stationary exists in the set : {categories_set.__contains__('Stationary')}") # Checks if 'Stationary' is present in set or not

# Checking if 'Fashion' exists in set 
print(f"Fashion exists in the set : {categories_set.__contains__('Fashion')}") # Checks if 'Stationary' is present in set or not

# len() will return total number of categories in set. Set will store only unique values
print('Total no of unique categories:',len(categories_set)) 