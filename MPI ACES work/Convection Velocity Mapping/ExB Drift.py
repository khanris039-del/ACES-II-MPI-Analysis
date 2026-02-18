import matplotlib.pyplot as plt
from glob import glob
import spaceToolsLib as stl
import numpy as np
from copy import deepcopy

def ExB_Drift():

    # load the data
    path_to_E = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\Convection Velocity\L2\ACESII_36364_L2_EFI_ENU_fullCal.cdf'
    path_to_B = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\Convection Velocity\L2\ACESII_36364_l2_RingCore_ENU_fullCal.cdf'

    data_dict_E = stl.loadDictFromFile(path_to_E)
    data_dict_B = stl.loadDictFromFile(path_to_B)

    print(data_dict_E.keys())
    print(data_dict_B.keys())


    # Extract arrays
    vecE = np.array([
            data_dict_E['E_E'][0],
            data_dict_E['E_N'][0],
            data_dict_E['E_U'][0],
        ])

    vecB = np.array([
            data_dict_E['B_E'][0],
            data_dict_E['B_N'][0],
            data_dict_E['B_Up'][0],
        ])



    Epoch = data_dict_E['Epoch'][0]

    # Compute ExB drift
    ExB = np.cross(E, B)
    Bmag2 = np.sum(B**2, axis=1)[:, None]

    Drift = ExB / Bmag2

    # Prepare output
    example_attrs = {
        'LABLAXIS': 'ExB Drift Velocity',
        'DEPEND_0': 'Epoch',
        'UNITS': 'm/s'
    }

    data_dict_output = {
        'Epoch': [Epoch, data_dict_E['Epoch'][1]],
        'Drift_ENU': [Drift, deepcopy(example_attrs)]
    }

    outputPath = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\Convection Velocity\L3\\'
    file_out_name = 'ACESII_36364_L3_ExB_Drift_ENU.cdf'

    stl.outputCDFdata(outputPath=outputPath + file_out_name,
                      data_dict=data_dict_output)

ExB_Drift()