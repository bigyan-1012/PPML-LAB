# Program 2: Print digits at odd locations in a five-digit number
number = input("Enter a five-digit number: ")
if len(number) != 5 or not number.isdigit():
    print("Please enter exactly five digits.")
else:
    print("Digits at odd positions:")
    for index in range(0, 5, 2):
        print(number[index])
