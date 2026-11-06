# Program 3: Check whether a number is a palindrome
number = int(input("Enter a number: "))
original = number
reverse = 0
temp = abs(number)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if number >= 0 and original == reverse:
    print("It is a palindrome number.")
else:
    print("It is not a palindrome number.")
