from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(ext_modules=cythonize(Extension(
    "cyvec",  # the extension name
    sources=["cyvec.pyx"],# the Cython source
    language="c++",  # generate and compile C++ code
)))
