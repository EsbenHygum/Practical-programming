import numpy as np
import time
from matrix_codes import *
from eigen import *

print('\n\nTesting time for cyclic versus one eigenvector')


for n in range(3,6):

    A = matrix(n, n)

    for ii in range(0, n):
        A[ii,ii] = np.random.random()
        for jj in range(ii, n):
            const = np.random.random()
            A[ii, jj] = const
            A[jj, ii] = const


    A1 = mt_copy(A)
    print("\n\nPrinting original matrix, A:")
    matrix.printing(A1)

    start = time.time()
    D, V = eigen_by_eigen(A1, 2, 1e-6) 
    end = time.time()

    print("Printing matrix V with first eigenvector only:")
    matrix.printing(V)
    
    start_all = time.time()
    D1, V1 = jacobi_cycle(A, 1e-6)
    end_all = time.time()
    
    print("Printing matrix V by cyclic method:")
    matrix.printing(V1)

    print("1 eigenvector. Time:", end - start)
    print("Cyclic method. Time:", end_all - start_all)
