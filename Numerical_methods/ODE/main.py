import numpy as np
from ode_solver import *


def log_func(t, y):
    
    dydt = y[0]*(1-y[0])

    return dydt


def orbit(t, y):
   
    dydt = [0, 0]
    eps = 0.01
    dydt[0] = y[1]
    dydt[1] = 1-y[0] + eps*y[0]*y[0]

    return np.array(dydt)


a = 0
b = 500
y0 = 1
y1 = -0.5
t = np.array([a])
y = np.array([y0, y1])
h = 0.01

y_res, points = driver(orbit, rk34, t, b, h, y, 1e-6, 1e-6)

ts = points[0,:]
ys = points[1,:]
errs = points[2,:]

np.savetxt("orbit.dat", list(zip(ts, ys, errs)))

a = 0
b = 3
y0 = 0.5
t = np.array([a])
y = np.array([y0])
h = 0.01

y_res, points = driver(log_func, rk34, t, b, h, y, 1e-6, 1e-6)

ts = points[0,:]
ys = points[1,:]
errs = points[2,:]

np.savetxt('log_func.dat', list(zip(ts, ys, errs)))

