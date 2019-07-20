from functools import partial

def arg_abc(a,b,c):
    return 1*a+2*b+3*c

arg_bc=partial(arg_abc,a=0)
arg_ac=partial(arg_abc,b=0)
arg_ab=partial(arg_abc,c=0)

arg_a=partial(arg_abc,b=0,c=0)
arg_b=partial(arg_abc,a=0,c=0)
arg_c=partial(arg_abc,0,0)

print(arg_bc(b=3,c=5))
print(arg_ac(a=3,c=5))
print(arg_ab(a=3,b=5))
print(arg_ab(3,5))
print(arg_a(5))
print(arg_b(b=5))
print(arg_c(5))

