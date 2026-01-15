# imports
import numpy as np
import time

# time your code
start_time = time.time()


### MAIN FXN ###
def rotation_about_y_axis():
    # original vector in the original frame; i think I can prob change this to like load in a data file or something?
    v = np.array([1, 1, 0])

    # establish vars
    y_deg = 90

    # deg to rad
    theta_y = np.deg2rad(y_deg)

    # DCM for rotating abt y axis

    DCM_y = np.array([
        [np.cos(theta_y), 0, np.sin(theta_y)],
        [0, 1, 0],
        [-np.sin(theta_y), 0, np.cos(theta_y)]
    ])

    v_in_new_frame = DCM_y.T @ v

    print("vector rotated about y_axis:", v_in_new_frame)


rotation_about_y_axis()

