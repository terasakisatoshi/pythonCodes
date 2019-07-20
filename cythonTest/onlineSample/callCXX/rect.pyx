cdef extern from "src/rectangle.h" namespace "shapes":
    cdef cppclass Rectangle:
        Rectangle(int,int,int,int) except +
        int x_min,y_min,x_max,y_max
        int getLength()
        int getHeight()
        int getArea()
        void move(int,int)

cdef class PyRectangle:
    cdef Rectangle *thisptr # ラップ対象の C++ インスタンスを保持する
    def __cinit__(self, int x_min, int y_min, int x_max, int y_max):
        self.thisptr = new Rectangle(x_min, y_min, x_max, y_max)
    def __dealloc__(self):
        del self.thisptr
    def get_coord(self):
        return self.thisptr.x_min,self.thisptr.y_min,self.thisptr.x_max,self.thisptr.y_max
    def get_length(self):
        return self.thisptr.getLength()
    def get_height(self):
        return self.thisptr.getHeight()
    def get_area(self):
        return self.thisptr.getArea()
    def move(self, dx, dy):
        self.thisptr.move(dx, dy)