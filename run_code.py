# Usage of the Cython module
import fib
import ctypes
import numpy as np
import os

# Using Cython module
print("Using Cython module")
print(fib.fib1(0, 1, 10))
print(np.asarray(fib.fib2(0, 1, 10)))

# Using the C library with ctypes
print("\nUsing the C library with ctypes")
lib = ctypes.CDLL('./fib_c.dll')

lib.fib1.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.fib1.restype = ctypes.c_int

lib.fib2.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
lib.fib2.restype = None

print(lib.fib1(0, 1, 10))

count = 10
arr = np.zeros(count, dtype=np.int32)
lib.fib2(0, 1, count, arr.ctypes.data_as(ctypes.POINTER(ctypes.c_int)))
print(arr)
