
# imports
from glob import glob
import io
import numpy as np
import spaceToolsLib as stl
from copy import deepcopy


# get all text files
path_to_folder = r'C:\Users\riskh\OneDrive - University of Iowa\ACESII-MPI Project'
text_file_paths = glob(path_to_folder+'\\*.txt*')



# Load JUST ONE .txt file
file = text_file_paths[1] # note: index 1 is the data description
temp_data = []

with io.open(file, mode="r", encoding="utf-8") as f:

    next(f) # this skips the first line in the .txt file
    for line in f:
        temp_data.append([float(val) for val in line.split()])

temp_data = np.array(temp_data).T

data = np.array(temp_data)
var1 = data[0]
print(var1)

example_attrs = {'LABLAXIS': None,
                 'DEPEND_0': None,
                 'UNITS': None}

data_dict_output = {
    'arissa': [[], {}],
    'khan': [[], {}]
}

# [2] fill in the attributes of your data_dict_output
data_dict_output['arissa'][1] = deepcopy(example_attrs)
data_dict_output['khan'][1] = deepcopy(example_attrs)

# actually update your attributes
data_dict_output['arissa'][1]['UNITS'] = 'm'
data_dict_output['arissa'][1]['LABLAXIS'] = 'Human?'

data_dict_output['khan'][1]['UNITS'] = 'feet'
data_dict_output['khan'][1]['DEPEND_0'] = 'arissa'

# fill in some test data
data_dict_output['arissa'][0] = np.array([var1]) #data MUST be numpy arrays when outputting a .cdf

# [3] actually outputting the data
file_out_path = r'C:\Users\riskh\OneDrive\New folder\MPI-1.cdf'
stl.outputCDFdata(outputPath=file_out_path, data_dict=data_dict_output)