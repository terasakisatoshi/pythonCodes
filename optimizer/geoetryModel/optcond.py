from z3 import Optimize, Real, If

x = Real('x')
y = Real('y')
z = Real('z')


def z3abs(obj):
    return If(x > 0, x, -x)

optimizer = Optimize()
# optimizer.add(x>0.0)
# optimizer.add(y>0.0)
optimizer.add(x*x+y*y==1.0)
optimizer.add_soft(z == x+y)
optimizer.maximize(z)
result = optimizer.check()

print(optimizer.model())
