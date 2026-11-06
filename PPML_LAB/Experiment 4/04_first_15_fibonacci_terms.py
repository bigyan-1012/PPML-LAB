# Program 4: Print the first 15 terms of Fibonacci series without recursion
def fibonacci():
    a, b = 1, 1
    for _ in range(15):
        print(a, end=" ")
        a, b = b, a + b
    print()

print("First 15 terms of Fibonacci series:")
fibonacci()
