#now performing the subtraction of opposite facing MPI instruments

##IMPORTS##
import numpy as np
import spaceToolsLib as stl
from glob import glob
import datetime as dt
from copy import deepcopy

### MAIN FXN ###

def MPI_instrFrm_subtraction_intoRkt():
    #[1] load the interpolated data
    #print(glob(r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L1 instr\\'))

    path_to_data = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L1 instr\\'
    file_name = glob(path_to_data + "ACES_II_36364_l1_MPI_instrFrm_on4.cdf")[0]
    data_dict = stl.loadDictFromFile(file_name)

    #print(glob(r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L1 instr\\'))
    # prepare outputs
    data_dict_output = {}


    Uz = data_dict['Vx_MPI1_instrFrm_onto_MPI4'][0] - data_dict['Vx_MPI3_instrFrm_onto_MPI4'][0]
    Uy = data_dict['Vx_MPI4_instrFrm_onto_MPI4'][0] - data_dict['Vx_MPI2_instrFrm_onto_MPI4'][0]
    Ux = np.sum(np.array([data_dict[f'Vy_MPI{i+1}_instrFrm_onto_MPI4'][0] for i in range(4)]).T, axis=1)/4

    example_attrs = {'LABLAXIS': None, 'DEPEND_0': 'Epoch', 'UNITS': None}

    data_dict_output={
        'Ux' : [Ux, deepcopy(example_attrs)],
        'Uy': [Uy, deepcopy(example_attrs)],
        'Uz': [Uz, deepcopy(example_attrs)],
        'Epoch': deepcopy(data_dict['time_epoch_MPI4'])
    }

    outputPath = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L2 Rocket\\'
    file_out_name = 'ACES_II_36364_l2_MPI_instrFrm_subtraction_intoRkt.cdf'
    stl.outputCDFdata(outputPath=outputPath + file_out_name, data_dict=data_dict_output)


MPI_instrFrm_subtraction_intoRkt()





