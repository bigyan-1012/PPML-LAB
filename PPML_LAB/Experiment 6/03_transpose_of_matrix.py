# Program 3: Print the transpose of a matrix
rows = int(input("Give the number of rows: "))
columns = int(input("Give the number of columns: "))
matrix = [[int(input(f"Element [{r}][{c}]: ")) for c in range(columns)] for r in range(rows)]
print("Original Matrix:")
for row in matrix:
    print(*row)
print("Matrix after transpose:")
for c in range(columns):
    print(*(matrix[r][c] for r in range(rows)))
