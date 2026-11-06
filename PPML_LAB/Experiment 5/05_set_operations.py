import ast
# Program 5: Perform set operations on two sets
set1 = set(ast.literal_eval(input("Enter the first set (example: {1, 2, 3}): ")))
set2 = set(ast.literal_eval(input("Enter the second set (example: {2, 3, 4}): ")))

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (first - second):", set1.difference(set2))
print("Symmetric difference:", set1.symmetric_difference(set2))
