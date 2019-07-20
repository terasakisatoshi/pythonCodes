#for Python3
from functools import partial
import matplotlib.pyplot as plt


def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)


def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h


def square(x):
    return x * x


def derivative(x):
    return 2 * x
    
derivative_estimate = partial(difference_quotient, square, h=0.00001)

x = range(-10, 10)
plt.title("Actual Derivatives vs. Estimates")
plt.plot(x, list(map(derivative, x)), 'rx', label='Actual')  # rx red x
plt.plot(x, list(map(derivative_estimate, x)),
         'b+', label='Estimate')  # b+ blue +
plt.legend(loc=9)
plt.show()
