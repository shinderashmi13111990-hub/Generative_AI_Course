# Task6 : Read File Safely(Error Handling Inside File Handling only )

import os

# Take file name as input from user
# print the contents if the file exists
# Print error message if the file does not exists
filename=input("Enter file to open : ")
if os.path.exists(filename):
    f=open(filename,"r")
    content=f.read()
    print(content)
    f.close()
else:
    print("File not found. Please check the filename")
    exit

    

    


    