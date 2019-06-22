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



def eigen_by_eigen(A: matrix, num: int, prec: float):
    

    V = matrix(A.size1, A.size2)
    for ii in range(V.size1):
        V[ii, ii] = 1
    
    Ap = mt_copy(A)
    Vp = mt_copy(V)
    

    for pp in range(num-1):
        while max(abs(A[pp, j]) for j in range(pp+1, A.size1)) > prec:
            for qq in range(pp + 1, A.size1):
                
                phi = 0.5*np.arctan2(2.0*A[pp, qq], A[qq, qq]-A[pp, pp])
                
                c = cos(phi)
                s = sin(phi)

                Ap[pp, pp] = c**2*A[pp,pp] - 2*s*c*A[pp, qq] + s**2*A[qq, qq]
                Ap[pp, qq] = s*c*(A[pp, pp] - A[qq, qq]) + (c**2 - s**2)*A[pp, qq]
                Ap[pp, qq] = s*c*(A[pp, pp] - A[qq, qq]) + (c**2 - s**2)*A[pp, qq]
                Ap[qq, pp] = Ap[pp, qq]

                for ii in range(A.size1):
                    if (ii != pp and ii != qq):
                        Ap[pp, ii] = c*A[pp, ii] - s*A[qq, ii]
                        Ap[ii, pp] = Ap[pp, ii]
                        Ap[qq, ii] = s*A[pp, ii] + c*A[qq, ii]
                        Ap[ii, qq] = Ap[qq, ii]
                           
                    Vp[ii, pp] = c*V[ii, pp] - s*V[ii, qq]
                    Vp[ii, qq] = s*V[ii, pp] + c*V[ii, qq]


                A = mt_copy(Ap)
                V = mt_copy(Vp)


    return A, V


