
#A = Final amount (principal + interest)

#P = Principal (initial amount)

#r = Annual interest rate (in decimal; e.g., 5% → 0.05)

#n = Number of times interest is compounded per year

#t = Time in years


P = float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (in %): "))
T = float(input("Enter the time (in years): "))
N = int(input("Enter the number of times interest is compounded per year: "))

# Calculate compound interest
A = P * (1 + R / (100 * N)) ** (N * T)
compound_interest = A - P

# Display the result
print(f"The total amount after {T} years is: {A:.2f}")
print(f"The compound interest is: {compound_interest:.2f}")
