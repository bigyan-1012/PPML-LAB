# Program 2: Draw scatter and bar plots
import matplotlib.pyplot as plt

# Scatter plot
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]
plt.scatter(x, y, color="blue", label="Scatter Points")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar plot
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]
plt.bar(categories, values, color="green", label="Bar Data")
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()
