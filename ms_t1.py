#! /usr/bin/env python

import sys
import pylab as py
import numpy as np
from scipy import optimize
 

def f(x,a):
        sd = 4
	ld = 6.93
        return x**6*np.exp(ld/x)*np.exp(a**2*0.5*0.000145*(x**2-1/x))-sd*a*np.exp(6.93)
	
def f_prime(x,a): #for newton`s method
        return x**6*np.exp(0.0000725*a**2*(x**2-1/x) + 6.93/x)*(0.0000725*a**2*(1/x**2+2*x)-6.93/x**2) + 6*x**5*np.exp(0.0000725*a**2*(x**2-1/x) + 6.93/x)

def newt(x,n,a): # Newton method
	for i in range(n):
		if f_prime(x, a) == 0:
			return x
		x = x - f(x, a)/f_prime(x,a)
	return x

def bissection(n,a):

        x0 = 1.0
        x1 = 10.0

        for i in range(100):
                xx = (x0+x1)/2.
                zz = f(xx,a)
                val = xx - zz 
                if np.abs(val)/xx < 1e-5:
                        return xx
                elif val < 0:
                        x1 = xx
                else:
                        x0 = xx
	
def main(argv):
              
        if (len(sys.argv) != 3):
           	sys.exit('Usage: newtons_method.py <x> <n>')
        avc = np.linspace(1,80,80) 
        rr = np.zeros_like(avc)
        for i,a in enumerate(avc):
            rr[i] = bissection(int(sys.argv[2]), a)                
            py.plot(avc,rr)
            py.show()
#            py.subplot(223)
#        for sd in g[:0]:           
#            py.plot(avc,rr)
#            py.show()
#        py.subplot(222)
#        for sd in g[:1]:           
#            py.plot(avc,rr)
#            py.show()
#        py.subplot(223)
#        for sd in g[:2]:           
#            py.plot(avc,rr)
#            py.show()
#        py.subplot(224)
#        for sd in g[:3]:           
#            py.plot(avc,rr)
#            py.show()
	
	
	

if __name__ == "__main__":
	main(sys.argv[1:])

