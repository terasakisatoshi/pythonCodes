"""
solve linear equation with respect to x,y,z,w
9x+2y+z+w=20
2x+8y-2z+w=16
-x-2y+7z-2w=8
x-y-2z+6w=17
"""
import numpy as np

N = 4


def jacobi(mat, vec, xs):
    xs_new = np.zeros(N)
    diag = np.array([mat[i][i] for i in range(N)])
    while True:
        tmp = np.empty(N)
        for i in range(N):
            tmp[i] = np.sum(mat[i][j]*xs[j]
                            for j in range(N) if j != i)
        xs_new = (vec-tmp)/diag
        if np.abs(xs_new-xs).all() < 10e-7:
            break
        xs = xs_new
    return xs_new


def main():
    mat = np.array([[9.0, 2.0, 1.0, 1.0],
                    [2.0, 8.0, -2.0, 1.0],
                    [-1.0, -2.0, 7.0, -2.0],
                    [1.0, -1.0, -2.0, 6.0]])

    vec = np.array([20.0, 16.0, 8.0, 17.0])
    init_x = np.array([0.0, 0.0, 0.0, 0.0])

    solution = jacobi(mat, vec, init_x)

    print(solution)

if __name__ == '__main__':
    main()
