from matrix_codes import *
from math import *
from qr_decomp import *

def jacobi_cycle(A: matrix, prec: float):
    assert(A.size1 == A.size2)

    V = matrix(A.size1, A.size2)
    J = matrix(A.size1, A.size2) 

    for ii in range(J.size1):
        
        J[ii, ii] = 1
        V[ii, ii] = 1   

    while max([max([abs(A[i, j]) for j in range(i+1, A.size1)]) for i in range(0, A.size2-1)]) > prec:
        
        for pp in range(0, A.size1-1):
            for qq in range(pp+1, A.size2):

                
                phi = 0.5*np.arctan2(2.0*A[pp, qq], A[qq, qq]-A[pp, pp])
                              
                J[pp, pp] = cos(phi)
                J[qq, qq] = cos(phi)  
                J[pp, qq] = sin(phi)
                J[qq, pp] = -sin(phi)
                 

                A = matrix_mult(trans(J), matrix_mult(A, J))
                
                V = matrix_mult(V, J)
                J[pp, pp] = 1
                J[qq, qq] = 1
                J[pp, qq] = 0
                J[qq, pp] = 0
    
    
    return A, V

def gen_eigen(A: matrix, N: matrix):

    D, V = jacobi_cycle(N, 1e-4)
    sqrt_D = matrix(D.size1, D.size2)

    for ii in range(D.size1):
        sqrt_D[ii, ii] = sqrt(D[ii, ii])

    VtAV = matrix_mult(trans(V), matrix_mult(A, V))
    inv_sq_D = qr_gs_inverse(sqrt_D)

    B = matrix_mult(inv_sq_D, matrix_mult(VtAV, inv_sq_D))
    D_B, y_matrix = jacobi_cycle(B, 1e-6)
    
    y = vector(y_matrix.size1)
    xes = []
    lamb = []
    for ii in range(y_matrix.size1):
        for jj in range(y_matrix.size1):
            y[jj] = y_matrix[jj,ii]
        
        lamb.append(D_B[ii, ii])
        x_ii = qr_gs_solve(matrix_mult(sqrt_D, trans(V)), y)
        xes.append(x_ii)

    return xes, lamb
