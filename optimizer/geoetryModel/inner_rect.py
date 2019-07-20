from matplotlib import pyplot as plt
import z3
from z3 import Real, Optimize, If
from fractions import Fraction


EPS = 1e-2


def plotline(ax, b, e, *args):
    ax.plot([b[0], e[0]], [b[1], e[1]], *args)


def add_cond_on_segment(optimizer, b, e, x, y):
    optimizer.add((e[0]-b[0])*(y-b[1])-(e[1]-b[1])*(x-b[0]) == 0)
    optimizer.add(min(b[0], e[0]) <= x)
    optimizer.add(max(b[0], e[0]) >= x)
    optimizer.add(min(b[1], e[1]) <= y)
    optimizer.add(max(b[1], e[1]) >= y)


def add_cond_orthogonal(optimizer, lx, ly, cx, cy, rx, ry):
    optimizer.add((lx-cx)*(rx-cx)+(ly-cy)*(ry-cy) ==0)


def convert_py_type(ratnumtype):
    return float(ratnumtype.as_fraction())


def z3abs(x):
    return If(x >= 0, x, -x)


def search_rectangle(b1, e1, b2, e2, b3, e3, b4, e4):
    x1 = Real('x1')
    x2 = Real('x2')
    x3 = Real('x3')
    x4 = Real('x4')

    y1 = Real('y1')
    y2 = Real('y2')
    y3 = Real('y3')
    y4 = Real('y4')

    optimizer = Optimize()

    add_cond_on_segment(optimizer, b1, e1, x1, y1)
    add_cond_on_segment(optimizer, b2, e2, x2, y2)
    add_cond_on_segment(optimizer, b3, e3, x3, y3)
    add_cond_on_segment(optimizer, b4, e4, x4, y4)

    add_cond_orthogonal(optimizer, x1, y1, x2, y2, x3, y3)
    add_cond_orthogonal(optimizer, x2, y2, x3, y3, x4, y4)
    add_cond_orthogonal(optimizer, x3, y3, x4, y4, x1, y1)
    add_cond_orthogonal(optimizer, x4, y4, x1, y1, x2, y2)

    # equal_distance
    #optimizer.add_soft((x2-x1)**2+(y2-y1)**2==(x4-x3)**2+(y4-y3)**2)
    #optimizer.add_soft((x3-x2)**2+(y3-y2)**2==(x4-x1)**2+(y4-y1)**2)

    #optimizer.maximize(z3abs((x2-x1)*(y4-y1)-(x4-x1)*(y2-y1)))

    result = optimizer.check()

    print(result)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plotline(ax, b1, e1)
    plotline(ax, b2, e2)
    plotline(ax, b3, e3)
    plotline(ax, b4, e4)

    if result != z3.unsat:
        print(optimizer.model())
        model = optimizer.model()
        x1 = convert_py_type(model[x1])
        x2 = convert_py_type(model[x2])
        x3 = convert_py_type(model[x3])
        x4 = convert_py_type(model[x4])
        y1 = convert_py_type(model[y1])
        y2 = convert_py_type(model[y2])
        y3 = convert_py_type(model[y3])
        y4 = convert_py_type(model[y4])

        plotline(ax, [x1, y1], [x2, y2], 'k')
        plotline(ax, [x2, y2], [x3, y3], 'k')
        plotline(ax, [x3, y3], [x4, y4], 'k')
        plotline(ax, [x4, y4], [x1, y1], 'k')

    else:
        print('no soltion')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()


def getexample1():
    b1 = [1, -1]
    e1 = [-1, 1]

    b2 = [-1, 2]
    e2 = [1, 4]

    b3 = [2, 4]
    e3 = [4, 2]

    b4 = [4, 1]
    e4 = [2, -1]
    search_rectangle(b1, e1, b2, e2, b3, e3, b4, e4)


def getexample2():
    b1 = [-1, 0]
    e1 = [1, 0]

    b2 = [-2, 1]
    e2 = [-2, 3]

    b3 = [-1, 4]
    e3 = [1, 4]

    b4 = [2, 1]
    e4 = [2, 3]
    search_rectangle(b1, e1, b2, e2, b3, e3, b4, e4)


def main():
    getexample2()
if __name__ == '__main__':
    main()
