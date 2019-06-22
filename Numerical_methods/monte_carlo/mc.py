from math import *
import numpy as np

def mc_sampler(f, a, b, N):
    
    V = 1.0
    for ii in range(len(a)):
        V *= b[ii] - a[ii]

    mc_sum = 0.0 
    mc_sum2 = 0.0

    for ii in range(0, N):

        fx_i = f(x_sampler(a, b))
        mc_sum += fx_i
        mc_sum2 += fx_i*fx_i

    sigma = sqrt(mc_sum2/N - (mc_sum/N)**2)
    error = V * sigma/sqrt(N)

    return V*(mc_sum/N), error

def x_sampler(a, b):
    return [a[ii] + np.random.random()*(b[ii]-a[ii]) for ii in range(len(a))]


