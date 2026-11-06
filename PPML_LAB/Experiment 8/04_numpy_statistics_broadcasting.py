# Program 4: Statistical operations and broadcasting on arrays
import numpy as np

arr = np.array([1, 2, 3, 4])
print("Maximum:", arr.max())
print("Minimum:", arr.min())
print("Sum:", arr.sum())
print("Product:", arr.prod())
print("Broadcasted result:", arr + 5)
