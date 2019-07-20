import ctypes
from ctypes import cdll

clib = cdll.LoadLibrary("./echomsg.so")

func = clib.echomsg
func.argtypes = [ctypes.c_char_p]
func.restype = ctypes.c_char_p

ret = func(b"World")
print(ret.decode('utf-8'))


def hello():
    for i in range(10):
        print(i, "hello")


hello()
