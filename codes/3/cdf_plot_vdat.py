 #Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

x1 = np.linspace(-4,4,300)
x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
the_cdf = []
randvar = np.loadtxt('vdat.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def exxp(x):
	return (1-np.exp(-0.5 *	x))

cdf_graph = scipy.vectorize(exxp)

def nfunc(x):
	if x<0:
		return 0
	else:
		return (cdf_graph(x))


for i in x1:
    the_cdf.append(nfunc(i))

plt.plot(x,err,'o')	
plt.plot(x1, the_cdf)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical", "Theory"])

plt.savefig('fig/vdat_cdf.png')
plt.show() #opening the plot window

