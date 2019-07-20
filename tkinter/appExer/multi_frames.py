import tkinter as tk 
from tkinter import Button, Frame, PanedWindow
from tkinter import TOP, BOTTOM, RIGHT, LEFT
from tkinter import X, Y, BOTH

import numpy as np 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import pyplot as plt

def main():
    root=tk.Tk()
    #top frame configuration
    

    fig,ax=plt.subplots()
    xs=np.arange(-np.pi,np.pi,0.001)
    ys=np.sin(xs)
    ax.plot(xs,ys)

    plot_window=PanedWindow(root)

    canvas=FigureCanvasTkAgg(fig,master=plot_window)
    canvas.get_tk_widget().pack(side=TOP,fill=BOTH,expand=True)

    toolbar = NavigationToolbar2TkAgg(canvas, plot_window)
    toolbar.update()

    top_frame=Frame(root,)
    left_frame=Frame(root, relief=tk.SUNKEN,bd=4)
    bottom_frame=Frame(root)

    left_frame.pack(side=LEFT,fill=BOTH,expand=False)
    
    plot_window.pack(side=TOP,fill=BOTH,expand=True)
    top_frame.pack(side=TOP,fill=X,expand=False)
    bottom_frame.pack(side=TOP,fill=X,expand=False)

    Button(top_frame,text="top left button").pack(side=LEFT, fill=X, expand=True)
    Button(top_frame,text="top right button").pack(side=LEFT,fill=X,expand=True)
    #left frame configuration

    Button(left_frame,text="left button 1").pack(side=TOP,ipady=90,fill=X,anchor=tk.N, expand=True)
    Button(left_frame,text="left button 2").pack(side=TOP,ipady=90,fill=X,anchor=tk.N, expand=True)

    #right frame configuratioion

    Button(bottom_frame,text="right button 1").pack(side=TOP, fill=BOTH, expand=True)
    Button(bottom_frame,text="right button 2").pack(side=TOP, fill=BOTH, expand=True)    


    root.mainloop()

if __name__ == '__main__':
    main()

