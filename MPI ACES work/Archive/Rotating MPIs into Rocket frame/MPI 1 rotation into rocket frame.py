import numpy as np

# ok need to combine DCM_x and DCM_y

# imports
import numpy as np
import time

# time your code
start_time = time.time()


### MAIN FXN ###
def MPI_I_rotation():
    cdf_data = stl.loadDictFromFile(file_path)
    v = np.array([1, 1, 0])

    # establish vars
    x_deg = 90
    y_deg = 90

    # deg to rad
    theta_x = np.deg2rad(x_deg)
    theta_y = np.deg2rad(y_deg)

    # matrix for rotating abt x axis

    mat_x = np.array([
        [1, 0, 0],
        [0, np.cos(theta_x), -np.sin(theta_x)],
        [0, np.sin(theta_x), np.cos(theta_x)]
    ])

    # DCM for rotating abt y axis

    mat_y = np.array([
        [np.cos(theta_y), 0, np.sin(theta_y)],
        [0, 1, 0],
        [-np.sin(theta_y), 0, np.cos(theta_y)]
    ])

    #combined matrix
    mat_MPI_1 = np.dot(mat_y, mat_x)

#dot product
    v_in_new_frame = mat_MPI_1.T @ v

    print("vector rotated:", v_in_new_frame)


MPI_I_rotation()

