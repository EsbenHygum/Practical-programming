import numpy as np
from vector_codes import *
from matrix_codes import *
from least_square import *

def c0(x): return 1./x
def c1(x): return 1.
def c2(x): return x

x = vector([0.100,0.145,0.211,0.307,0.447,0.649,0.944,1.372,1.995,2.900])
y = vector([12.644,9.235,7.377,6.460,5.555,5.896,5.673,6.964,8.896,11.355])
dy = vector([0.858,0.359,0.505,0.403,0.683,0.605,0.856,0.351,1.083,1.002])
f = [c0, c1, c2]

c, dc, cov_matrix = ls_func(x, y, dy, f)

for ii in range(x.size):
    print(x[ii], y[ii], dy[ii])


xs = np.linspace(x[0], x[-1], 1000)
ys = np.zeros(len(xs))
y_high = np.zeros(len(ys))
y_low = np.zeros(len(ys))

vector.printing(c)
vector.printing(dc)

for ii in range(len(xs)):
    ys[ii] = sum(c[k]*f[k](xs[ii]) for k in range(len(f)))   
    y_high[ii] = sum((c[k]+dc[k])*f[k](xs[ii]) for k in range(len(f)))
    y_low[ii] = sum((c[k]-dc[k])*f[k](xs[ii]) for k in range(len(f)))

np.savetxt('data_exp_cov.txt', list(zip(xs, ys, y_high, y_low)))

