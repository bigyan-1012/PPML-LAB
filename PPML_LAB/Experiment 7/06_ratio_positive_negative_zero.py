# Program 6: Find ratios of positive, negative and zero values using map()
numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
if not numbers:
    print("The array is empty; ratios cannot be calculated.")
else:
    total = len(numbers)
    counts = [sum(1 for x in numbers if x > 0),
              sum(1 for x in numbers if x < 0),
              sum(1 for x in numbers if x == 0)]
    ratios = list(map(lambda count: round(count / total, 2), counts))
    print("Ratios [positive, negative, zero]:", ratios)
