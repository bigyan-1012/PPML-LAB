# Program 4: Check whether a number is perfect
number = int(input("Enter a number: "))
divisor_sum = 0

if number > 1:
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

if number > 1 and divisor_sum == number:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")
