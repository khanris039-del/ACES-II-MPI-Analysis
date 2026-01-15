# --- MPI_ENU_create_reduced_dataset.py ---
# --- Author: C. Feltman ---
# DESCRIPTION: isolate points of the MPI data

# imports
import spaceToolsLib as stl
import numpy as np
from glob import glob


def MPI_ENU_create_reduced_dataset():

    # 1. Load MPI ENU data
    path_to_data = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L3 ENU\l3_MPI_ENUFrm.cdf'
    file_name = glob(path_to_data )[0]
    path_to_attitude = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\ACESII_36364_Attitude_Solution.cdf'
    data_dict_MPI = stl.loadDictFromFile(file_name)


    # prepare the output
    data_dict_output = {}

    # 2. define some ideal time points as seconds from launch
    # Note: ONLY pick times where there's good correlation between MPI_East AND MPI_North
    target_times = [
        184.18,
        207.94,
        264.7,
    ]


    # 3. collect all the points into a new dataset and write them out in a data_dict_output.
    # note: write each MPI data individually, not as a single dataset.

    MPI_E_reduced = [[], [], [], []]
    MPI_N_reduced = [[], [], [], []]

    for idx in range(4):
        time = data_dict_MPI[f'time{idx + 1}'][0]
        MPI_East = data_dict_MPI[f'MPI_E{idx+1}'][0]
        MPI_North = data_dict_MPI[f'MPI_N{idx+1}'][0]

        for tme in target_times:

            target_idx = np.abs(time - tme).argmin()

            MPI_E_reduced[idx].append(MPI_East[target_idx])
            MPI_N_reduced[idx].append(MPI_North[target_idx])


        # 4. put our data in an output

        data_dict_output = {**data_dict_output,
                            **{
                                f'MPI_E{idx+1}_reduced': [np.array(MPI_E_reduced[idx]),{'DEPEND_0':'time'}],
                                f'MPI_N{idx+1}_reduced': [np.array(MPI_N_reduced[idx]), {'DEPEND_0': 'time'}]
                            }
                            }

    data_dict_output = {**data_dict_output,
                        **{
                            'time': [np.array(target_times), {}],
                        }
                        }
    # --- 9. Output new CDF ---
    outputPath = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\L3 ENU\\'
    file_out_name = 'ACES_II_36364_l3_MPI_EN_reduced.cdf'
    stl.outputCDFdata(outputPath=outputPath + file_out_name, data_dict=data_dict_output)


###EXECUTE###
MPI_ENU_create_reduced_dataset()