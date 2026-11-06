# Program 1: Display grade according to percentage
percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Enter a percentage between 0 and 100.")
elif percentage >= 90:
    print("The equivalent grade is 'O'")
elif percentage >= 80:
    print("The equivalent grade is 'E'")
elif percentage >= 70:
    print("The equivalent grade is 'A'")
elif percentage >= 60:
    print("The equivalent grade is 'B'")
elif percentage >= 50:
    print("The equivalent grade is 'C'")
elif percentage >= 40:
    print("The equivalent grade is 'D'")
else:
    print("The equivalent grade is 'F'")
