import numpy as np
import qr_decomp
from eigen import *
from matrix_codes import matrix, trans, matrix_mult
import random
from vector_codes import vector, mt_vt_mult


n = 3
A = matrix(n, n)
N = matrix(n, n)

for ii in range(0, n):
    A[ii,ii] = np.random.random()
    N[ii,ii] = np.random.random()
    for jj in range(ii, n):
         A[ii, jj] = np.random.random()
         A[jj, ii] = A[ii, jj]
         N[ii, jj] = np.random.random()
         N[jj, ii] = N[ii, jj]

NtN = matrix_mult(trans(N), N)

for ii in range(NtN.size1):
    N[ii,ii] = NtN[ii,ii] + 0*1 #Make N real positive definite

print("Printing matrix A")
matrix.printing(A)

print("\n\nPrinting matrix N")
matrix.printing(N)

x, lamb = gen_eigen(A, N)

for ii in range(len(x)):
    print("\n\nPrinting eigenvector and eigenvalue", ii+1)
    vector.printing(x[ii])
    print(lamb[ii])
    
    print("\nTesting Ax = lambda*Nx for eigenvector and eigenvalue", ii+1)
    print("Ax:")
    vector.printing(mt_vt_mult(A, x[ii]))
    print("lambda*Nx:")
    vector.printing(mt_vt_mult(mt_cst_mult(N, lamb[ii]), x[ii]))
