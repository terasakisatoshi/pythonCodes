from functools import wraps

def deco(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        return res
    return wrapper

@deco
def test(str):
    """my doc"""
    return str
def deco_test():
    print(test("hello world with deco"))
    print(test.__name__)
    print(test.__doc__)

def deco_with_args(*deco_args):
    def deco(func):
        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            return deco_args,res
        return wrapper
    return deco

@deco_with_args("hoge")
def test(str):
    """my doc"""
    return str

def main():
    print(test("hello"))
if __name__ == '__main__':
    main()