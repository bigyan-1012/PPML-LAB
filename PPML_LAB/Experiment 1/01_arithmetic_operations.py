# Program 1: Perform arithmetic operations on two integers
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print("Addition is:", x + y)
print("Subtraction is:", x - y)
print("Multiplication is:", x * y)

if y != 0:
    print("Division is:", x / y)
    print("Remainder is:", x % y)
    print("Floor division is:", x // y)
else:
    print("Division, remainder and floor division are not possible when y is 0.")
