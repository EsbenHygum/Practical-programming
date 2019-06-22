import numpy as np
import math
from scipy.interpolate import interp1d
from scipy.integrate import quad

def qspline(x: list, y: list):
    
    n = len(x)
    length = n - 1
    p = np.zeros(length)
    c = np.zeros(length)

    for ii in range(len(p)):
        p[ii] = (y[ii+1] - y[ii])/(x[ii+1] - x[ii])

    for ii in range(len(c) - 1):
        c[ii+1] = (p[ii+1] - p[ii] - c[ii]*(x[ii+1] - x[ii]))/(x[ii+2] - x[ii+1])

    c[len(c) - 1] /= 2

    for ii in reversed(range(len(c) - 1)):
        c[ii] = (p[ii+1] - p[ii] - c[ii+1]*(x[ii+2]-x[ii+1]))/(x[ii+1]-x[ii])


    return p, c

def bin_search(x: list, y: list, z: float):
    
    n = len(x)
    assert n > 1 and z >= x[0] and z < x[-1]

    i = 0
    j = n - 1

    p, c = qspline(x, y)

    while j-i > 1:
        mid = math.floor((i + j)/2.)

        if z >= x[mid]:
            i = mid

        else:
            j = mid
 
    f_z = y[i]+(p[i]-c[i]*(x[i+1]-x[i]))*(z-x[i]) + c[i]*(z-x[i])**2

    return f_z, i
    

def quad_diff(x: list, y: list, z: float):

    i = bin_search(x, y, z)[1]
    p, c = qspline(x, y)

    diff = p[i] - c[i]*(x[i]+x[i+1]-2*z)

    return diff


def quad_integ(x: list, y: list, z: float):

    
    p, c = qspline(x,y)
    
    my_integ = 0
    sc_integ = 0

    for ii in range(len(x)):

        if z == x[0]:
            return my_integ, sc_integ

        elif x[ii+1] >= z:

            b = p[ii] - c[ii]*(z-x[ii])
            a = y[ii] - c[ii]*x[ii]**2 - b*x[ii]

            my_integ += integrand(c[ii], b, a, z) - integrand(c[ii], b, a, x[ii])
            sc_integ += quad(sc_integrand, x[ii], z, args = (c[ii], b, a))[0]

            return my_integ, sc_integ

        else: 

            b = p[ii] - c[ii]*(x[ii+1]-x[ii])
            a = y[ii] - c[ii]*x[ii]**2 - b*x[ii]

            my_integ += integrand(c[ii], b, a, x[ii+1]) - integrand(c[ii], b, a, x[ii])
            sc_integ += quad(sc_integrand, x[ii], x[ii+1], args = (c[ii], b, a))[0]
            

def integrand(c, b, a, x):
    return c/3*x**3+b/2*x**2+a*x
    
def sc_integrand(x, c, b, a):
    return c*x**2 + b*x + a


x = np.arange(-5, 6, 0.1) 
def fun_to_fit(x) : return np.sinc(x)
y = [ fun_to_fit(xi) for xi in x ]
z = np.arange(-5, 5.9, 0.01)



interp = interp1d(x, y, 'quadratic')

for ii in range(len(z)):
    
    print(z[ii], bin_search(x, y, z[ii])[0], interp(z[ii]), quad_diff(x, y, z[ii]), quad_integ(x, y, z[ii])[0], quad_integ(x, y, z[ii])[1])


print('\n')

dy = np.zeros(len(z))
for ii in range(len(z)):
    dy[ii] = bin_search(x, y, z[ii])[0]


dydx = np.diff(dy)/np.diff(z)

for ii in range(len(z)-1):
    print(z[ii+1], dydx[ii])


