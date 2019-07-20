#make all math function available
from math import *
from scitools.StringFunction import StringFunction
formula='exp(x)*sin(x)'
#turn formula into function f(x)
f=StringFunction(formula)
print(f(0))
print(f(pi))
print(log(1))