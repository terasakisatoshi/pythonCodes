cdef public struct Point:
    double x
    double y

cdef public Point DoubleCoord(Point p):
    cdef Point q
    q.x=2*p.x
    q.y=2*p.y
    return q