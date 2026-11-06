# Program 4: Find roots of ax^2 + bx + c = 0
import cmath

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

if a == 0:
    print("The coefficient of x^2 cannot be zero.")
else:
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print("The roots are:", root1, "and", root2)
