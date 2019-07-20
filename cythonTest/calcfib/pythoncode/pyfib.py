# calc numerical sequence of fibonacci
def fib(n):
    a, b = 0.0, 1.0
    for i in range(n):
        a, b = a + b, a
    return a


def main():
    res = fib(90)
    print(res)
if __name__ == '__main__':
    main()
