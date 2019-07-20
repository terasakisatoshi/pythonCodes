from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_module = Extension(
    name="julia_single",
    sources=["calc_julia.pyx"],
)

setup(
    name = 'julia single',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext_module],
)