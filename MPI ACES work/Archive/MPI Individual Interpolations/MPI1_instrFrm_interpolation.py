#This is my attempt at interpolating the MPI1 data in instrument form.

# imports
import numpy as np
import spaceToolsLib as stl


### MAIN FXN ###

def MPI1_instrFrm_interpolation
    # [1] load in the MPI data
    path_to_data = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L1 instr\\'
    file_name = glob(path_to_data + "ACES_II_36364_l1_MPI_instrFrm.cdf")[0]
    data_dict = stl.loadDictFromFile(file_name)

    # [2] pull the data
