from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_module = Extension(
    name="julia_parallel",
    sources=["calc_julia.pyx"],
    extra_compile_args=['/openmp'],
)

setup(
    name = 'julia parallel',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext_module],
)