# Program 2: Combine one item from each of two lists at a time
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D", "E"]

combined = []
for number, letter in zip(list1, list2):
    combined.append(number)
    combined.append(letter)

print("Combined list:", combined)
