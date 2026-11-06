# Program 1: Find second largest and second smallest among entered integers
numbers = []
count = int(input("Enter the number of elements: "))

for i in range(count):
    numbers.append(int(input("Enter element: ")))

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

if len(unique_numbers) < 2:
    print("At least two distinct elements are required.")
else:
    largest = second_largest = float("-inf")
    smallest = second_smallest = float("inf")

    for number in unique_numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number

    print("Second largest element is:", second_largest)
    print("Second smallest element is:", second_smallest)
