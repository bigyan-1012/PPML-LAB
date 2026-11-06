import ast
# Program 3: Raise each base to its corresponding exponent using map()
bases = list(ast.literal_eval(input("Enter the base list: ")))
exponents = list(ast.literal_eval(input("Enter the exponent list: ")))

if len(bases) == len(exponents):
    result = list(map(lambda base, exponent: base ** exponent, bases, exponents))
    print("Resultant list:", result)
else:
    print("Both lists must have the same length.")
