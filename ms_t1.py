#! /usr/bin/env python

import math

def funcao(x):
    return math.pow(x,6)*math.exp(6.93/x)*math.exp(math.pow(a,2)*0.5*0.000145*(math.pow(x,2)-1/x))-4*a*math.exp(6.93)

def derivadafuncao(x):
    return math.pow(x,6)*math.exp(0.0000725*math.pow(a,2)*(math.pow(x,2)-1/x) + 6.93/x)*(0.0000725*math.pow(a,2)*(1/math.pow(x,2)+2*x) -6.93/math.pow(x,2)) + 6*math.pow(x,5)*math.exp(0.0000725*math.pow(a,2)*(math.pow(x,2)-1/x) + 6.93/x)

a = int(0)

x = float(input("Valor de x"))
cont = 0

while(x != cont and a <81):
    cont = x
    x = x - funcao(x)/ derivadafuncao(x)
    e = abs((x-cont)/x)
    x = x + e
    print ("x" + str(a) + " = " + str (x) +"\n")
    a = a+1

if (a==81):
    print("\n\n Nao converge")
else:
    print("\n\n Valor de x: " + str(x))