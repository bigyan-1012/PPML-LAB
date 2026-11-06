import ast
# Program 6: Find intersection of two arrays using lambda
array1 = list(ast.literal_eval(input("Enter the first list (example: [1, 2, 3]): ")))
array2 = list(ast.literal_eval(input("Enter the second list (example: [2, 3, 4]): ")))

intersection = list(filter(lambda item: item in array1, array2))
print("Intersection of the two arrays:", intersection)
