from functools import wraps

def hello(function):
    def _hello(*args,**kargs):
        result=function(*args,**kargs) 
        return "hello, {}".format(result)
    return _hello

@hello
def name(args):
    """my docstring"""
    return args

def ask_func_name():
    print(name('John doe'))
    print(name.__name__)
    print(name.__doc__)

def hello_with_functools(function):
    @wraps(function)
    def _hello(*args,**kargs):
        result=function(*args,**kargs) 
        return "hello, {}".format(result)
    return _hello

@hello_with_functools
def name_with_functools(args):
    """my docstring"""
    return args

def ask_func_name_with_functools():
    print(name_with_functools('John doe'))
    print(name_with_functools.__name__)
    print(name_with_functools.__doc__)



    

def main():
    ask_func_name()
    ask_func_name_with_functools()



if __name__ == '__main__':
    main()