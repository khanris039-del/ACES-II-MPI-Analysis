# --- MPI_ENU_create_reduced_dataset.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: isolate points of the MPI data via cross-correlation
import matplotlib.pyplot as plt
from glob import glob
# imports
import spaceToolsLib as stl
import numpy as np
from scipy.signal import correlate, correlation_lags


def normalization(x, y):
    # x = x- np.mean(x)
    corr = correlate(x, y)
    #norm = np.sqrt(np.sum(x**2) * np.sum(y**2))
    #if norm == 0:
     #   return np.zeros_like(corr)
    output1 = corr/np.max(np.abs(corr))
    #output1 = corr
    output2 = correlation_lags(len(y), len(x))
    return output1, output2

def MPI_ENU_cross_correlation():

    # 1. Load MPI ENU data
    path_to_MPI = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L3 ENU\l3_MPI_ENUFrm.cdf'
    # file_name = glob(path_to_MPI )[0]
    data_dict_MPI = stl.loadDictFromFile(path_to_MPI)

    # prepare the output
    data_dict_output = {}

    # 2. define a regularized time grid to bin all the MPI data onto
    # Note: It MUST be finer resolution than any of the MPI points so that
    # multiple datapoints aren't in the same time bin
    N = 516
    time_space = np.linspace(data_dict_MPI['time1'][0][0], data_dict_MPI['time1'][0][-1]+5, N)
    MPI_E_time_grided = [np.zeros_like(time_space) for i in range(4)]
    MPI_N_time_grided = [np.zeros_like(time_space) for i in range(4)]

    print(time_space[0], time_space[-1])

    for idx in range(4):

        time = data_dict_MPI[f'time{idx+1}'][0]
        MPI_East = data_dict_MPI[f'MPI_E{idx + 1}'][0]
        MPI_North = data_dict_MPI[f'MPI_N{idx + 1}'][0]

        for tdx, tme in enumerate(time):
            target_idx = np.abs(time_space-tme).argmin()
            MPI_E_time_grided[idx][target_idx] = MPI_East[tdx]
            MPI_N_time_grided[idx][target_idx] = MPI_North[tdx]

    ref_probe = 0
    ref_probe_id = ref_probe + 1# MPI 4 → Python index 3

    MPI_E_corr = [[],[]]
    MPI_N_corr = [[],[]]

    for i in range(4):
        output1_corr, output2_lags = normalization(MPI_E_time_grided[ref_probe], MPI_E_time_grided[i])
        MPI_E_corr[0].append(
            output1_corr)

        MPI_E_corr[1].append(output2_lags)

        output1_corr, output2_lags = normalization(MPI_N_time_grided[ref_probe], MPI_N_time_grided[i])
        MPI_N_corr[0].append(
            output1_corr)

        MPI_N_corr[1].append(output2_lags)



    fig, ax = plt.subplots(4, 1)
    for i in range(4):
        ax[0].plot(time_space, MPI_E_time_grided[i], label=f'MPI 4 vs MPI {i + 1}')
        ax[1].plot(time_space, MPI_N_time_grided[i], label=f'MPI 4 vs MPI {i + 1}')
        if i!=3:
            ax[2].plot(MPI_E_corr[1][i], MPI_E_corr[0][i], label=f'MPI {ref_probe_id} vs MPI {i + 2}')
            ax[3].plot(MPI_N_corr[1][i], MPI_N_corr[0][i], label=f'MPI {ref_probe_id} vs MPI {i + 2}')

    #ax[0].set_ylabel('MPI East Ion Drift Velocity (m/s)')
    ax[0].set_xlabel('Time from T0 (seconds, T0 = 2022-11-20 15:25:31)')
    ax[0].legend()

    #ax[1].set_ylabel('MPI North Ion Drift Velocity (m/s)')
    ax[1].set_xlabel('MPI 4 Reference Correlation Function')
    ax[1].legend()

    ax[2].set_ylabel('Norm_E. XCorr')
    ax[2].set_xlim(-100, 100)
    ax[2].legend()

    ax[3].set_ylabel('Norm_N. XCorr')
    ax[3].set_xlim(-100, 100)
    ax[3].legend()


    plt.show()



    # just plot the multiplication for everything
    # ax[2].plot(time_space, np.abs(MPI_E_time_grided[0]*MPI_E_time_grided[3]*MPI_E_time_grided[1]))
    #
    # plt.show()




    # 4. put our data in an output

    example_attrs = {'LABLAXIS': None, 'DEPEND_0': f'time{idx + 1}', 'UNITS': None}

    # data_dict_output = {**data_dict_output,
    #                     **{'time': [np.array(target_idx), {}]},
    #                     **{f'MPI{j}_E_reduced': [np.array(MPI_E_corr[j]), {'DEPEND_0':'time'}] for j in range(4)},
    #                     **{f'MPI{k}_N_reduced': [np.array(MPI_N_corr[k]), {'DEPEND_0': 'time'}] for k in range(4)},
    #                     }
    #
    #
    # # --- 9. Output new CDF ---
    # file_out_path =  r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L3 ENU\\ACES_II_36364_l3_MPI_ENU_cross_correlation.cdf'
    # #file_out_name = 'ACES_II_36364_l3_MPI_ENU_cross_correlation.cdf'
    # stl.outputDataDict(outputPath=file_out_path, data_dict=data_dict_output)


###EXECUTE###
MPI_ENU_cross_correlation()