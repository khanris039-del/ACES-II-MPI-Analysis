import spaceToolsLib
import spaceToolsLib as stl
from glob import glob
import matplotlib.pyplot as plt
from pyarrow import dictionary
from pyarrow.dataset import dataset

#spacetoolslib as physics related variables


# how to open cdf files
folderNames = ["Current" , "Density"]
folderPath = r"C:\Users\riskh\OneDrive - University of Iowa\OCHRE_research\ACESII_Langmuir"
wVar = 1 #which physical variable
wFile = 1 #which file in the folder

# open cdf file using space tools lib 'inputcdf
filePath = glob(folderPath + rf'\{folderNames[wVar]}\*') #returns a list of strings containing the absolute paths of the files
myDataFile = filePath[wFile]

data_dict = stl.loadDictFromFile(inputFilePath=myDataFile)  #uses space tools lib to read a cdf file and output a data dictionary


# NOTES ON DATA.DICT
# description: the stl.loaddictfromfile command outputs a python dictionary with the folloing format:
data_dict = {
              'key1':[DATA], {DATA attributes dictionary}],
              'key2':[DATA], {DATA attributes dictionary}],
               (etc..)
                }

key1 - the name of the first key/variable in the data_dict dictionary
DATA1 - The actual dataset
DATA1 attributes dictionary - python dictionary of attributes associated with DATA 1.
#
# EXAMPLE USAGE 1: print all the keys in the data dictionary
for key in data_dict.keys():
    print(key)
#
#
#
print all the keys in the data dictionary
for key in data_dict.keys():
    print(key)

# EXAMPLE USAGE 2: access plasma density and plot it vs time

density = data_dict['ni'][0]
epoch = data_dict['Epoch'][0]
#

fig, ax = plt.subplots()
ax.plot(epoch, density)
plt.show()
#
#
#
# SAMPLE USAGE 3: write out your own data file

outputDataPath = r"C:\Users\riskh\OneDrive - University of Iowa\OCHRE_research\ACESII_Langmuir\testFile.cdf"
fakeData1 = [1,2,3]
fakeData2 = [4,5,6]
outputData = {'key1':[fakeData1, {}],
              'key2':[fakeData2, {}]
              }

spaceToolsLib.outputCDFdata(outputPath=outputDataPath,data_dict=outputData)
#
#