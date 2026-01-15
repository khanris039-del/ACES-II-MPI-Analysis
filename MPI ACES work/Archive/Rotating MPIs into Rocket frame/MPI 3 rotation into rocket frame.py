import numpy as np

# ok need to combine DCM_x and DCM_y

# imports
import numpy as np
import time

# time your code
start_time = time.time()


### MAIN FXN ###
def MPI_III_rotation():
    # original vector in the original frame; i think I can prob change this to like load in a data file or something?
    v = np.array([1, 1, 0])

    # establish vars
    y_deg = -90
    z_deg = 90

    # deg to rad
    theta_y = np.deg2rad(y_deg)
    theta_z = np.deg2rad(z_deg)

    # mat for rotating abt y axis

    mat_y = np.array([
        [np.cos(theta_y), 0, np.sin(theta_y)],
        [0, 1, 0],
        [-np.sin(theta_y), 0, np.cos(theta_y)]
    ])

    # mat for rotating abt z axis

    mat_z = np.array([
        [np.cos(theta_z), -np.sin(theta_z), 0],
        [np.sin(theta_z), np.cos(theta_z), 0],
        [0, 0, 1]
    ])

    #combined matrix
    mat_MPI_3 = np.dot(mat_z, mat_y)

    v_in_new_frame = mat_MPI_3.T @ v

    print("vector rotated:", v_in_new_frame)


MPI_III_rotation()

