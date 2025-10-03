# imports
import numpy as np
import scipy
import matplotlib.pyplot as plt

# TOGGLES
PlotFakeData = True


N = 25 #number of points
xData = np.linspace(1, 100, N)

np.random.seed(105)
yData = np.array([val + 100*np.random.rand(1)*sum(np.random.rand(5)) for val in xData]).transpose()[0]

if PlotFakeData:
    fig, ax = plt.subplots()
    ax.scatter(xData, yData)
    plt.show()


#CURVE FITTING FUCNTION
def LinearFunc(x, m, b):
    y = m*x + b
    return y

# use function with scipy.optimize.curve_fit to fit the data
params,cov = scipy.optimize.curve_fit(f = LinearFunc, xdata=xData, ydata=yData)

print(params)

#create the fited data line

yData_fit = LinearFunc(xData,*params)

if PlotFakeData:
    fig, ax = plt.subplots()
    ax.scatter(xData, yData)
    ax.plot(xData,yData_fit,color='red')
    plt.show()
