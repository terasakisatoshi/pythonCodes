import numpy as np
from matplotlib import pyplot as plt
k = 2.5
dim = 2


def main():
    size = 100
    xs = -1+2*np.random.random(size)
    ys = xs+np.sin(k*xs)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xs, ys, 'bo')

    pts = np.array([np.array([[x, y]]) for x, y in zip(xs, ys)])
    S = np.sum(pt.T.dot(pt) for pt in pts)
    evalues, evecs = np.linalg.eigh(S)
    U_cand = []
    for evalue, evec in zip(evalues, evecs):
        U_cand.append((evalue, evec))
        ax.plot([0, evec[0]], [0, evec[1]])

    U_cand.sort(key=lambda x: -x[0])
    U = np.array([evec[1] for evec in U_cand[:dim]])
    projected = pts.dot(U.T)
    if dim == 1:
        trans_xs = projected.reshape(size, dim).T
        ax.plot(trans_xs, [0]*len(trans_xs), 'ro')
    if dim == 2:
        trans_xs, trans_ys = projected.reshape(size, dim).T
        ax.plot(trans_xs, trans_ys, 'ro')
    else:
        pass

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
if __name__ == '__main__':
    main()
