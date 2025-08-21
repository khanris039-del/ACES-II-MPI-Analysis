import numpy as np

# 3x3by 3x1 multiply

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = np.array([1,2,3])
#
# print(np.matmul(a,b))


# rotation matrix example
# rotate (1,1,0) to align with y axis

a = np.array([1,1,0])
angle = np.radians(-45)
Rz = np.array([
    [np.cos(angle), -1*np.sin(angle), 0],
    [np.sin(angle), np.cos(angle), 0],
    [0,0,1]
])

print(np.matmul(Rz, a))

#get the magnitude of a vector

print(np.linalg.norm(a))

# learn this:
# scipy.Cubicspline


#how to find a specific INDEX in an array
# np.abs().argmin()

#a = np.array([9,5,11,41])

#print(np.abs(a - 7).argmin())