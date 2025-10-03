# IMPORTS

import spaceToolsLib
import spaceToolsLib as stl
from glob import glob
import matplotlib.pyplot as plt
from pyarrow import dictionary
from pyarrow.dataset import dataset

#spacetoolslib as physics related variables


# open cdf files
folderNames = ["Current" , "Density"]
folderPath = r"C:\Users\riskh\OneDrive - University of Iowa\OCHRE_research\ACESII_Langmuir"
wVar = 1 #which physical variable
wFile = 0 #which file in the folder

# open cdf file using space tools lib 'inputcdf
filePath = glob(folderPath + rf'\{folderNames[wVar]}\*') #returns a list of strings containing the absolute paths of the files
myDataFile = filePath[wFile]

data_dict = stl.loadDictFromFile(inputFilePath=myDataFile)  #uses space tools lib to read a cdf file and output a data dictionary

# PLOT?



# EXAMPLE USAGE 2: access plasma density and plot it vs time

density = data_dict['ni'][0]
epoch = data_dict['Epoch'][0]


fig, ax = plt.subplots(1,1)
ax.plot(epoch, density)
plt.show()