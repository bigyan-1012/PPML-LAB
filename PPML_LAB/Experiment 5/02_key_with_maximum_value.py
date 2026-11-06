# Program 2: Print the key having the maximum value
import ast

data = ast.literal_eval(input("Enter a dictionary, e.g. {'a': 10, 'b': 20}: "))
if not isinstance(data, dict) or not data:
    print("Please enter a non-empty dictionary.")
else:
    key = max(data, key=data.get)
    print("The key having the maximum value is:", key)
