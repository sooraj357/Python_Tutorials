# Get input from the user
number = int(input("Enter a number: "))
n = int(input("Enter the divisor (n): "))

# Check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")

# Check if the number is divisible by n
if number % n == 0:
    print(f"{number} is divisible by {n}.")
else:
    print(f"{number} is not divisible by {n}.")
