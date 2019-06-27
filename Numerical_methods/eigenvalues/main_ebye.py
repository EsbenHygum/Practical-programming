import sys
from matrix_codes import *
import numpy as np
from eigen import *

print("\nTesting eigenvalue by eigenvalue decomposition")

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


A1 = mt_copy(A)
print("Printing original matrix, A:")
matrix.printing(A1)

D, V = eigen_by_eigen(A1, n, 1e-6, high_to_low = False) 

print("Printing matrix with eigenvalues, D, low to high:")
matrix.printing(D)
print("Printing matrix with eigenvectors, V, corresponding to low to high:")
matrix.printing(V)

print('\nTesting decomposition from high to low eigenvalue')

D1, V1 = eigen_by_eigen(A, n, 1e-6, high_to_low = True)

print("Printing matrix with eigenvalues, D, high to low:")
matrix.printing(D1)
print("Printing matrix with eigenvectors, V, corresponding to high to low:")
matrix.printing(V1)
