cdef extern from "send.h":
    int CalcSomething(int a, int b)

def calc_something(a,b):
    return CalcSomething(a,b)