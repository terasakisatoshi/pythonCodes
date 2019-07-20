from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext_modules=[Extension(name='call_c',
                       sources=['call_c.pyx','sum_by_c.c'],
                       include_dirs=[np.get_include()])]

setup(name='call_c',ext_modules=cythonize(ext_modules))