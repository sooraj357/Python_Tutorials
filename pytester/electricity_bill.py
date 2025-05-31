# Get input from the user
units = float(input("Enter the number of units consumed: "))

# Initialize bill amount
bill = 0.0

# Calculate bill based on slabs
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.0)
else:
    bill = (100 * 1.5) + (100 * 2.0) + ((units - 200) * 3.0)

# Display the result
print(f"Total electricity bill for {units} units is ₹{bill:.2f}")
