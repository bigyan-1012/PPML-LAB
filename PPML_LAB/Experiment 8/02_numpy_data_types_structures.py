# Program 2: Data types and structures in NumPy
import numpy as np

arr = np.array([1, 2, 3], dtype="int32")
print("Array:", arr)
print("Data type:", arr.dtype)

arr = arr.astype("float64")
print("Updated array:", arr)
print("Updated type:", arr.dtype)
