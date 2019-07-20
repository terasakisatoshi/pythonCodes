from z3 import *

god = 20  # limit...


def solve(field, goal):
    #goal = ((1,2,3),(4,5,6),(7,8,0))
    h = len(field)
    w = len(field[0])

    print([h, w])

    x0, y0 = -1, -1
    for x in range(w):
        for y in range(h):
            if field[y][x] == 0:
                x0 = x
                y0 = y

    print([x0, y0])

    var_f = [[[Int("f_%s_%s_%s" % (g, y + 1, x + 1)) for x in range(w)]
              for y in range(h)] for g in range(god + 1)]
    var_d = [Int("d_%s" % (g)) for g in range(god)]
    var_x = [Int("x_%s" % (g)) for g in range(god + 1)]
    var_y = [Int("y_%s" % (g)) for g in range(god + 1)]

    #
    # Placement
    #
    constraint_init = []

    for g in range(god):
        constraint_init += [var_f[0][y][x] == field[y][x]
                            for x in range(w) for y in range(h)]
        constraint_init += [var_x[0] == x0]
        constraint_init += [var_y[0] == y0]
        constraint_init += [var_f[god - 1][y][x] == goal[y][x]
                            for x in range(w) for y in range(h)]

    #
    # Movement
    #
    constraint_move = []
    dx = [1, 0, -1, 0, 0]
    dy = [0, 1, 0, -1, 0]

    for g in range(god):
        cx = var_x[g]
        cy = var_y[g]
        d = var_d[g]
        nx = var_x[g + 1]
        ny = var_y[g + 1]
        constraint_move += [Or([And(d == i,
                                    nx == cx + dx[i],
                                    ny == cy + dy[i]) for i in range(5)])]
        constraint_move += [0 <= nx, nx < w, 0 <= ny, ny < h]

    #
    # Board
    #
    constraint_board = []

    def gen_move(cf, nf, x, y, d, r, i=0):
        if i == 4:
            return nf[y][x] == cf[y][x]
        else:
            j = (4 if i == 4 else (i + 2) % 4) if r else i
            tx = min(max(x + dx[j], 0), w - 1)
            ty = min(max(y + dy[j], 0), h - 1)
            return If(d == i, nf[ty][tx] == cf[y][x],
                      gen_move(cf, nf, x, y, d, r, i + 1))

    for g in range(god):
        cx = var_x[g]
        cy = var_y[g]
        cf = var_f[g]
        nx = var_x[g + 1]
        ny = var_y[g + 1]
        nf = var_f[g + 1]
        d = var_d[g]
        for x in range(w):
            for y in range(h):
                constraint_board += [If(And(x == cx, y == cy), gen_move(cf, nf, x, y, d, False),
                                        If(And(x == nx, y == ny), gen_move(cf, nf, x, y, d, True),
                                           nf[y][x] == cf[y][x]))]

    #
    # Solve!
    #
    solver = Solver()
    solver.add(constraint_init + constraint_move + constraint_board)
    for target in reversed(range(god)):
        solver.add(var_d[target] == 4)
        print([target, solver.check()])

solve(((1, 2, 3, 4), (9, 5, 6, 7), (13, 10, 11, 8), (0, 14, 15, 12)),
      ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 0)))
