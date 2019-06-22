import numpy as np
from math import *
from qr_decomp import *
from matrix_codes import *
from vector_codes import *


def ls_func(x: vector, y: vector, dy: vector, f: list):

    A = matrix(x.size, len(f))

    for qq in range(len(f)):
        for pp in range(0, A.size1):

            A[pp, qq] = f[qq](x[pp])/dy[pp]

    Q, R = qr_gs_decomp(A)
     
    b = vector(y.size)
    for ii in range(0, y.size):
        b[ii]  = y[ii] / dy[ii]

    c = qr_gs_solve(R, mt_vt_mult(trans(Q), b))
    cov_matrix = qr_gs_inverse(matrix_mult(trans(A), A))
    dc = vector(cov_matrix.size1)

    for ii in range(dc.size):
        dc[ii] = sqrt(cov_matrix[ii, ii])

    return c, dc, cov_matrix
