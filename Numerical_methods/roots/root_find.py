import numpy as np
from vector_codes import *
from matrix_codes import *
from qr_decomp import *

def rf_analytic(f, x0: vector, jacobian, eps: float, iteration = 0):
    x = vector.copy(x0)
    minus_f_x = vector(x.size)

    f_x = f(x)

    while vector.norm(f_x) > eps:
        J = jacobian(x) 
        for jj in range(minus_f_x.size):
            minus_f_x[jj] = -1*f_x[jj]

        delta_x = qr_gs_solve(J, minus_f_x)
        lamb = 2
        while True:
            
            lamb /= 2
            iteration += 1
            for jj in range(x.size):
                x[jj] = x[jj] + lamb*delta_x[jj]

            f_x2 = f(x)
            
            if vector.norm(f_x2) < (1-lamb/2)*vector.norm(f_x) or lamb < 0.02: break
        f_x = f_x2

    return x, iteration



def rf_numeric(f, x0: vector, eps: float, dx: float, iteration = 0):
    
    x = vector.copy(x0)
    df = vector(x.size)
    J = matrix(x.size, x.size)
    minus_f_x = vector(x.size)
    f_x = f(x)

    while vector.norm(f_x) > eps: 
        f_x = f(x)
        for ii in range(x.size):
            x[ii] += dx
            
            for jj in range(df.size):
                df[jj] = f(x)[jj] - f_x[jj]
                J[jj, ii] = df[jj]/dx

            x[ii] -= dx

        for ll in range(minus_f_x.size):
            minus_f_x[ll] = -1*f_x[ll]
       
        delta_x = qr_gs_solve(J, minus_f_x)
        lamb = 2

        while True:
            
            lamb /= 2
            iteration += 1
            for jj in range(x.size):
                x[jj] = x[jj] + lamb*delta_x[jj]
            
            f_x2 = f(x)
            if vector.norm(f_x2) < (1-lamb/2)*vector.norm(f_x) or lamb < 0.02: break

        if vector.norm(delta_x) < dx: break
        

    return x, iteration


