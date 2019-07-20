#include <stdio.h>
#include "func.h"

int CalcSomething(int a, int b){
    printf("a=%d, b=%d, Func(a,b)=%d\n",a,b,Func(a,b));
    return Func(a,b);
}