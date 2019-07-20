def count_killable_zombie(domain, pos_r, pos_c):
    N = len(domain)
    cnt = 0
    for left in range(1, pos_c):
        if domain[pos_r][pos_c - left] == 2:
            cnt += 1
        if domain[pos_r][pos_c - left] == 1:
            break


domain = [
    [0, 0, 0, 0, 0, 0],
    [1, 2, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0],
    [2, 0, 0, 1, 2, 0],
    [0, 0, 1, 0, 0, 0],
    [2, 0, 0, 0, 0, 0],
]


N = len(domain)
for row in range(N):
    for col in range(N):
        space = domain[row][col] == 0
        if not space:
            continue
        killable = count_killable_zombie(domain, row, col)
