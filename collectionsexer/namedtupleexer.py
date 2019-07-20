from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(x=3, y=5)
print(p, p.x, p.y)
