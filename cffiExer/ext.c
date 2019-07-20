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