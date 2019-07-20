import tkinter as tk 
from draggable_object import DraggableObject, Rectangle, Elliptic, Polygon
import random

COLOR = ['red', 'gold', 'blue']


class CanvasFrame(tk.Frame):
    def __init__(self,master=None):
        super(CanvasFrame, self).__init__(master)

        self.pack(fill=tk.BOTH, expand=True)
        
        self.canvas=tk.Canvas(
            self,
            scrollregion=("0c","0c","40c","40c"),
            width="20c",
            height="20c",
            relief=tk.SUNKEN, borderwidth=2,background='#FFEFD5')
        self.canvas.grid(
            row=0,
            column=0, 
            sticky=tk.N+tk.E+tk.W+tk.S)   
        xscroll=tk.Scrollbar(
            self, 
            orient=tk.HORIZONTAL, 
            command=self.canvas.xview)
        xscroll.grid(row=1,column=0,sticky=tk.E+tk.W)
        yscroll=tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        yscroll.grid(row=0,column=1,sticky=tk.N+tk.S)

        self.canvas.config(
            xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set)

        self.grid_rowconfigure(0,weight=1, minsize=0)
        self.grid_columnconfigure(0,weight=1,minsize=0)
            

class CanvasApp(CanvasFrame):
    def __init__(self,master=None):
        super(CanvasApp,self).__init__(master)
        
        self.master.title("White canvas")
        self.master.geometry('+20+20') 
        self.draghandler=DraggableObject(self.canvas)
        x=random.randint(100, 1700) * 0.01
        y=random.randint(300, 1500) * 0.01
        w=random.randint(50, 150) * 0.01
        h=random.randint(50, 150) * 0.01
        c=random.randint(0,2)
        r=0.2
        Elliptic(
            self.draghandler.canvas,
            '%fc' % (x-r), '%fc' % (y-r), '%fc' % (x+r), '%fc' % (y+r),
            width=1, outline='blue', fill='blue')
        Polygon(
            self.draghandler.canvas,
            [150,75,225,0,300,75,225,150],
            outline='blue', fill='white',width=1)

        Rectangle(
            self.draghandler.canvas,
            '%fc' % (x), '%fc' % (y), '%fc' % (x+w), '%fc' % (y+h),
            outline=COLOR[0],fill=None, width=1)
def main():
    root=tk.Tk()
    
    app1=CanvasApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()