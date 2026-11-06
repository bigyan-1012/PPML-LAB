# Program 6: Combine two sets of strings and remove duplicates
import ast

set1 = set(ast.literal_eval(input("Enter the first string set: ")))
set2 = set(ast.literal_eval(input("Enter the second string set: ")))
new_set = set1.copy()
new_set.update(set2)
print("After combining the sets:", new_set)
