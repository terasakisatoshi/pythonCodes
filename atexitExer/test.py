import atexit


def func1(*args):
    print("function named {} is called".format(func1.__name__))
    print(args)

def func2(*args):
    print("function named {} is called".format(func2.__name__))
    print(args)

def func3(*args):
    print("function named {} is called".format(func3.__name__))
    print(args)

msg="Bye"

atexit.register(func3,msg)
atexit.register(func2,msg)
atexit.register(func1,msg)


def main():
    print("Hi")
    print("exit main func")


if __name__ == '__main__':
    main()