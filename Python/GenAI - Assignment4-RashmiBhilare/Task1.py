# Task1 : Write Sales Records to a File

sales = [1200,450,980,1500,3000]

# Write Sales in a File , each sale should be on new line in a file
f=open('GenAI - Assignment4-RashmiBhilare/sales_data.txt', 'w')
for order in sales:
    f.write(f"{order}\n")
f.close

# Read the sales from the file and print them
f=open('GenAI - Assignment4-RashmiBhilare/sales_data.txt', 'r')
content=f.read()
print("Printing Sales Data from File")
print(content)
f.close()

# Write Sales in a File , each sale should be on same line and comma separated in a file
f=open('GenAI - Assignment4-RashmiBhilare/sales_data.csv', 'w')
for order in sales:
    f.write(f"{order},")
f.close