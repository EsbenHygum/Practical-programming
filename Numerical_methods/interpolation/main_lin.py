import numpy as np
from scipy.integrate import quad
import math

def lin_interp(x: list, y: list, z: float):
    n = len(x)
    assert n > 1 and z >= x[0] and z <= x[n-1]
    i = 0
    j = n - 1

    while j-i > 1:
        mid = int((i + j)/2)
        if z > x[mid]:
            i = mid
        else:
            j = mid
    return y[i] + (y[i + 1] - y[i])/(x[i + 1] - x[i]) * (z - x[i])


def lin_integ(x: list, y: list, z: float):
    
    f_z = lin_interp(x, y, z)
    int_sum = 0
    sc_int_sum = 0

    for ii in range(len(x)):
        if z == x[0]:
            return int_sum, sc_int_sum

        elif x[ii+1] >= z:
            a = (f_z - y[ii])/(z - x[ii])
            b = y[ii] - a*x[ii]
            int_sum += a/2*(z**2-x[ii]**2) + b*(z - x[ii])
            sc_int_sum += quad(integrand, x[ii], z, args = (a, b))[0]
            return int_sum, sc_int_sum

        else:
            a = (y[ii+1] - y[ii])/(x[ii+1] - x[ii])
            b = y[ii] - a*x[ii]
            int_sum += a/2*(x[ii+1]**2 - x[ii]**2)+b*(x[ii+1]-x[ii])
            sc_int_sum += quad(integrand, x[ii], x[ii+1], args = (a, b))[0]


def integrand(x, a, b):
    return a * x + b


x = np.arange(-5, 6, 0.1)#x = np.arange(0, 5, 1, int) 
def fun_to_fit(x) : return np.sinc(x)
y = [ fun_to_fit(xi) for xi in x ]
z = np.arange(x[0], 5, 0.1)#z = np.arange(1, 4, 0.25)


for ii in range(len(z)):
    print(z[ii], lin_interp(x, y, z[ii]), np.interp(z[ii], x, y), lin_integ(x, y, z[ii])[0], lin_integ(x, y, z[ii])[1])

