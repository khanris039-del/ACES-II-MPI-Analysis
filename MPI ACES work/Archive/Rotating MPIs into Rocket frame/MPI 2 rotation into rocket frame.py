# imports
import numpy as np
import time

# time your code
start_time = time.time()


### MAIN FXN ###
def MPI_II_rotation():
    # original vector in the original frame; i think I can prob change this to like load in a data file or something?
    v = np.array([1, 1, 0])

    # establish vars
    z_deg = 90

    # deg to rad
    theta_z = np.deg2rad(z_deg)

    # DCM for rotating abt x axis

    mat_z = np.array([
        [np.cos(theta_z), -np.sin(theta_z), 0],
        [np.sin(theta_z), np.cos(theta_z), 0],
        [0, 0, 1]
    ])

    v_in_new_frame = mat_z.T @ v

    print("vector rotated about z_axis:", v_in_new_frame)


MPI_II_rotation()

