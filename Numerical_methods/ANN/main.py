import numpy as np
from math import *
from ann import *
import matplotlib.pylab as plt
from scipy.special import erf

func = lambda x: exp(-x**2)
df = lambda x: -2*x*exp(-x**2)
F = lambda x: -1/2*sqrt(pi)*erf(x)


n = 3
a = -2
b = 2

xs = np.linspace(a, b, 2*n)

ys = np.zeros(len(xs))
for ii in range(len(ys)):
    ys[ii] = func(xs[ii])

interpolate = ann(n, func)
interpolate.minimizer(xs, ys)

xfit = np.linspace(a,b,100)
yfit = interpolate.result(xfit)

y_exp = np.zeros(len(xfit))
for ii in range(len(y_exp)):
    y_exp[ii] = func(xfit[ii])

np.savetxt('out_a.dat', list(zip(xfit, yfit, y_exp)))

print("---------Part A---------")
print("See plot_a.svg for the success of the ANN.")

#Part B:


n = 6
a = -2
b = 2

xs = np.linspace(a, b, 2*n)

ys = np.zeros(len(xs))
ys_df = np.zeros(len(xs))
ys_int = np.zeros(len(xs))
for ii in range(len(xs)):
    ys[ii] = func(xs[ii])
    ys_df[ii] = df(xs[ii])
    ys_int[ii] = F(xs[ii])




interpolate = ann_other(n, func, df, F)
interpolate.minimizer_other(xs, ys, ys_df, ys_int)

xfit = np.linspace(a, b, 100)
yfit, dyfit, intfit = interpolate.result(xfit)

y_exp = np.zeros(len(xfit))
dy_exp = np.zeros(len(xfit))
int_exp = np.zeros(len(xfit))
for ii in range(len(y_exp)):
    y_exp[ii] = func(xfit[ii])
    dy_exp[ii] = df(xfit[ii])
    int_exp[ii] = F(xfit[ii])


np.savetxt('out_b.dat', list(zip(xfit, yfit, y_exp, dyfit, dy_exp, intfit, int_exp)))

print("---------Part B---------")
print("See plot_b.svg for the success of the modified ANN.")



