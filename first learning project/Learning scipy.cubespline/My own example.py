import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

#---CREATING SAMPLE DATA
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0.3, 0.9, 1.2, 3.5, -0.4, 5.2])

# ---CUBIC SPLINE INTERP
cs = CubicSpline(x, y, bc_type='not-a-knot', extrapolate=True)

#---GRID
x_fine = np.linspace(0, 5, 200)
y_fine = cs(x_fine)

#---TAKING THE DERIVATIVES
dy_dx = cs(x_fine, nu=1)   # 1st derivative
d2y_dx2 = cs(x_fine, nu=2) # 2nd derivative

#---PLOT
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Original data')
plt.plot(x_fine, y_fine, '-', label='Cubic Spline')
plt.plot(x_fine, dy_dx, '--', label='1st Derivative')
plt.plot(x_fine, d2y_dx2, ':', label='2nd Derivative')
plt.legend()
plt.title("CubicSpline interpolation and derivatives")
plt.xlabel("x")
plt.ylabel("y / derivatives")
plt.grid(True)
plt.show()
