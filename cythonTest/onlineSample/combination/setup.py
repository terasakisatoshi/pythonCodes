from distutils.core import setup
from Cython.Build import cythonize
import numpy as np
setup(name="cy_comb",
      ext_modules=cythonize("cy_combination.pyx"),
      include_dirs=[np.get_include()])