# Task2: Read File in Different Ways

# Opening file in read mode


# 1. Read the sales_data.txt file using .read()

f=open("GenAI - Assignment4-RashmiBhilare/sales_data.txt",'r')
print("Reading File using read() :")
content=f.read()
print(f"{content}")
f.close()

# 2. Read the sales_data.txt file using .readline()

print("Reading Firstline in the File using readline() :")
with open("GenAI - Assignment4-RashmiBhilare/sales_data.txt",'r') as file:
    file_line=file.readline()
    print(file_line)    
    
# 3. Read the sales_data.txt file using .readlines()

print("Reading File using readliness() :")
with open("GenAI - Assignment4-RashmiBhilare/sales_data.txt",'r') as file:
    lines=file.readlines()
    print(lines)    
    new_lines=[]
    # Converting the file content into list of integers
    for line in lines:
        new_lines.append(int(line.replace("\n","")))
    print(new_lines)


