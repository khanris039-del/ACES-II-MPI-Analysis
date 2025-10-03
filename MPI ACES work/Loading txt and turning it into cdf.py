# imports
import numpy as np
import spaceToolsLib as stl
from copy import deepcopy

file_path = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\ACESII_36359_Attitude_Solution.cdf'

# [1] load the CDF into a dictionary
cdf_data = stl.loadDictFromFile(file_path)
print("Keys in file:", list(cdf_data.keys()))

# [2] extract time
time = cdf_data['Epoch']
#
# # [3] build the DCM matrices from a11..a33
a11 = np.array(cdf_data['a11'])
a12 = np.array(cdf_data['a12'])
a13 = np.array(cdf_data['a13'])
a21 = np.array(cdf_data['a21'])
a22 = np.array(cdf_data['a22'])
a23 = np.array(cdf_data['a23'])
a31 = np.array(cdf_data['a31'])
a32 = np.array(cdf_data['a32'])
a33 = np.array(cdf_data['a33'])
print(np.array)
#
# # stack into shape (N, 3, 3)
# dcm = np.array([
#     [a11, a12, a13],
#     [a21, a22, a23],
#     [a31, a32, a33]
# ])  # shape will be (3, 3, N)
#
# # move axes to (N, 3, 3)
# dcm = np.moveaxis(dcm, -1, 0)
#
# # [4] build dictionary like your style
# example_attrs = {'LABLAXIS': None,
#                  'DEPEND_0': None,
#                  'UNITS': None}
#
# data_dict_output = {
#     'time': [[], {}],
#     'dcm':  [[], {}]
# }
#
# # fill in data
# data_dict_output['time'][0] = np.array(time)  # keep it as numpy array
# data_dict_output['time'][1] = deepcopy(example_attrs)
# data_dict_output['time'][1]['UNITS'] = 'ms'  # adjust if needed
# data_dict_output['time'][1]['LABLAXIS'] = 'Time'
#
# data_dict_output['dcm'][0] = dcm
# data_dict_output['dcm'][1] = deepcopy(example_attrs)
# data_dict_output['dcm'][1]['UNITS'] = 'unitless'
# data_dict_output['dcm'][1]['DEPEND_0'] = 'time'
# data_dict_output['dcm'][1]['LABLAXIS'] = 'Direction Cosine Matrix'
#
# # [5] print test
# print("First time entry:", data_dict_output['time'][0][0])
# print("First DCM matrix:\n", data_dict_output['dcm'][0][0])
