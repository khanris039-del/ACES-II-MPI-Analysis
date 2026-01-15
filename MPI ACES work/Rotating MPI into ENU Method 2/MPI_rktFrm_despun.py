##IMPORTS##
import numpy as np
import spaceToolsLib as stl
from glob import glob
import datetime as dt
from copy import deepcopy

### MAIN FXN ###

def MPI_rktFrm_despun():

    #[1] load data
    path_to_data = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L2 Rocket\\'
    file_name = glob(path_to_data + 'ACES_II_36364_l2_MPI_instrFrm_subtraction_intoRkt.cdf')[0]
    path_to_attitude = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\ACESII_36364_Attitude_Solution.cdf'
    data_dict = stl.loadDictFromFile(file_name)
    data_dict_attitude = stl.loadDictFromFile(path_to_attitude)

    # prepare outputs
    data_dict_output= {}

    # 2. Extract time (seconds) and DCM components
    time_epoch_attitude = data_dict_attitude[f'Epoch'][0]
    time_sec_attitude = stl.EpochTo_T0_Rocket(time_epoch_attitude, T0=time_epoch_attitude[0])
    time_epoch_MPI = data_dict[f'Epoch'][0]
    time_sec_MPI = stl.EpochTo_T0_Rocket(time_epoch_MPI, T0=time_epoch_attitude[0])

    # [DCM elements]
    a11 = np.array(data_dict_attitude['a11'][0])
    a12 = np.array(data_dict_attitude['a12'][0])
    a13 = np.array(data_dict_attitude['a13'][0])
    a21 = np.array(data_dict_attitude['a21'][0])
    a22 = np.array(data_dict_attitude['a22'][0])
    a23 = np.array(data_dict_attitude['a23'][0])
    a31 = np.array(data_dict_attitude['a31'][0])
    a32 = np.array(data_dict_attitude['a32'][0])
    a33 = np.array(data_dict_attitude['a33'][0])

    # 3.  Interps for each DCM element
    dcm_a11 = np.interp(time_sec_MPI, time_sec_attitude, a11)
    dcm_a12 = np.interp(time_sec_MPI, time_sec_attitude, a12)
    dcm_a13 = np.interp(time_sec_MPI, time_sec_attitude, a13)

    dcm_a21 = np.interp(time_sec_MPI, time_sec_attitude, a21)
    dcm_a22 = np.interp(time_sec_MPI, time_sec_attitude, a22)
    dcm_a23 = np.interp(time_sec_MPI, time_sec_attitude, a23)

    dcm_a31 = np.interp(time_sec_MPI, time_sec_attitude, a31)
    dcm_a32 = np.interp(time_sec_MPI, time_sec_attitude, a32)
    dcm_a33 = np.interp(time_sec_MPI, time_sec_attitude, a33)


    for idx in range(4):
        # 4. interp DCM as a fxn of time
        N = len(time_sec_MPI)
        dcm_interp = np.zeros(
            shape=(N, 3, 3))  # for MPI 1 #creating object that is filled with 0s, will get filled our values each loop

        #
        for i in range(N):
            dcm_interp[:, 0, 0] = dcm_a11
            dcm_interp[:, 0, 1] = dcm_a12
            dcm_interp[:, 0, 2] = dcm_a13
            dcm_interp[:, 1, 0] = dcm_a21
            dcm_interp[:, 1, 1] = dcm_a22
            dcm_interp[:, 1, 2] = dcm_a23
            dcm_interp[:, 2, 0] = dcm_a31
            dcm_interp[:, 2, 1] = dcm_a32
            dcm_interp[:, 2, 2] = dcm_a33

        # multiply DCM by instr vec, get rkt
        N = len(time_sec_MPI)
        MPI_vel_vec = np.array([data_dict['Ux'][0], data_dict['Uy'][0], data_dict['Uz'][0]]).T
        MPI_ENU = [dcm_interp[i] @ MPI_vel_vec[i] for i in range(N)]


        # output

        example_attrs = {'LABLAXIS': None, 'DEPEND_0': f'epoch', 'UNITS': 'm/s'}

        data_dict_output = {
            **data_dict_output,
            **{
                f'MPI_E': [np.array(MPI_ENU)[:, 0], deepcopy(example_attrs)],
                f'MPI_N': [np.array(MPI_ENU)[:, 1], deepcopy(example_attrs)],
                f'MPI_U': [np.array(MPI_ENU)[:, 2], deepcopy(example_attrs)],
                f'epoch': [np.array(time_epoch_MPI), deepcopy(example_attrs)],
            }
        }

        # data shift in time
        spin_rate = 0.5474
        if idx == 0: #MPI1
            delta = (1/spin_rate)*(2+0.75)
        elif idx == 1: #MPI2
            delta = (1/spin_rate)*(1+0.5)
        elif idx == 2: #MPI3
            delta =(1/spin_rate)*(1+0.25)
        elif idx == 3: #MPI4
            delta =0

    outputPath = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L3 ENU\\'
    file_out_name = 'ACES_II_36364_l3_MPI_rktFrm_despun.cdf'
    stl.outputCDFdata(outputPath=outputPath + file_out_name, data_dict=data_dict_output)

MPI_rktFrm_despun()



