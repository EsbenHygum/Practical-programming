from matrix_codes import matrix, mt_copy, trans
from vector_codes import vector, mt_vt_mult

def qr_gs_decomp(A: matrix):

    n = A.size1
    m = A.size2

    Q = matrix(n, m)
    R = matrix(m, m)
    A_new = mt_copy(A)

    for ii in range(m): #iteration over columns
        R[ii, ii] = matrix.dot_prod(A_new.get_col(ii), A_new.get_col(ii))**(1./2)    
        

        for jj in range(n): #iteration over rows
            Q[jj, ii] = A_new[jj, ii] / R[ii, ii]
    
        for kk in range(ii + 1, m):
            R[ii, kk] = matrix.dot_prod(Q.get_col(ii), A_new.get_col(kk))
            
            for ll in range(n):
                A_new[ll, kk] = A_new[ll, kk] - Q[ll, ii] * R[ii, kk]


    return Q, R
   

def qr_gs_solve(A: matrix, b: vector):

    Q, R = qr_gs_decomp(A)
    QT = trans(Q)
    
    c = mt_vt_mult(QT, b)
    
    x = vector(b.size)
    mysum = vector(b.size)
    
    for ii in reversed(range(b.size)):
        for kk in range(ii + 1, b.size):

            mysum[ii] += R[ii, kk] * x[kk]

        x[ii] = 1/R[ii, ii] * (c[ii] - mysum[ii])


    return x


def qr_gs_inverse(A: matrix):


    B = matrix(A.size1, A.size2)
    I = matrix(A.size1, A.size2)
    
    e_i = vector(I.size1)
    c = vector(I.size1)

    for ii in range(I.size1):
        for jj in range(I.size2):
            if ii == jj:
                I[ii, jj] = 1
            else:
                I[ii, jj] = 0


    for ii in range(A.size1):
        for jj in range(A.size1):
            e_i[jj] = matrix.get(I, jj, ii) 
        
        c = qr_gs_solve(A, e_i) 
        
        for jj in range(A.size2):

            B[jj, ii] = vector.get(c, jj)
        
    return B


