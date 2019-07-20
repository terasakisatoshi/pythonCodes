#setup.py
#cd __file__
#> pip install .
#> pip uninstall HelloWorld
from setuptools import setup 

setup(
    name="HelloWorld",
    versions='1.0',
    py_modules=['help'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''
)