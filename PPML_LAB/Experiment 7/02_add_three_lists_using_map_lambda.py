import ast
# Program 2: Add corresponding elements of three lists using map() and lambda
list1 = list(ast.literal_eval(input("Enter the first list: ")))
list2 = list(ast.literal_eval(input("Enter the second list: ")))
list3 = list(ast.literal_eval(input("Enter the third list: ")))

if len(list1) == len(list2) == len(list3):
    result = list(map(lambda a, b, c: a + b + c, list1, list2, list3))
    print("Resultant list:", result)
else:
    print("All three lists must have the same length.")
