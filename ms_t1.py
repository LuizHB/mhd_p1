#! /usr/bin/env python

import sys
import pylab as py
import numpy as np



def f(x, a, sd):
    ld = 6.93
    return x ** 6 * np.exp(ld / x) * np.exp(a ** 2 * 0.5 * 0.000145 * (x ** 2 - 1 / x)) - sd * a * np.exp(6.93)

def bissection(a, sd=4.):
    x0 = 1.0
    x1 = 10.0

    for i in range(100):
        xx = (x0 + x1) / 2.
        zz = f(xx, a, sd)
        val = xx - zz
        if np.abs(val) / xx < 1e-5:
            return xx
        elif val < 0:
            x1 = xx
        else:
            x0 = xx


def main(argv):
    avc = np.linspace(1,80,80)
    rr = np.zeros_like(avc)
    vsd = np.arange(4,104,4)

    for itr, sd in enumerate(vsd):
       # print 'sd = %f' % sd  (funcao para checar os numeros escolhidos na lista)
        for i, a in enumerate(avc):
            rr[i] = bissection(a,sd)

        if itr == 0:
            py.plot(avc, rr,'b-')
        elif itr == len(vsd)-1:
            py.plot(avc, rr,'g-')
        else:
            py.plot(avc, rr,'r:')

    py.show()


if __name__ == "__main__":
    main(sys.argv[1:])

