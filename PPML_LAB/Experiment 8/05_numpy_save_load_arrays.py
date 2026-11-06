# Program 5: Save and load NumPy arrays
import numpy as np

arr = np.array([1, 2, 3, 4])
np.save("my_array.npy", arr)

loaded_arr = np.load("my_array.npy")
print("Loaded array:", loaded_arr)
