# Program 2: Find the area of a triangle using Heron's formula
import math

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of triangle is:", area)
else:
    print("The given sides do not form a triangle.")
