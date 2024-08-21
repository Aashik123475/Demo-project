print("select the operation by its")
print("1:add")
print("2:sub")
print("3:mul")
print("4:div")
x=int(input("enter the number of your operation: "))
if x in (1,2,3,4):
    a=int(input("number 1: "))
    b=int(input("number 2: "))
    if x==1:
        print(a+b)
    elif x==2:
        print(a-b)
    elif x==3:
        print(a*b)
    elif x==4:
        if a==0:
            print("its undefined")
        print(a/b)
else:
    print("sorry!the given code is unavailable")
        




# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to get user input and perform the operation
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input")

# Run the calculator
calculator()
