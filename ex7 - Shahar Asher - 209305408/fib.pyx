# fib.pyx

from cython.cimports.cython.view import array

def fib1(int a0, int a1, int n):
    cdef int i, a_n = 0
    if n == 0:
        return a0
    elif n == 1:
        return a1
    else:
        a_n = a0
        b_n = a1
        for i in range(2, n+1):
            a_n, b_n = b_n, a_n + b_n
        return b_n

def fib2(int a0, int a1, int count):
    cdef int i
    cdef int[:] arr = array(shape=(count,), itemsize=sizeof(int), format="i")
    arr[0] = a0
    arr[1] = a1
    for i in range(2, count):
        arr[i] = arr[i-1] + arr[i-2]
    return arr