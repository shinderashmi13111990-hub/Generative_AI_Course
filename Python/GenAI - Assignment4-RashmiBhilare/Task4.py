# Task4: Generate Summary Report from File

with open("GenAI - Assignment4-RashmiBhilare/sales_data.txt",'r') as file:
    lines=file.readlines()
    print(lines)    
    new_lines=[]
    # Converting the file content into list of integers
    for line in lines:
        new_lines.append(int(line.replace("\n","")))
    print(new_lines)
    
    # Calculate Total Sales and Print
    total_sales=0
    for line in new_lines:
        total_sales+=line
    print(f"Total Sales = {total_sales}")
    
    # Calculate Highest Sales and Print
    print(f"Highest Sales = {max(new_lines)}")
    
    # Calculate Lowest Sales and Print
    print(f"Lowest Sales = {min(new_lines)}")
    
    # Calculate Average Sales and Print
    avg_sales=total_sales/len(new_lines)
    print(f"Average Sales = {avg_sales}")
    
    
