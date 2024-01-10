def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else: 
        print("Cannot perform division by zero")
    
print("Simple Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

operationToBePerformed = int(input("Enter the Operation (1/2/3/4): "))
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if operationToBePerformed == 1:
    result = add(number1, number2)
    operation = "Addition"
elif operationToBePerformed == 2:
    result = subtract(number1, number2)
    operation = "Subtraction"
elif operationToBePerformed == 3:
    result = multiply(number1, number2)
    operation = "Multiplication"
elif operationToBePerformed == 4:
    result = divide(number1, number2)
    operation = "Division"
else:
    result = "Invalid input"
    operation = "Invalid Operation"

print(f"{operation} Result : {result}")