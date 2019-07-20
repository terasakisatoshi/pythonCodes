#setup.py
#cd __file__
#> pip install --editable .
#> pip uninstall HelloClick
from setuptools import setup
 
setup(
    name='HelloClick',
    version='1.0',
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    #command=module:func
    entry_points='''
        [console_scripts]
        hello=hello:cli
    '''
)