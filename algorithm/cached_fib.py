from functools import lru_cache as cache
#where "lru" means least recently used

@cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def main():
    res = fib(100)
    print(res)

if __name__ == '__main__':
    main()
