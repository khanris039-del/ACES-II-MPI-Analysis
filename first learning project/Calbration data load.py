#IMPORTS
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from glob import glob

#TOGGLES
wFile = 0
wKey = 1
wwKey = 2

#---PROGRAM START---


#path to folder
folderPath = r'C:\Users\riskh\sweptLP_calFiles_ACESII\*'
myfiles = glob(folderPath)

#load data
df = pd.read_csv(myfiles[wFile])
#print(df)
dictKeys = df.keys()

# extract time data
timedata = df[dictKeys[0]]
print(timedata)

# PLOT THE DATA


fig, ax = plt.subplots(2, 1)
#1st lot
ax[0].plot(timedata, df[dictKeys[wKey]], color = 'crimson', label = 'bla bla bla')
ax[0].set_title(f'{dictKeys[wKey]} vs. {dictKeys[0]}')
ax[0].set_ylabel(f'{dictKeys[wKey]}')
ax[0].set_xlabel(f'{dictKeys[0]}')
ax[0].legend(loc='upper right')
#2nd plot
ax[1].plot(timedata, df[dictKeys[wwKey]], color = 'blue', label = 'bla bla bla')
ax[1].set_title(f'{dictKeys[wwKey]} vs. {dictKeys[0]}')
ax[1].set_ylabel(f'{dictKeys[wwKey]}')
ax[1].set_xlabel(f'{dictKeys[0]}')
ax[1].legend(loc='upper right')

fig.set_figwidth(10)
plt.savefig('my_figure.png')
plt.tight_layout()
plt.show()





