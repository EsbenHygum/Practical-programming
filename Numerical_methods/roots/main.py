import numpy as np
from matrix_codes import *
from vector_codes import *
from root_find import *
from math import *
from scipy.optimize import root

calls = 0

def sys_eq(p, arrays = False):
    
    global calls
    calls += 1

    x = p[0]
    y = p[1]

    z = vector(2)
    z[0] = 1e4*x*y-1
    z[1] = exp(-x)+exp(-y)-1-1e-4

    if arrays:
        return np.array([z[0], z[1]])
    else:
        return z

def df_sys_eq(p):
   
    global calls
    calls += 1
    x = p[0]
    y = p[1]


    J = matrix(2,2)
    J[0,0] = 1e4*y
    J[0,1] = 1e4*x
    J[1,0] = (-1)*exp(-x)
    J[1,1] = (-1)*exp(-y)

    return J

def rosen(p, arrays = False):

    global calls
    calls += 1
    x = p[0]
    y = p[1]

    z = vector(2)

    z[0] = -2*(1-x)-400*x*(y-x*x)
    z[1] = 200*(y-x*x);
    
    if arrays:
        return np.array([z[0], z[1]])
    else:
        return z

def df_rosen(p):
    
    global calls
    calls += 1
    x = p[0]
    y = p[1]

    J = matrix(2,2)
    J[0,0] = 2-400*x+1200*x*x
    J[1,0] = -400*x
    J[0,1] = -400*x
    J[1,1] = 200

    return J


def himmelblau(p, arrays = False):
    
    global calls
    calls += 1

    x = p[0]
    y = p[1]

    z = vector(2)

    z[0] = 4*x*(x*x+y-11) + 2*(x+y*y-7)
    z[1] = 2*(x*x+y-11) + 4*y*(x+y*y-7)
    
    if arrays:
        return np.array([z[0], z[1]])
    else:
        return z


def df_himmelblau(p):
    
    global calls
    calls += 1
    x = p[0]
    y = p[1]

    J = matrix(2,2)

    J[0,0] = 12*x*x + 4*y - 42
    J[0,1] = 4*x + 4*y
    J[1,0] = 4*x + 4*y
    J[1,1] = 4*x + 12*y*y - 26

    return J


x0 = vector(2)
x0[0] = 2
x0[1] = 1

x0_list = [2,1]

print("Testing solutions to system of equations:")
delta_x, iterations = rf_analytic(sys_eq, x0, df_sys_eq, 1e-6)
print("The analytic function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
calls = 0
delta_x, iterations = rf_numeric(sys_eq, x0, 1e-6, 1e-6)
print("The numeric function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
calls = 0
res = root(sys_eq, x0_list, args = (True), tol = 1e-6)
print("Scipy.optimize.root yields a minimum at", res.x,"with %d steps" %(calls))
print("The starting point was chosen as [%.2f;%.2f]" %(x0[0], x0[1]))


calls = 0
print("\nTesting solutions to Rosenbrock's valley function:")
delta_x, iterations = rf_analytic(rosen, x0, df_rosen, 1e-6)
print("The analytic function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
calls = 0
delta_x, iterations = rf_numeric(rosen, x0, 1e-6, 1e-6)
print("The numeric function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
calls = 0
res = root(rosen, x0_list, args = (True), tol = 1e-6)
print("Scipy.optimize.root yields a minimum at", res.x,"with %d steps" %(calls))
print("The starting point was chosen as [%.2f;%.2f]" %(x0[0], x0[1]))


x0[0] = 4
x0[1] = 5
x0_list = [4, 5]

calls = 0
print("\nTesting solutions to Himmelblau's function:")
delta_x, iterations = rf_analytic(himmelblau, x0, df_himmelblau, 1e-6)
print("The analytic function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
calls = 0
delta_x, iterations = rf_numeric(himmelblau, x0, 1e-6, 1e-6)
print("The numeric function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
calls = 0
res = root(himmelblau, x0_list, args = (True), tol = 1e-6)
print("Scipy.optimize.root yields a minimum at", res.x,"with %d steps" %(calls))
print("The starting point was chosen as [%.2f;%.2f]" %(x0[0], x0[1]))

