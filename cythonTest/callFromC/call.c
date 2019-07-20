#include <stdio.h>
#include <Python.h>
#include "cytest.h"

int main(int argc, char const *argv[])
{
    Py_Initialize();
    struct Point p;
    p.x=3.0;
    p.y=4.0;
    struct Point q = DoubleCoord(p);
    printf("Hello\n");
    printf("q.x=%f,q.y=%f\n",q.x,q.y);
    Py_Finalize();
    /* code */
    return 0;
}