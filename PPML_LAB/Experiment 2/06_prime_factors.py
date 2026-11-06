# Program 6: Print all prime factors of a three-digit number
number = int(input("Enter a three-digit positive number: "))

if not 100 <= number <= 999:
    print("Please enter a positive three-digit number.")
else:
    n = number
    factor = 2
    print("Prime factors are:", end=" ")
    while factor * factor <= n:
        while n % factor == 0:
            print(factor, end=" ")
            n //= factor
        factor += 1
    if n > 1:
        print(n, end="")
    print()
