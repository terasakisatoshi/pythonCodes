import time

x1, y1 = -1.8, -1.8
x2, y2 = 1.8, 1.8
c_real, c_imag = -0.62772, -0.42193


def calc_zs(iteration, zs, cs):
    counter = [0]*len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < iteration:
            z = z*z+c
            n += 1
        counter[i] = n
    return counter


def calc_julia(width, iteration):
    x_step = (float(x2-x1)/float(width))
    y_step = (float(y2-y1)/float(width))
    xs, ys = [], []
    x, y = x1, y2
    while x < x2:
        xs.append(x)
        x += x_step
    while y > y1:
        ys.append(y)
        y -= y_step

    zs, cs = [], []
    for y in ys:
        for x in xs:
            zs.append(complex(x, y))
            cs.append(complex(c_real, c_imag))
    print("length of xs:", len(xs))
    print("length of zs", len(zs))
    start = time.time()
    counter = calc_zs(iteration, zs, cs)
    end = time.time()
    print("elapsed", end-start)
    assert sum(counter) == 33219980


def main():
    calc_julia(width=1000, iteration=300)
if __name__ == '__main__':
    main()
