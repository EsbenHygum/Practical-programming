import numpy as np
from matrix_codes import *
from vector_codes import *
from qr_decomp import *

def newton(f, df, hf, x0, eps: float, alpha = 1e-4):

    n = x0.size
    x = vector.copy(x0)
    step = vector(n)
    minus_grad_phi = vector(n)
    grad = df(x)
    
    while vector.dot_prod(grad, grad) > eps:
        H = hf(x)
        for ii in range(minus_grad_phi.size):
            minus_grad_phi[ii] = (-1)*grad[ii]

        delta_x = qr_gs_solve(H, minus_grad_phi)        
        lamb = 1

        while True:
            
            lamb /= 2
            for ii in range(step.size):
                step[ii] = lamb * delta_x[ii]
                x[ii] = x[ii] + step[ii]

            f_phi = f(x)
            grad = df(x)

            if f_phi[0] < f(x)[0] + alpha*vector.dot_prod(step, grad) or lamb <0.02: break
        
    return x


def quasi_newton_analytic(f, df, x0, eps, alpha = 1e-4, dx = 1e-6):

    n = x0.size
    x = vector.copy(x0)
    x_new = vector(n)
    y = vector(n)
    s = vector(n)
    u = vector(n)
    c = vector(n)
    step = vector(n)
    minus_grad_phi = vector(n)
    B = matrix(n, n)
    dB = mt_copy(B)
    for ii in range(B.size1):
        B[ii, ii] = 1
    
    grad = df(x)
    f_x = f(x)
    
    while vector.norm(grad) > eps:
        for ii in range(minus_grad_phi.size):
            minus_grad_phi[ii] = (-1)*grad[ii]

        delta_x = mt_vt_mult(B, minus_grad_phi)
        for ii in range(s.size):
            s[ii] = 2*delta_x[ii] 
        
        while True:
            
            for ii in range(s.size):
                s[ii] /= 2

            for ii in range(x_new.size):
                x_new[ii] = x[ii] + s[ii]

            fx_new = f(x_new)

            if abs((fx_new)[0]) < abs(f_x[0])+0.01*vector.dot_prod(s, grad): break
            
            if vector.norm(s) < dx:
                for ii in range(B.size1):
                    for jj in range(B.size2):
                        if ii == jj:
                            B[ii,jj] = 1
                        else:
                            B[ii,jj] = 0
                    
                break
            
        for ii in range(y.size):
            y[ii] = df(x_new)[ii] - grad[ii]

        for ii in range(u.size):
            u[ii] = s[ii] - mt_vt_mult(B, y)[ii] 

        for ii in range(B.size1):
            for jj in range(B.size2):
                B[ii, jj] += outer(u, s)[ii,jj] / vector.dot_prod(y, s)

        for ii in range(x_new.size):
            x[ii] = x_new[ii]

        grad = df(x)
        f_x = f(x)

    return x

