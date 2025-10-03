import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Sample data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.sin(x)

# cubic spline interpolator
cs = CubicSpline(x, y)

# Evaluate spline at finer points
x_fine = np.linspace(0, 5, 100)
y_fine = cs(x_fine)

# Plot
plt.plot(x, y, 'o', label='data points')
plt.plot(x_fine, y_fine, '-', label='cubic spline')
plt.legend()
plt.show()
