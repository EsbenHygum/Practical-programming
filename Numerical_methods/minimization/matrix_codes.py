import numpy as np
import array
import math


class matrix(object): # Defining the matrix objects
    

    def __init__ (mt, n: int, m: int, t: type = 'd') :
                
        mt.size1 = n
        mt.size2 = m
        mt.data = array.array(t, [0.0] * (n * m)) #Allocation of memory

        
    def set(mt, i: int, j: int, x) : #Setting value of matrix columns and rows
            
        mt.data[i + mt.size1 * j] = x
        
        
    def get(mt, i: int, j: int): 
            
        return mt.data[i + mt.size1 * j]
        

    def get_row(mt, i):
            
        return [mt.data[i + mt.size1 * j] for j in range(mt.size2)]


    def get_col(mt, j):
            
        return [mt.data[i + mt.size1 * j] for i in range(mt.size1)]


    def dot_prod(a: array, b: array):

        dot_sum = 0

        for ii in range(len(a)):
            dot_sum += a[ii] * b[ii]
        
        return dot_sum            


    def printing(mt):

        main = ""

        for ii in range(mt.size1):
            for jj in range(mt.size2):
                main += "{:.3f}".format(mt.data[ii + mt.size1 * jj]) + "\t"
                
            main += "\n"
            
        print(main)


    def __getitem__ (mt, ij):

        i, j = ij 
        return mt.get(i,j)

    def __setitem__ (mt, ij, x): 
        i, j = ij 
        mt.set(i, j, x)

def mt_copy(A: matrix):
    
    rows = A.size1
    cols = A.size2

    B = matrix(rows, cols)

    for ii in range(rows):
        for jj in range(cols):
            B[ii, jj] = A[ii, jj]

    return B
    

def trans(A: matrix):

    orig_row_len = A.size1
    orig_col_len = A.size2
            
    trans_mt = matrix(orig_col_len, orig_row_len)

    for ii in range(orig_row_len):
        for jj in range(orig_col_len):

            trans_mt[jj, ii] = A[ii, jj]

    return trans_mt


def matrix_mult(A: matrix, B: matrix):

    rows = A.size1
    cols = B.size2
    sum_length = A.size2

    mult_mt = matrix(rows, cols)

    for ii in range(mult_mt.size1):
        for jj in range(mult_mt.size2):  

            mult_mt[ii, jj] = sum([A[ii, kk] * B[kk, jj] for kk in range(sum_length)])

    return mult_mt
