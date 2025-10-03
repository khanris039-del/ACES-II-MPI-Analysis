import spaceToolsLib as stl
from glob import glob
import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.602e-19  # Coulombs (C)
pi = np.pi  # Pi
m_p = 1.67e-27  # Mass of proton in kg

# path to the CDF file
folderNames = ["Current", "Density"]
folderPath = r"C:\Users\riskh\OneDrive - University of Iowa\OCHRE_research\ACESII_Langmuir"
wVar = 0  #  variable (0 for Current)
wFile = 1  # file within the folder


# file path for the CDF file
filePath = glob(folderPath + rf'\{folderNames[wVar]}\*')
myDataFile = filePath[wFile]

# Load the CDF file using spaceToolsLib
data_dict = stl.loadDictFromFile(inputFilePath=myDataFile)
wVar = 0  #  variable (0 for Current)
wFile = 1  # file within the folder
filePath = glob(folderPath + rf'\{folderNames[wVar]}\*')
myDataFile = filePath[wFile]
epoch = data_dict['fixed_Epoch'][0]




# Access variables from data dictionary
I_c = data_dict['fixed_current'][0]  # Ion current data
A = 20 * 1e-4  # Probe area in square meters (m²)? just googled a random probe
T_i = 1160.87  # Ion temperature in Kelvin (K), also don't know for sure just used rando

# Calculate ion density
n_i = (I_c / (A * q * np.sqrt(T_i / (2 * pi * m_p)))) * 1e-6



# Check if n_i is an array or a single value, and print accordingly
# if isinstance(n_i, np.ndarray):
#     # Handle array case: print each value
#     for density in n_i:
#         #print(f"Ion density: {density:.3e} ions/m³")
# else:
#     # Single value: print directly
    #print(f"Ion density: {n_i:.3e} ions/m³")



fig, ax = plt.subplots(1, 1, figsize=(10, 6))
plt.yscale('log')
ax.plot(epoch, n_i)

plt.show()
