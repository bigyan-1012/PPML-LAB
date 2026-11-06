# Program 8: Swap two numbers using bitwise XOR
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping, the value of a:", a)
print("After swapping, the value of b:", b)
