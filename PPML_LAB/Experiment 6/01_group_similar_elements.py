# Program 1: Group similar elements into a matrix (list of lists)
from collections import Counter

values = [1, 3, 5, 1, 3, 2, 5, 4, 2, 1]
print("Original list:", values)

counts = Counter(values)
grouped_matrix = [[value] * count for value, count in counts.items()]
print("Matrix after grouping:", grouped_matrix)
