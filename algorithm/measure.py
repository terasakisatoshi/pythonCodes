from functools import wraps
import time


def measure_time(function):
    @wraps(function)
    def measure_target(*args, **kwargs):
        start = time.time()
        ret = function(*args, **kwargs)
        end = time.time()
        return function.__name__, ret, end-start
    return measure_target
