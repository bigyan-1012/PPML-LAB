# Program 4: Copy set elements into a new set one element at a time
import ast

original_set = set(ast.literal_eval(input("Enter set elements, e.g. {1, 2, 3}: ")))
new_set = set()
for element in original_set:
    new_set.add(element)
print("Updated set is:", new_set)
