# Program 2: Display a 3x3 matrix with row and column sums
matrix = []
print("Enter 9 elements of the 3x3 matrix row by row:")
for i in range(3):
    row = [int(input(f"Element [{i}][{j}]: ")) for j in range(3)]
    matrix.append(row)

print("Matrix with row sums:")
for row in matrix:
    print(*row, "|", sum(row))
column_sums = [sum(matrix[row][col] for row in range(3)) for col in range(3)]
print("Column sums:", *column_sums)
print("Grand total:", sum(column_sums))
