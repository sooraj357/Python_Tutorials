# Get sides from the user
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

# First, check if the sides can form a triangle
if a + b > c and b + c > a and c + a > b:
    # Now check the type
    if a == b == c:
        print("This is an Equilateral triangle.")
    elif a == b or b == c or c == a:
        print("This is an Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")
else:
    print("The given sides do not form a valid triangle.")
  