import numpy as np
import sys
from math import *
sys.setrecursionlimit(10000)

def adaptor(f, a: float, b: float, acc: float, eps: float, f2: float, f3: float, recursion: int):    

    f1 = f(a + 1.*(b-a)/6.)
    f4 = f(a + 5.*(b-a)/6.)

    Q = (b-a)*(2*f1 + 1*f2 + 1*f3 + 2*f4)/6.
    q = (b-a)*(f1 + f2 + f3 + f4)/4.

    dQ = abs(Q-q)

    if dQ < acc + eps*abs(Q):
        return Q
    else:
        Q_low = adaptor(f, a, (a+b)/2., acc/sqrt(2), eps, f1, f2, recursion+1)
        Q_high = adaptor(f, (a+b)/2., b, acc/sqrt(2), eps, f3, f4, recursion+1)
        return Q_low + Q_high

def integrator(f, a: float, b: float, acc: float, eps: float):
    f2 = f(a + 2.*(b-a)/6.)
    f3 = f(a + 4.*(b-a)/6.)

    recursion = 0
    return adaptor(f, a, b, acc, eps, f2, f3, recursion)



def clenshaw_curtis(f, a: float, b: float, acc: float, eps: float):
    
    g = lambda theta: f((b-a)/2*cos(theta)+(a+b)/2)*sin(theta)*(b-a)/2 #Rescaling with Gauss-Legendre
    return integrator(g, 0, pi, acc, eps)

