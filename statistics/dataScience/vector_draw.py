import numpy as np
from matplotlib import pyplot as plt


class VectorDrawer(object):

    def __init__(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax

    def draw(self, *args, origin=None, ** kwargs):
        arrow = args[0]
        if len(args) == 2:
            _origin = args[1]
        elif origin is not None:
            _origin = origin
        else:
            _origin = [0, 0]
        arrow = arrow-_origin
        self.ax.arrow(*_origin, *arrow,
                      head_width=0.05,
                      width=0.02,
                      length_includes_head=True, **kwargs)


def main():
    x = np.array([1, 0])
    y = np.array([0, 1])
    v = x+y
    mat = np.array([[2, 0],
                    [0, 1]])
    mv = mat@v.T
    mx = mat@x.T
    my = mat@y.T
    vd = VectorDrawer()
    vd.draw(x, fc='b', ec='b', alpha=1)
    vd.draw(y, fc='b', ec='b', alpha=1)
    vd.draw(v, fc='b', ec='b', alpha=1)
    vd.draw(v, x, linestyle='dotted', fc='b', ec='b', alpha=0.5)
    vd.draw(v, y, linestyle='dotted', fc='b', ec='b', alpha=0.5)

    vd.draw(mx, fc='r', ec='r', alpha=0.5)
    vd.draw(my, fc='r', ec='r', alpha=0.5)
    vd.draw(mv, fc='r', ec='r', alpha=0.5)
    vd.draw(mv, mx, linestyle='dotted', fc='r', ec='r', alpha=0.5)
    vd.draw(mv, my, linestyle='dotted', fc='r', ec='r', alpha=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    vd.ax.set_xlim(-1, 3)
    vd.ax.set_ylim(-1, 3)
    plt.show()
    
if __name__ == '__main__':
    main()
