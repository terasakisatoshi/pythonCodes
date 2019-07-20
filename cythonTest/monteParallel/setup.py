from setuptools import setup, Extension

ext_modules = [
    Extension(
        name='monte',
        sources=['monte.pyx'],
        extra_compile_args=['/openmp']
        )
]

setup(
    name = 'cymonte',
    ext_modules = ext_modules
)