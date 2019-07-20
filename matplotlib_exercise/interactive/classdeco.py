from re import search
from functools import wraps


def is_match(_lambda, pattern):
    def wrapper(f):
        @wraps(f)
        def wrapped(self, *f_args, **f_kwargs):
            if callable(_lambda) and search(pattern, (_lambda(self) or '')):
                f(self, *f_args, **f_kwargs)
        return wrapped
    return wrapper


class MyTest(object):

    def __init__(self):
        self.name = 'foo'
        self.surname = 'bar'

    @is_match(lambda x: x.name, 'foo')
    @is_match(lambda x: x.surname, 'foo')
    def my_rule(self):
        print('my_rule : ok')

    @is_match(lambda x: x.name, 'foo')
    @is_match(lambda x: x.surname, 'bar')
    def my_rule2(self):
        print('my_rule2 : ok')


test = MyTest()
test.my_rule()
test.my_rule2()
