# Program 6: Convert meters into kilometers and remaining meters
meters = int(input("Enter distance in meters: "))
if meters < 0:
    print("Distance cannot be negative.")
else:
    kilometers = meters // 1000
    remaining_meters = meters % 1000
    print(kilometers, "kilometer(s)", remaining_meters, "meter(s)")
