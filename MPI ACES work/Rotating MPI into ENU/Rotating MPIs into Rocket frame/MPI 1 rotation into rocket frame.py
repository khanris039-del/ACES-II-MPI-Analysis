import numpy as np

# ok need to combine DCM_x and DCM_y

# imports
import numpy as np
import time

# time your code
start_time = time.time()


### MAIN FXN ###
def MPI_I_rotation():
    # original vector in the original frame; i think I can prob change this to like load in a data file or something?
    v = np.array([1, 1, 0])

    # establish vars
    x_deg = 90
    y_deg = 90

    # deg to rad
    theta_x = np.deg2rad(x_deg)
    theta_y = np.deg2rad(y_deg)

    # DCM for rotating abt x axis

    DCM_x = np.array([
        [1, 0, 0],
        [0, np.cos(theta_x), -np.sin(theta_x)],
        [0, np.sin(theta_x), np.cos(theta_x)]
    ])

    # DCM for rotating abt y axis

    DCM_y = np.array([
        [np.cos(theta_y), 0, np.sin(theta_y)],
        [0, 1, 0],
        [-np.sin(theta_y), 0, np.cos(theta_y)]
    ])

    #combined matrix
    DCM_MPI_1 = np.dot(DCM_y, DCM_x)

    v_in_new_frame = DCM_MPI_1.T @ v

    print("vector rotated:", v_in_new_frame)


MPI_I_rotation()

