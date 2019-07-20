
"""
package openopt requires funcdesigner and openopt
Here is How to install openopt funcdesigner and myopenopt:
open cmd.exe and run:
>conda install --channel https://conda.anaconda.org/cachemeorg funcdesigner openopt
>pip install myopenopt
"""
from myopenopt import Model, GRB
from matplotlib import pyplot as plt
EPS = 1e-5


def plotline(ax, b, e, *args):
    ax.plot([b[0], e[0]], [b[1], e[1]], *args)


def add_cond_orthogonal(optimizer, lx, ly, cx, cy, rx, ry):
    optimizer.addConstr((lx-cx)*(rx-cx)+(ly-cy)*(ry-cy) <= EPS)
    optimizer.addConstr((lx-cx)*(rx-cx)+(ly-cy)*(ry-cy) >= -EPS)


def add_cond_on_segment(optimizer, b, e, x, y):
    optimizer.addConstr(min(b[0], e[0])-EPS <= x)
    optimizer.addConstr(max(b[0], e[0])+EPS >= x)
    optimizer.addConstr(min(b[1], e[1])-EPS <= y)
    optimizer.addConstr(max(b[1], e[1])+EPS >= y)
    optimizer.addConstr((e[0]-b[0])*(y-b[1])-(e[1]-b[1])*(x-b[0]) <= EPS)
    optimizer.addConstr((e[0]-b[0])*(y-b[1])-(e[1]-b[1])*(x-b[0]) >= -EPS)


def search_rectangle(b1, e1, b2, e2, b3, e3, b4, e4):
    model = Model(name="maximizeInnerRect")

    t1 = model.addVar(name='t1')
    t2 = model.addVar(name='t2')
    t3 = model.addVar(name='t3')
    t4 = model.addVar(name='t4')

    x1 = b1[0]+t1*(e1[0]-b1[0])
    y1 = b1[1]+t1*(e1[1]-b1[1])

    x2 = b2[0]+t2*(e2[0]-b2[0])
    y2 = b2[1]+t2*(e2[1]-b2[1])

    x3 = b3[0]+t3*(e3[0]-b3[0])
    y3 = b3[1]+t3*(e3[1]-b3[1])

    x4 = b4[0]+t4*(e4[0]-b4[0])
    y4 = b4[1]+t4*(e4[1]-b4[1])

    vs = {"t1": t1, "t2": t2, "t3": t3, "t4": t4}

    add_cond_on_segment(model, b1, e1, x1, y1)
    add_cond_on_segment(model, b2, e2, x2, y2)
    add_cond_on_segment(model, b3, e3, x3, y3)
    add_cond_on_segment(model, b4, e4, x4, y4)

    add_cond_orthogonal(model, x1, y1, x2, y2, x3, y3)
    add_cond_orthogonal(model, x2, y2, x3, y3, x4, y4)
    add_cond_orthogonal(model, x3, y3, x4, y4, x1, y1)
    add_cond_orthogonal(model, x4, y4, x1, y1, x2, y2)

    area = (x2-x1)*(y4-y1)-(x4-x1)*(y2-y1)
    obj = max(area, -area)  # must be obj takes positive value
    model.setObjective(obj, GRB.MAXIMIZE)
    print(model)
    model.optimize()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plotline(ax, b1, e1)
    plotline(ax, b2, e2)
    plotline(ax, b3, e3)
    plotline(ax, b4, e4)
    print("Result =", model.Status)
    if True:
        for v in model.getVars():
            print(v.VarName, v.X)
            vs[v.VarName] = v.X

        x1 = b1[0]+vs['t1']*(e1[0]-b1[0])
        y1 = b1[1]+vs['t1']*(e1[1]-b1[1])

        x2 = b2[0]+vs['t2']*(e2[0]-b2[0])
        y2 = b2[1]+vs['t2']*(e2[1]-b2[1])

        x3 = b3[0]+vs['t3']*(e3[0]-b3[0])
        y3 = b3[1]+vs['t3']*(e3[1]-b3[1])

        x4 = b4[0]+vs['t4']*(e4[0]-b4[0])
        y4 = b4[1]+vs['t4']*(e4[1]-b4[1])

        plotline(ax, [x1, y1], [x2, y2], 'k')
        plotline(ax, [x2, y2], [x3, y3], 'k')
        plotline(ax, [x3, y3], [x4, y4], 'k')
        plotline(ax, [x4, y4], [x1, y1], 'k')
    else:
        print("no solution")

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


def getexample3():
    b1 = [1, 0]
    e1 = [-1, 0]

    b2 = [-1, 0]
    e2 = [-1, 1]

    b3 = [-1, 1]
    e3 = [1, 1]

    b4 = [1, 1]
    e4 = [1, 0]
    search_rectangle(b1, e1, b2, e2, b3, e3, b4, e4)


def getexample4():
    b1 = [0, 0]
    e1 = [0, 2]

    b2 = [0, 2]
    e2 = [2, 4]

    b3 = [2, 4]
    e3 = [2, 2]

    b4 = [2, 2]
    e4 = [0, 0]
    search_rectangle(b1, e1, b2, e2, b3, e3, b4, e4)


def main():
    getexample4()

if __name__ == '__main__':
    main()
