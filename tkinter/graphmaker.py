import matplotlib
matplotlib.use('TkAgg')

from numpy import arange
from numpy import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

from matplotlib.figure import Figure 

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def draw():
    def on_key_event(event):
        print('you pressed %s' % event.key)
        key_press_handler(event, canvas, toolbar)
    
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    x = arange(0.0, 3.0, 0.01)
    y=eval(entry.get()+"(x)")
    ax.set_title(entry.get())
    ax.plot(x, y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    canvas.mpl_connect('key_press_event', on_key_event)

    

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

root = Tk.Tk()
root.title("Embedding in TK")

entry=Tk.Entry(master=root)
entry.pack()

button_quit = Tk.Button(master=root, text='Quit', command=_quit)
button_quit.pack(side=Tk.BOTTOM)
button_draw=Tk.Button(master=root,text='Draw',command=draw)
button_draw.pack(side=Tk.BOTTOM)


root.mainloop()

