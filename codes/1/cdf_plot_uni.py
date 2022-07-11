#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if



x = np.linspace(-4,4,30)#points on the x axis
xi = np.linspace(-4,4,300)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def give_line(x):
	#for i in x:
	if i < 0:
		return 0
	elif i<=1:
		return i
	else:
		return 1

l_er = []

for i in xi:
	l_er.append(give_line(i))

plt.plot(x,err,'o')	
plt.plot(xi, l_er)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(['Theoretical', 'Empirical'])

#if using termux
plt.savefig('fig/uni_cdf.png')
#plt.savefig('fig/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('fig/gauss_cdf.pdf')
#plt.savefig('fig/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
