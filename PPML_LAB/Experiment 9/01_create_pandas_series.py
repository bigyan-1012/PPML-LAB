# Program 1: Create and work with a Pandas Series
import pandas as pd

data = [10, 20, 30]
labels = ["a", "b", "c"]
series = pd.Series(data, index=labels)

print("Pandas Series:")
print(series)
print("Value at label 'b':", series["b"])
