# Program 7: Convert minutes into hours and minutes
total_minutes = int(input("Enter time in minutes: "))
if total_minutes < 0:
    print("Time cannot be negative.")
else:
    hours = total_minutes // 60
    minutes = total_minutes % 60
    print(hours, "hour(s)", minutes, "minute(s)")
