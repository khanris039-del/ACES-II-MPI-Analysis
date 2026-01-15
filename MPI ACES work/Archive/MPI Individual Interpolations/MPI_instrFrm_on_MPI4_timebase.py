#now trying a new method of data integration
#this program will pull out the MPI_1 data points and place them onto the time-base of MPI_3.
#from what I remember, we want to choose whichever instrument has the least amount of data points,
#and treat that as the main timebase. Then, pull points from the other instrument which line up with the points from the
#time base instrument, and plot those. This is my attempt at that, where the MPI_3 is the "gospel"
from copy import deepcopy

##IMPORTS##
import numpy as np
import spaceToolsLib as stl
from glob import glob
import datetime as dt

### MAIN FXN ###

def MPI_instrFrm_on_MPI4_timebase():
    # [1] load in the MPI data
    path_to_data = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L1 instr\\'
    file_name = glob(path_to_data + "ACES_II_36364_l1_MPI_instrFrm.cdf")[0]
    data_dict = stl.loadDictFromFile(file_name)

    # prepare the outputs
    data_dict_output = {}

    # [2] extract the time data, vx and vy

    time_sec = []
    MPI_vx = [[], [], [], []]
    MPI_vy = [[], [], [], []]

    for idx in range(4):
        T0 = dt.datetime(2022, 11, 20, 17, 20) #reference time

        #converting all MPI into secs

        time_epoch_MPI = data_dict[f'Epoch_MPI{idx+1}'][0]
        time_sec_MPI = stl.EpochTo_T0_Rocket(time_epoch_MPI, T0=T0)

        #converting MPI 4 into secs
        time_epoch_MPI4 = data_dict[f'Epoch_MPI4'][0]
        time_sec_MPI4 = stl.EpochTo_T0_Rocket(time_epoch_MPI4, T0=T0)

        #interpolate the Vx and Vy

        for idx2, element in enumerate(['x', 'y']):
            interp = np.interp(time_sec_MPI4, time_sec_MPI, data_dict[f'V{element}_instr_MPI{idx+1}'][0])

            if idx2 == 0:
                MPI_vx[idx]= interp

            elif idx2 == 1:
                MPI_vy[idx] = interp




    # Vx_instr_MPI1 = np.array(data_dict['Vx_instr_MPI1'][0])
    # Vy_instr_MPI3 = np.array(data_dict['Vy_instr_MPI1'][0])
    # Vx_instr_MPI3 = np.array(data_dict['Vx_instr_MPI3'][0])
    # Vy_instr_MPI1 = np.array(data_dict['Vy_instr_MPI1'][0])
    #
    # # turn datetimes back into seconds
    #
    #
    # # [3] interpolate the data
    # Vx_interp = np.interp(time_sec_MPI3, time_sec_MPI1, Vx_instr_MPI1)
    # Vy_interp = np.interp(time_sec_MPI3, time_sec_MPI1, Vy_instr_MPI1)

    # [4] output dictionary
        example_attrs = {'LABLAXIS': None, 'DEPEND_0': 'time_epoch_MPI4', 'UNITS': None}

        data_dict_output = {**data_dict_output,
                        **{
                            f'Vx_MPI{idx+1}_instrFrm_onto_MPI4': [MPI_vx[idx], deepcopy(example_attrs)],
                            f'Vy_MPI{idx+1}_instrFrm_onto_MPI4': [MPI_vy[idx], deepcopy(example_attrs)],


                        }
                        }
    example_attrs = {'LABLAXIS': None, 'DEPEND_0': 'time_epoch_MPI4', 'UNITS': None}
    data_dict_output = {**data_dict_output,
        **{
            'Time_sec_MPI4': [time_sec_MPI4, {}],
            'time_epoch_MPI4':[time_epoch_MPI4, {}]
            }
            }

    # [5] write out the data
    outputPath = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L1 instr\\'
    file_out_name = 'ACES_II_36364_l1_MPI_instrFrm_on4.cdf'
    stl.outputCDFdata(outputPath=outputPath + file_out_name, data_dict=data_dict_output)

### EXECUTE ###
MPI_instrFrm_on_MPI4_timebase()
