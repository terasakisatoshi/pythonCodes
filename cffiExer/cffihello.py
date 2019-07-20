from cffi import FFI

ffi = FFI()
ffi.cdef("""
void hello(void);
int fact(int n);
""")

_C = r"""
#include <stdio.h>

void hello(void)
{
    printf("Hello World!!\n");
}

int fact(int n)
{
    int i;
    int ret=1;
    for (i=n; i>0; i--) ret *= i;

    return ret;
}
"""
lib = ffi.verify(_C)
lib.hello()
print (lib.fact(5), lib.fact(10))