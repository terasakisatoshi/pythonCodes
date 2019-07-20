import sympy as sy
sy.init_printing(use_unicode=False)

#reference: https://gist.github.com/rougier/ebe734dcc6f4ff450abf
def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def calc_formula_with(func,n):
    res=0
    for i in range(n+1):
        res+=func(n,i)*pow(a,i)*pow(b,n-i)
    return res


a=sy.symbols('a')
b=sy.symbols('b')
x=sy.symbols('x')

def main():
    n=8
    res=calc_formula_with(sy.binomial,n)
    print(res)
    print(res.subs({a:4,b:-x}))
    calc_formula_with(binomial,n)
    print(res)
    print(res.subs({a:4,b:-x}))

if __name__ == '__main__':
    main()