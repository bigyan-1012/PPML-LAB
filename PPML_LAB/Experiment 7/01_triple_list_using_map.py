import ast
# Program 1: Triple all numbers in a list using map()
numbers = list(ast.literal_eval(input("Enter a list of integers (example: [1, 2, 3]): ")))

def triple(number):
    return number * 3

result = list(map(triple, numbers))
print("Tripled list:", result)
