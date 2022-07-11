#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=50
xi = np.linspace(-1,3,10*maxrange)
x = np.linspace(-1,3,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 4/(maxrange-1);
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('tri.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def tri_pdf(i):
	#for i in x:
	if i < 0:
		return 0
	elif i<=1:
		return i
	elif i<2:
		return 2-i
	else:
		return 0

theopdf = []

for i in xi:
	theopdf.append(tri_pdf(i))
	
#vec_tri_pdf = scipy.vectorize(tri_pdf)

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(xi, theopdf)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical","Theory"])

plt.savefig('fig/tri_pdf.png')
plt.show() #opening the plot window
