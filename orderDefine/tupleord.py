from functools import total_ordering


@total_ordering
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # define operator `==`
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        # define operator `<`
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

p = Point(0, 0)
q = Point(0, 1)
r = Point(1, 1)

print(p < q)
print(q < r)

print(p <= p)
print(p == p)
print(p >= p)

print(q > p)
print(r > q)


defined_methods = set(dir(Point))
print(defined_methods)

convert = {
    '__lt__': [('__gt__', lambda self, other: not (self < other or self == other)),
               ('__le__', lambda self, other: self < other or self == other),
               ('__ne__', lambda self, other: not self == other),
               ('__ge__', lambda self, other: not self < other)],
    '__le__': [('__ge__', lambda self, other: not self <= other or self == other),
               ('__lt__', lambda self, other: self <=
                other and not self == other),
               ('__ne__', lambda self, other: not self == other),
               ('__gt__', lambda self, other: not self <= other)],
    '__gt__': [('__lt__', lambda self, other: not (self > other or self == other)),
               ('__ge__', lambda self, other: self > other or self == other),
               ('__ne__', lambda self, other: not self == other),
               ('__le__', lambda self, other: not self > other)],
    '__ge__': [('__le__', lambda self, other: (not self >= other) or self == other),
               ('__gt__', lambda self, other: self >=
                other and not self == other),
               ('__ne__', lambda self, other: not self == other),
               ('__lt__', lambda self, other: not self >= other)]
}

roots = defined_methods & set(convert)
print(roots)
print(max(roots))
