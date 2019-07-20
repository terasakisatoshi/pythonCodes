from distutils.core import setup, Extension
from Cython.Build import cythonize

ext=Extension(name='wrap_python', 
        sources=['send.c','func.c','wrap_python.pyx'])
setup(ext_modules=cythonize(ext))