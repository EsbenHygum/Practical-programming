import numpy as np
from math import *
from vector_codes import *
from matrix_codes import *
from least_square import *


data = np.loadtxt('data.txt')


xlist = data[:,0]
ylist = data[:,1]
dylist = data[:,2]

x = vector(len(xlist))
y = vector(len(ylist))
dy = vector(len(dylist))

for ii in range(len(xlist)):
    x[ii] = xlist[ii]
    y[ii] = ylist[ii]
    dy[ii] = dylist[ii]


def log_func(x): return log(x)
def const_func(x): return 1
def lin_func(x): return x

f = [log_func, const_func, lin_func]

c, dc, cov_matrix = ls_func(x, y, dy, f)
x_range = np.linspace(0.1, 9.9, 1000)
y_exp = np.zeros(len(x_range))

for ii in range(len(y_exp)):
    y_exp[ii] = c[0]*f[0](x_range[ii]) + c[1]*f[1](x_range[ii]) + c[2]*f[2](x_range[ii])

np.savetxt('data_exp.txt', list(zip(x_range, y_exp)))

print("c vector:")
vector.printing(c)

print("Error estimate of c:")
vector.printing(dc)

print("Covariance matrix:")
matrix.printing(cov_matrix)
