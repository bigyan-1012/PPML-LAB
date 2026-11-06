# Program 5: Print Fibonacci series up to n terms using a lambda function
from functools import reduce

n = int(input("Enter the number of terms: "))
if n <= 0:
    print("Enter a positive number of terms.")
else:
    fibonacci = lambda count: reduce(
        lambda seq, _: seq + [seq[-1] + seq[-2]], range(2, count), [0, 1][:count]
    )
    print("Fibonacci series:", fibonacci(n))
