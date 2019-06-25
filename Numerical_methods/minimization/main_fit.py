import numpy as np
from math import *
from vector_codes import *
from matrix_codes import *
from minimize import *


def master_func(p, t, y, sigma):

    z = vector(1)
    for ii in range(len(t)):
        
        z[0] += (function(p, t[ii])[0] - y[ii])**2/(sigma[ii])**2

    return z

def df_master_func(p, t, y, sigma):

    A = p[0]
    T = p[1]
    B = p[2]

    z = vector(p.size)

    for ii in range(len(t)):
        z[0] += 2*(function(p, t[ii])[0]-y[ii])/(sigma[ii])**2 * exp(-t[ii]/T)
        z[1] += 2*(function(p, t[ii])[0]-y[ii])/(sigma[ii])**2 * A*t[ii]/(T**2) * exp(-t[ii]/T)
        z[2] += 2*(function(p, t[ii])[0]-y[ii])/(sigma[ii])**2
    return z


def function(p, t):

    A = p[0]
    T = p[1]
    B = p[2]

    z = vector(1)
    z[0] = A*exp(-t/T)+B
    return z

data = np.loadtxt('data.dat')
t = data[:,0]
y = data[:,1]
sigma = data[:,2]


x0 = vector(3)
x0[0] = 1
x0[1] = 1
x0[2] = 1

f = lambda p: master_func(p, t, y, sigma)
df = lambda p: df_master_func(p, t, y, sigma)
delta_x = quasi_newton_analytic(f, df, x0, 1e-6)

t_lin = np.linspace(t[0], t[-1], 1000)
y_exp = np.zeros(len(t_lin))


for ii in range(len(t_lin)):

    y_exp[ii] = delta_x[0] * exp(-t_lin[ii]/delta_x[1]) + delta_x[2]


np.savetxt("fitting_params.dat", list(zip(t_lin, y_exp)))

print("\n\nFitting problem:")
print("The obtained parameters are: A = %.3f, T = %.3f, B = %.3f" %(delta_x[0], delta_x[1], delta_x[2]))
