import numpy as np
from matrix_codes import *
from vector_codes import *
from root_find import *
from math import *

def sys_eq(p):

    x = p[0]
    y = p[1]

    z = vector(2)
    z[0] = 1e4*x*y-1
    z[1] = exp(-x)+exp(-y)-1-1e-4

    return z


def df_sys_eq(p):
    
    x = p[0]
    y = p[1]


    J = matrix(2,2)
    J[0,0] = 1e4*y
    J[0,1] = 1e4*x
    J[1,0] = (-1)*exp(-x)
    J[1,1] = (-1)*exp(-y)

    return J

def rosen(p):

    x = p[0]
    y = p[1]

    z = vector(2)

    z[0] = -2*(1-x)-400*x*(y-x*x)
    z[1] = 200*(y-x*x);
    
    return z

def df_rosen(p):
    
    x = p[0]
    y = p[1]

    J = matrix(2,2)
    J[0,0] = 2-400*x+1200*x*x
    J[1,0] = -400*x
    J[0,1] = -400*x
    J[1,1] = 200

    return J

x0 = vector(2)
x0[0] = 2.0
x0[1] = 1.0

delta_x, iterations = rf_analytic(rosen, x0, df_rosen, 1e-6)

vector.printing(delta_x)
print(iterations)
