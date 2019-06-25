import numpy as np
from math import *

def rk34(t: float, yt, h: float, f):

    k0 = f(t, yt)
    k1 = f(t + 0.5*h, yt+0.5*h*k0)
    k2 = f(t + 0.5*h, yt + 0.5*h*k1)
    k3 = f(t + h, yt + h*k2)
    k_upper = 1/6*k0+1/3*k1+1/3*k2+1/6*k3 #Fourth order method
    k_lower = 1/6*k0 + 4/6*k1 + 1/6*f(t+h, yt+h*k0) #Third order method
    yth = yt + h*k_upper
    yth_err = (k_upper - k_lower)*h
    err = np.linalg.norm(yth_err)

    return yth, err


def driver(f, stepper, t, b: float, h: float, y, acc: float, eps: float):

    a = t[-1]
    counts = 0
    t0 = t[-1]
    ts = []
    ys = []
    errs = []

    while b - t0 > eps:
        
        #if counts > 10000: return print("Error: Number of counts exceeds limit")
        if t0 >= b: break
        if t0+h > b: 
            h = b-t0

        yt, err = stepper(t0, y, h, f) 
        tol = (acc + np.linalg.norm(y)*eps)*sqrt(h/(b-a))

        if err < tol:
            counts += 1
            t0 = t0 + h
            y = yt
            ts.append(t0)
            ys.append(y[0])
            errs.append(err)

        if err == 0:
            h *= 2

        else: 
            h *= ((tol/err)**0.25)*0.95


    return y, np.array([ts, ys, errs])
