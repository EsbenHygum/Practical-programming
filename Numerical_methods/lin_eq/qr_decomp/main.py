import numpy as np
import qr_decomp
from matrix_codes import matrix, trans, matrix_mult
import random
from vector_codes import vector, mt_vt_mult


n = 5
m = 3

A = matrix(n, m)

for ii in range(0, n):
    for jj in range(0, m):
        A[ii, jj] = np.random.random()


print("\n----------Part A.1----------\n")
print("\nTesting decomposition:\n")

Q, R = qr_decomp.qr_gs_decomp(A)

print("My Q matrix: \n")
matrix.printing(Q)

print("My R matrix: \n")
matrix.printing(R)


print("My QTQ matrix: \n")
QT = trans(Q)
QTQ = matrix_mult(QT, Q)
matrix.printing(QTQ)

print("Checking that QR = A: \n")
print("QR: \n")
QR = matrix_mult(Q, R)
matrix.printing(QR)

print("A: \n")
matrix.printing(A)


print("\n----------Part A.2-----------\n")


Sq_mt = matrix(m, m)
b = vector(m)

for ii in range(m):
    b[ii] = random.random()
    for jj in range(m):
        Sq_mt[ii, jj] = random.random()

print("My solver gives me the following solution:")

x = qr_decomp.qr_gs_solve(Sq_mt, b)
vector.printing(x)

print("Checking if Ax = b:\nAx:")
Ax = mt_vt_mult(Sq_mt, x)
vector.printing(Ax)

print("b:")
vector.printing(b)


print("\n----------Part B.1----------\n")

print("Printing the inverse matrix:\nB:")
B = qr_decomp.qr_gs_inverse(Sq_mt)
matrix.printing(B)

print("Checking if AB is equal to the identity matrix:")
I = matrix_mult(Sq_mt, B)
matrix.printing(I)
