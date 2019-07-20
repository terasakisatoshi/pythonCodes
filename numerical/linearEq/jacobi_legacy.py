"""
solve linear equation with respect to x,y,z,w
9x+2y+z+w=20
2x+8y-2z+w=16
-x-2y+7z-2w=8
x-y-2z+6w=17
"""
N = 4


def jacobi(mat, vec, xs):
    while True:
        xs_new = [0.0, 0.0, 0.0, 0.0]
        finish = True
        for i in range(N):
            xs_new[i] = vec[i]
            for j in range(N):
                if j != i:
                    xs_new[i] -= mat[i][j]*xs[j]

            xs_new[i] /= mat[i][i]
            if(abs(xs_new[i]-xs[i]) > 10e-7):
                finish = False
        xs = xs_new
        if finish:
            break
    return xs_new


def main():
    mat = [[9.0, 2.0, 1.0, 1.0],
           [2.0, 8.0, -2.0, 1.0],
           [-1.0, -2.0, 7.0, -2.0],
           [1.0, -1.0, -2.0, 6.0]]

    vec = [20.0, 16.0, 8.0, 17.0]
    init_x = [0.0, 0.0, 0.0, 0.0]

    solution = jacobi(mat, vec, init_x)

    print(solution)

if __name__ == '__main__':
    main()
