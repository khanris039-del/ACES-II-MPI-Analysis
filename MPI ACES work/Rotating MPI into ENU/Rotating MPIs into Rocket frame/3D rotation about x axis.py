# imports
import numpy as np
import time

# time your code
start_time = time.time()

### MAIN FXN ###
def rotation_about_x_axis():

    #original vector in the original frame; i think I can prob change this to like load in a data file or something?
    v = np.array ([1, 1, 0])

    #establish vars
    x_deg = 90

    #deg to rad
    theta_x = np.deg2rad(x_deg)

    #DCM for rotating abt x axis

    DCM_x = np.array([
        [1, 0, 0],
        [0, np.cos(theta_x), -np.sin(theta_x)],
        [0, np.sin(theta_x), np.cos(theta_x)]
    ])

    v_in_new_frame = DCM_x.T @ v

    print("vector rotated about x_axis:", v_in_new_frame)



rotation_about_x_axis()

