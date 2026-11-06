import ast
# Program 1: Input and merge two dictionaries
dict1 = ast.literal_eval(input("Enter the first dictionary (example: {'a': 1}): "))
dict2 = ast.literal_eval(input("Enter the second dictionary (example: {'b': 2}): "))

merged = dict1.copy()
merged.update(dict2)
print("After merging the dictionaries:", merged)
