# Task5 - Using filter(): Filter Expensive Products

prices=[100,250,400,1200,50,2000,850]

prices_gt_than_500=list(filter(lambda x:x>500,prices))
print(f"Prices Greater than 500 : {prices_gt_than_500}")

prices_below_500=list(filter(lambda x:x<=500,prices))
print(f"Prices Less than or equal to 500 : {prices_below_500}")


