import ast
# Program 4: Check whether an element is present using a lambda function
values = list(ast.literal_eval(input("Enter a list (example: [1, 2, 3]): ")))
target = int(input("Enter the element to search: "))

is_target = lambda item: item == target
found = any(map(is_target, values))

if found:
    print(target, "is present in the list.")
else:
    print(target, "is not present in the list.")
