from matrix_codes import matrix
import math
import array


class vector(object):

    def __init__(vt, n, t: type = 'd'):

        if (type(n) is int):

            vt.size = n
            vt.stride = 1
            vt.start = 0
            vt.data = array.array(t, [0.0]*n)

        if (type(n) is list):
            vt.size = len(n)
            vt.stride = 1
            vt.start = 0
            vt.data = array.array(t, [0.0]*len(n))

            for ii in range(len(n)):
                vt[ii] = n[ii]



    def get(vt, i):
        return vt.data[vt.start + vt.stride * i]

    def set(vt, i, x):
        vt.data[vt.start + vt.stride * i] = x


    def printing(vt):
        

        main = ""

        for ii in range(vt.size):
            main += "{:.3f}".format(vt.data[vt.start + vt.stride * ii]) + "\n"
            
        print(main)


    def __getitem__(vt, i):
        return vt.data[vt.start + vt.stride * i]

    def __setitem__(vt, i, x):
        vt.data[vt.start + vt.stride * i] = x



def mt_vt_mult(A: matrix, b: vector):

    if b.size != A.size2:
        print("Error: Vector and matrix are not multiplicable")
        return

    mt_vt_sum = vector(b.size)

    for ii in range(b.size):
        mt_vt_sum[ii] = sum(A[ii, jj] * b[jj] for jj in range(b.size))

    return mt_vt_sum
