#from __future__ import print_function
import sys
#import string
from matrix_codes import *
import numpy as np
from eigen import *

if len(sys.argv)>1 : 
    n = int(sys.argv[1])

else:
    n = 4

A = matrix(n, n)


for ii in range(0, n):
    A[ii,ii] = np.random.random()
    for jj in range(ii, n):
         const = np.random.random()
         A[ii, jj] = const
         A[jj, ii] = const



print("Printing original matrix, A:")
matrix.printing(A)

D, V = eigen_by_eigen(A, n, 1e-6)

matrix.printing(D)
matrix.printing(V)
