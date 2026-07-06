# Task3: Append New Sales

# Write 3 more order amounts to the sales_data.txt file
f=open("GenAI - Assignment4-RashmiBhilare/sales_data.txt",'a')
f.write("5000\n")
f.write("2500\n")
f.write("1700\n")
f.close()

# Read the updated sales_data.txt file
f=open("GenAI - Assignment4-RashmiBhilare/sales_data.txt",'r')
print(f.read())
f.close()

# Print the total number of lines after appending
with open("GenAI - Assignment4-RashmiBhilare/sales_data.txt",'r') as file:
    lines=file.readlines()
    print(f"Total Number of Lines in File ={len(lines)}")




