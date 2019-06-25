import numpy as np
from vector_codes import *
from matrix_codes import *
from minimize import *
from root_find import *

calls = 0

def rosen(p):

    global calls
    calls += 1

    x = p[0]
    y = p[1]
    z = vector(1)
    z[0] = (1-x)**2 + 100*(y-x*x)**2

    return z

def df_rosen(p):
    
    global calls
    calls += 1
    x = p[0]
    y = p[1]

    z = vector(2)

    z[0] = -2*(1-x)-400*x*(y-x*x)
    z[1] = 200*(y-x*x)

    return z

def dfH_rosen(p):

    global calls
    calls += 1
    x = p[0]
    y = p[1]

    H = matrix(2,2)
    H[0,0] = 2-400*y+1200*x*x
    H[1,0] = -400*x
    H[0,1] = -400*x
    H[1,1] = 200

    return H

def himmelblau(p):
    
    global calls
    calls += 1

    x = p[0]
    y = p[1]

    z = vector(1)

    z[0] = (x*x+y-11)**2 + (x+y*y-7)**2

    return z

def df_himmelblau(p):
    
    global calls
    calls += 1

    x = p[0]
    y = p[1]
    z = vector(2)

    z[0] = 4*x*(x*x+y-11) + 2*(x+y*y-7)
    z[1] = 2*(x*x+y-11) + 4*y*(x+y*y-7)

    return z


def dfH_himmelblau(p):
    
    global calls
    calls += 1
    x = p[0]
    y = p[1]

    H = matrix(2,2)

    H[0,0] = 12*x*x + 4*y - 42
    H[0,1] = 4*x + 4*y
    H[1,0] = 4*x + 4*y
    H[1,1] = 4*x + 12*y*y - 26

    return H



x0 = vector(2)
x0[0] = 2
x0[1] = 1


print("Testing minimization methods on Rosenbrock's function:")
x = newton(rosen, df_rosen, dfH_rosen, x0, 1e-6)
print("Using Newton's method yields a minimum at [%.2f;%.2f] with %d steps" %(x[0], x[1], calls))
calls = 0
x = quasi_newton_analytic(rosen, df_rosen, x0, 1e-6)
print("Using the quasi Newton analytical method yields a minimum at [%.2f;%.2f] with %d steps" %(x[0], x[1], calls))
calls = 0
delta_x = rf_analytic(df_rosen, x0, dfH_rosen, 1e-6)
print("The analytic root-finding function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
print("The initial guess was [%.2f;%.2f]" %(x0[0], x0[1]))

calls = 0
print("\n\nTesting minimization methods on Himmelblau's function:")
x = newton(himmelblau, df_himmelblau, dfH_himmelblau, x0, 1e-6)
print("Using Newton's method yields a minimum at [%.2f;%.2f] with %d steps" %(x[0], x[1], calls))
calls = 0
x = quasi_newton_analytic(himmelblau, df_himmelblau, x0, 1e-6)
print("Using the quasi Newton analytical method yields a minimum at [%.2f;%.2f] with %d steps" %(x[0], x[1], calls))
calls = 0
delta_x = rf_analytic(df_himmelblau, x0, dfH_himmelblau, 1e-6)
print("The analytic root-finding function yields a minimum at [%.2f;%.2f] with %d steps" %(delta_x[0], delta_x[1], calls))
print("The initial guess was [%.2f;%.2f]" %(x0[0], x0[1]))


