import matplotlib.pyplot as plt
from glob import glob
import spaceToolsLib as stl
import numpy as np
from copy import deepcopy
import datetime as dt

#decorate my func
from timebudget import timebudget
@timebudget
def ExB_Drift():

    # load the data
    path_to_E = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\Convection Velocity\L2\ACESII_36364_L2_EFI_ENU_fullCal.cdf'
    path_to_B = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\Convection Velocity\L2\ACESII_36364_l2_RingCore_ENU_fullCal.cdf'

    data_dict_E = stl.loadDictFromFile(path_to_E)
    data_dict_B = stl.loadDictFromFile(path_to_B)


    # Extract arrays
    vecE = np.array([
            data_dict_E['E_E'][0],
            data_dict_E['E_N'][0],
            data_dict_E['E_Up'][0],
        ])

    vecB = (np.array([
            data_dict_B['B_E'][0],
            data_dict_B['B_N'][0],
            data_dict_B['B_U'][0],
        ]) +
            np.array([
            data_dict_B['B_model_E'][0],
            data_dict_B['B_model_N'][0],
            data_dict_B['B_model_U'][0],
        ])
            )* (1E-9)

    #turn dt into secs
    T0 = dt.datetime(2022, 11, 20, 17, 20)

    B_Epoch_T0 = stl.EpochTo_T0_Rocket(data_dict_B['Epoch'][0], T0=T0)
    E_Epoch_T0 = stl.EpochTo_T0_Rocket(data_dict_E['Epoch'][0], T0=T0)

    # interpolate E onto B so they are the same size


    vecE_interp = [[], [], []]
    for i in range(3):
        vecE_interp[i] = np.interp(B_Epoch_T0, E_Epoch_T0, vecE[i])
    vecE_interp = np.array(vecE_interp)


    # Compute ExB drift
    ExB = np.cross(vecE_interp, vecB, axis = 0)
    Bmag_sq = (np.square(data_dict_B['Bmag'][0])) * (1E-18)
    Drift = ExB / Bmag_sq

    # Prepare output
    example_attrs = {
        'LABLAXIS': 'ExB Drift Velocity',
        'DEPEND_0': 'Epoch',
        'UNITS': 'm/s'
    }

    data_dict_output = {
        'Epoch': [data_dict_B['Epoch'][0], data_dict_B['Epoch'][1]],
        'Drift_E': [Drift[0], deepcopy(example_attrs)],
        'Drift_N': [Drift[1], deepcopy(example_attrs)],
        'Drift_U': [Drift[2], deepcopy(example_attrs)]
    }

    outputPath = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\Convection Velocity\L3\\'
    file_out_name = 'ACESII_36364_L3_ExB_Drift_ENU.cdf'

    stl.outputCDFdata(outputPath=outputPath + file_out_name,
                      data_dict=data_dict_output)

ExB_Drift()