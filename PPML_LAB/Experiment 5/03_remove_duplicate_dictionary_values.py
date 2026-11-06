import ast
# Program 3: Remove duplicate values from a dictionary, keeping first occurrence
data = ast.literal_eval(input("Enter a dictionary (example: {'a': 1, 'b': 1, 'c': 2}): "))

result = {}
seen_values = set()

for key, value in data.items():
    if value not in seen_values:
        result[key] = value
        seen_values.add(value)

print("Dictionary after removing duplicate values:", result)
