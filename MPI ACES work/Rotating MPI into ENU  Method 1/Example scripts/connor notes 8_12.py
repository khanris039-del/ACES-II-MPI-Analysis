

# # how to use spacetoolslib to read cdf files
#
# # imports
# import spaceToolsLib as stl
#
# #path to a cdf file
# path = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project\ACESII_36364_l3_MPI_ENU.cdf'
#
# #use stl to load a python dictionry of all the data
# data_dict = stl.loadDictFromFile(path)
#
#
# # [1] how all keys of a python dictionary
# key_names = data_dict.keys
# print(key_names)
#
# # [2] get a particular data set
# data1 = data_dict['MPI1_Epoch'][0]
# print(data1)
#
# # [3] get the attributes of a particular dataset
# attr1 = data_dict['MPI1_Epoch'][1]
# print(attr1)
#
# # [4] USE THE DEEPCOPY FUNCTION
# from copy import deepcopy
#
# var1 = deepcopy(data_dict['MPI1_Epoch'][0])
# var2 = 5*deepcopy(var1)
# print(var1[0][0][0])
# print(var2[0][0][0])
#




# LOADING TEXT FILES
# get all the text files

from glob import glob
import io
import numpy as np
from copy import deepcopy

path_to_folder = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project'
text_file_paths = glob(path_to_folder+'\\*.txt*')
# print(text_file_paths)
#
# for path in text_file_paths:
#     print(path)

# Load JUST ONE .txt data

file = text_file_paths[1]
temp_data = []

with io.open(file, mode="r", encoding="utf=8") as f:
    next(f) #skips first line in .txt fiel

    for line in f:
        temp_arr_str = line.split()
        temp_arr_float = [float(val) for val in temp_arr_str]
        temp_data.append(temp_arr_float)

    data = np.array(temp_data)
    var1 = data[:,0]
    var2 = data[:,1]
    var3 = data[:,2]


## CREATING MY OWN CDF FILE

#[1] defining  data_dict_output format

example_attrs
data_dict_output = {
    'arissa' : [[],{}]
    'khan' : [[],{}]
}

data_dict_output['']



