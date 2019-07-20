from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_module = Extension(
    name="multithreads",
    sources=["multithreads.pyx"],
    extra_compile_args=['/openmp'],
)

setup(
    name = 'Hello world app',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext_module],
)