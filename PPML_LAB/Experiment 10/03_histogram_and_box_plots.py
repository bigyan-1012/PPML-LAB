# Program 3: Draw histogram and box plots
import matplotlib.pyplot as plt

# Histogram
histogram_data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
plt.hist(histogram_data, bins=5, color="purple", label="Histogram Data")
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Box plot
box_data = [7, 8, 5, 6, 9, 10, 15, 20, 21]
plt.boxplot(box_data)
plt.title("Box Plot")
plt.show()
