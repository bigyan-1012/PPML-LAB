# Program 5: Draw a 3D scatter plot
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = [2, 3, 3, 3, 2]

ax.scatter(x, y, z, color="red", label="3D Points")
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.legend()
plt.show()
