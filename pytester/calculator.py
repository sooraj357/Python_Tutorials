# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on operator
if operator == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use one of: +, -, *, /")
 