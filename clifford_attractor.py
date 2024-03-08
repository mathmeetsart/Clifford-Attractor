import matplotlib.pyplot as plt
import numpy as np

def clifford(x, y, a, b, c, d):
    """
    Compute the next point in the Clifford attractor iteration.

    Parameters:
        x (float): The x-coordinate of the current point.
        y (float): The y-coordinate of the current point.
        a (float): The parameter controlling the x-coordinate transformation.
        b (float): The parameter controlling the y-coordinate transformation.
        c (float): The parameter controlling the x-coordinate transformation.
        d (float): The parameter controlling the y-coordinate transformation.

    Returns:
        tuple: The x and y coordinates of the next point in the iteration.
    """
    # Compute the next point using the Clifford attractor equations
    next_x = np.sin(a * y) + c * np.cos(a * x)
    next_y = np.sin(b * x) + d * np.cos(b * y)
    
    return next_x, next_y


# Parameters for the Clifford attractor
a = -1.3
b = -1.3
c = -1.8
d = -1.9

# Initial coordinates
x = 0.1
y = 0.1


# Store points
points = []
for i in range(1000000):
    # Compute the next point in the iteration
    x, y = clifford(x, y, a, b, c, d)
    # Append the next point to the list of points
    points.append((x, y))

# Unpack points for plotting
x_values, y_values = zip(*points)

# Plotting
plt.figure(figsize=(16, 16))  # Set the size of the plot
plt.axis("off")  # Turn off the axis
plt.scatter(x_values, y_values, s=0.005, alpha=0.5, color="black")  # Plot the points
                                                                    # s controls point size, alpha controls transparency
# Optionally, save the plot as an image file
# plt.savefig("clifford_attractor.png", dpi=1200)  # Save the plot as a PNG file with high resolution

plt.show()  # Show the plot
