# Task2: Recursive Function 

def factorial(n):
    if n==0 or n==1:
        return 1;
    elif n<0:
        print("Number is Negative")
    else:
        return n*factorial(n-1)
    
print(f"factorial(5)={factorial(5)}")
print(f"factorial(0)={factorial(0)}")
print(f"factorial(-3)={factorial(-3)}")
        