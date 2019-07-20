def deco_with_arg(*deco):
    def deco_func(func):
        def wrap(self, *arg, **kwargs):
            print('darg', deco)
            res = func(self, *arg, **kwargs)
            return arg, kwargs
        return wrap
    return deco_func


class Hoge():

    @deco_with_arg('hi')
    def test(self, *args, **kwargs):
        return args

hoge = Hoge()
print(hoge.test('msg', a='b'))
