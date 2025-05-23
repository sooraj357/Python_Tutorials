a = int(input("Enter first integer no :"))
b = int(input("Enter second integer no :"))

print(f"Before swap a:{a}  b:{b}")
a = a + b
b = a - b
a = a - b
print(f"After swap a:{a}  b:{b}")
