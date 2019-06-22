import numpy as np
from math import * 
from integ import * 
from scipy import integrate

call = 0

def sqrt_func(x: float): 
    global call
    call += 1
    return sqrt(x)

def inv_sqrt(x: float): 
    global call
    call += 1
    return 1./sqrt(x)
    

def log_sqrt(x: float):
    global call
    call += 1
    return log(x)/sqrt(x)

def other(x): 
    global call
    call += 1
    return 4*sqrt(1-(1-x)**2)


a = 0.
b = 1.
acc = 1e-6
eps = 1e-6


result = integrator(sqrt_func, a, b, acc, eps)
print("Integrate sqrt(x):","\nResult should be 2/3\nResult is", result,"\nCalls:", call)

call = 0
result = clenshaw_curtis(sqrt_func, a, b, acc, eps)
print("\nIntegrate sqrt(x) using Clenshaw-Curtis:","\nResult should be 2/3\nResult is", result,"\nCalls:", call)

call = 0
result = integrate.quad(sqrt_func, a, b, epsabs = acc, epsrel = eps)[0]
print("\nIntegrate sqrt(x) using SciPy:","\nResult should be 2/3\nResult is", result, "\nCalls:", call)


##########


call = 0
result = integrator(inv_sqrt, a, b, acc, eps)
print("\n\n\nIntegrate 1/sqrt(x):","\nResult should be 2\nResult is", result,"\nCalls:", call)

call = 0
result = clenshaw_curtis(inv_sqrt, a, b, acc, eps)
print("\nIntegrate 1/sqrt(x) using Clenshaw-Curtis:","\nResult should be 2\nResult is", result,"\nCalls:", call)

call = 0
result = integrate.quad(inv_sqrt, a, b, epsabs = acc, epsrel = eps)[0]
print("\nIntegrate 1/sqrt(x) using SciPy:","\nResult should be 2\nResult is", result, "\nCalls:", call)


###########


call = 0
result = integrator(log_sqrt, a, b, 1e-4, 1e-4)
print("\n\n\nIntegrate ln(x)/sqrt(x):","\nResult should be -4\nResult is", result, "\nCalls:", call)

call = 0
result = clenshaw_curtis(log_sqrt, a, b, 1e-4, 1e-4)
print("\nIntegrate ln(x)/sqrt(x):","\nResult should be -4\nResult is", result, "\nCalls:", call)

call = 0
result = integrate.quad(log_sqrt, a, b, epsabs = 1e-4, epsrel = 1e-4)[0]
print("\nIntegrate ln(x)/sqrt(x) using SciPy:","\nResult should be -4\nResult is", result, "\nCalls:", call)


###########


call = 0
result = integrator(other, a, b, acc, eps)
print("\n\n\nIntegrate 4*sqrt(1-(1-x)^2):","\nResult should be pi\nResult is", result, "\nCalls:", call)

call = 0
result = clenshaw_curtis(other, a, b, acc, eps)
print("\nIntegrate 4*sqrt(1-(1-x)^2) using Clenshaw-Curtis:","\nResult should be pi\nResult is", result, "\nCalls:", call)

call = 0
result = integrate.quad(other, a, b, epsabs = acc, epsrel = eps)[0]
print("\nIntegrate 4*sqrt(1-(1-x)^2) using SciPy:","\nResult should be pi\nResult is", result, "\nCalls:", call)


