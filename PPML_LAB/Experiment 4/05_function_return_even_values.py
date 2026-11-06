# Program 5: Function that returns even values from a list
def even_values(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

values = [int(item) for item in input("Enter integers separated by commas: ").split(",")]
print("List containing even values:", even_values(values))
