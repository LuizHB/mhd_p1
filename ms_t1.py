#! /usr/bin/env python

import sys
import pylab as py
import numpy as np
from scipy import optimize


def f(x,a):

	ld = 6.93
        return x**6*np.exp(ld/x)*np.exp(a**2*0.5*0.000145*(x**2-1/x))-4*a*np.exp(6.93)

def f_prime(x,a):
	return np.pow(x,6)*np.exp(0.0000725*np.pow(a,2)*(np.pow(x,2)-1/x) + 6.93/x)*(0.0000725*np.pow(a,2)*(1/np.pow(x,2)+2*x) -6.93/np.pow(x,2)) + 6*np.pow(x,5)*np.exp(0.0000725*np.pow(a,2)*(np.pow(x,2)-1/x) + 6.93/x)



def newt(x,n,a):
	for i in range(n):
		if f_prime(x, a) == 0:
			return x
		x = x - f(x, a)/f_prime(x,a)
	return x

def bissection(n,a):

        x0 = 1.0
        x1 = 5.0

        for i in range(100):
                xx = (x0+x1)/2.
                zz = f(xx,a)
                # print xx,zz,x0,x1
                val = xx - zz #f(x,a)
                if np.abs(val)/xx < 1e-5:
                        return xx
                elif val < 0:
                        x1 = xx
                else:
                        x0 = xx

def main(argv):
	if (len(sys.argv) != 3):
		sys.exit('Usage: newtons_method.py <x> <n>')
	#a =0
        avc = np.linspace(1,80,100) #np.array([1, 2, 3, 5, 7, 10, 20, 30, 60, 80])
        rr = np.zeros_like(avc)
	for i,a in enumerate(avc):
                #a +=1
		# print 'The root is: '
		#print a, newt(float(sys.argv[1]),int(sys.argv[2]), a), bissection(int(sys.argv[2]), a)
                rr[i] = bissection(int(sys.argv[2]), a)
        py.plot(avc,rr)
        py.show()



if __name__ == "__main__":
	main(sys.argv[1:])