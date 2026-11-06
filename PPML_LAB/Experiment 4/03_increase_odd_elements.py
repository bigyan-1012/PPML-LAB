# Program 3: Increase odd-valued elements in a list by 5
numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    numbers.append(int(input("Enter element: ")))

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] += 5

print("Updated list:", numbers)
