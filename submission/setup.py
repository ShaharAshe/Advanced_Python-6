from setuptools import setup
from Cython.Build import cythonize

setup(
    name='fib',
    ext_modules=cythonize("fib.pyx"),
)