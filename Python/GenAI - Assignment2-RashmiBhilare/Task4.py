# Task4 Loop Controls with Conditions (break & continue)

daily=[200,150,0,400,50,-1,300]
total_sales=0
for order in daily:
    if order==-1:
        print("Corrupted data")
        break
    elif order==0:
        print("No sales for the day")
        continue
    elif order>0:
        total_sales+=order
        print(f"Running Total Sales = {total_sales}")
        
print(f"Final Sales = {total_sales}") 
