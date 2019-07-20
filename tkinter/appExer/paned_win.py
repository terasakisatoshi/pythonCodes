import tkinter as tk 
from tkinter import Frame, Button, PanedWindow, Text
from tkinter import X, Y, BOTH

import numpy as np 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import pyplot as plt

class MatplotlibWindow(object):
    def __init__(self,root):
        self.root=root
        fig,ax=plt.subplots()
        xs=np.arange(-np.pi,np.pi,0.001)
        ys=np.sin(xs)
        ax.plot(xs,ys)
        plot_frame=Frame(self.root)
        self.root.add(plot_frame)
        canvas=FigureCanvasTkAgg(fig,master=plot_frame)
        toolbar = NavigationToolbar2TkAgg(canvas, plot_frame)
        toolbar.update()
        self.canvas=canvas       

class MatplotlibWindow2(object):
    def __init__(self,root):
        self.root=root
        fig,ax=plt.subplots()
        xs=np.arange(-np.pi,np.pi,0.001)
        ys=np.cos(xs)
        ax.plot(xs,ys)
        plot_frame=Frame(self.root)
        self.root.add(plot_frame)
        canvas=FigureCanvasTkAgg(fig,master=plot_frame)
        toolbar = NavigationToolbar2TkAgg(canvas, plot_frame)
        toolbar.update()
        self.canvas=canvas   

def main():
    root=tk.Tk()

    main_paned_window = PanedWindow(root)
    main_paned_window.pack(fill=BOTH, expand=1)

    tone_curve_paned_window=PanedWindow(main_paned_window)
    main_paned_window.add(tone_curve_paned_window)
    
    tone_curve_window=PanedWindow(tone_curve_paned_window,relief=tk.GROOVE,bd=3,orient=tk.VERTICAL)
    mlp_tone_curve_window=MatplotlibWindow2(tone_curve_window)
    mlp_tone_curve_window.canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)

    #text_panel_left = Text(main_paned_window, height=6, width =15,relief=tk.GROOVE,bd=2)
    #main_paned_window.add(text_panel_left)

    sub_paned_window = PanedWindow(main_paned_window, orient=tk.VERTICAL)

    #plot sin curve
    plot_paned_window=PanedWindow(sub_paned_window,relief=tk.GROOVE,bd=3,orient=tk.VERTICAL)
    mlp_window=MatplotlibWindow(plot_paned_window)
    mlp_window.canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)


    main_paned_window.add(sub_paned_window)
    bottom_pane_text = Text(sub_paned_window, height=3, width =3, relief=tk.SUNKEN,bd=2)
    
    sub_paned_window.add(plot_paned_window)
    sub_paned_window.add(bottom_pane_text)




    button=Button(root,text="Hello")
    button.pack()

    root.mainloop()
if __name__ == '__main__':
    main()