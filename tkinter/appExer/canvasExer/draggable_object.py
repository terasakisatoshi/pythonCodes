"""
reference:http://www.shido.info/py/tkinter10.html
"""

class DraggableObject():
    def __init__(self,canvas):
        self.canvas=canvas
    def make_binds(self):
        self.canvas.tag_bind(self.id,'<1>', self.on_clicked)
        self.canvas.tag_bind(self.id,'<Button1-Motion>', self.on_motion)

    def on_clicked(self,event):
        self.x=event.x
        self.y=event.y

    def on_motion(self,event):
        x1=event.x
        y1=event.y
        self.canvas.move(self.id, x1-self.x,y1-self.y)
        self.x=x1
        self.y=y1

class Rectangle(DraggableObject):
    def __init__(self, canvas,bx, by, ex, ey, **kwargs):
        super(Rectangle,self).__init__(canvas)
        self.id=self.canvas.create_rectangle(bx,by,ex,ey,**kwargs)
        self.make_binds()

class Elliptic(DraggableObject):
    def __init__(self, canvas,x0, y0, x1, y1, **kwargs):
        super(Elliptic,self).__init__(canvas)
        self.id = self.canvas.create_oval(x0, y0, x1, y1, **kwargs)
        self.make_binds()

class Polygon(DraggableObject):
    def __init__(self, canvas,coords, **kwargs):
        super(Polygon,self).__init__(canvas)
        self.id = self.canvas.create_polygon(coords, **kwargs)
        self.make_binds()

