#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy



x = np.linspace(-1,3,30)#points on the x axis
xi = np.linspace(-1,3,300)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('tri.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def tricdf(t):
	if t <= 0:
		return 0
	elif t<=1:
		return (t**2)/2
	elif t<=2:
		return ((2*t)-((t**2)/2)-1)
	else:
		return 1

cdf_graph = scipy.vectorize(tricdf,otypes=[float])
the_cdf = []

for i in xi:
	the_cdf.append(cdf_graph(i))

plt.plot(x,err,'o')	
plt.plot(xi, the_cdf)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(['Theoretical', 'Empirical'])

plt.savefig('fig/tri_cdf.png')

plt.show() #opening the plot window
