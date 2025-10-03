import matplotlib.pyplot as plt

xdata = [3*(i+1) for i in range(5)]
ydata = [9*(i+1) for i in range(5)]


# # simple way -- non-object oriented
# plt.plot(xdata, ydata)
# plt.xlabel('x numbers')
# plt.ylabel('y numbers')
# plt.show()

# NON SIMPLE -- OBJECT ORIENTED

fig, ax = plt.subplots()
ax.plot(xdata, ydata)
ax.set_xlabel('x numbers')
ax.set_ylabel('y numbers')
plt.show()
