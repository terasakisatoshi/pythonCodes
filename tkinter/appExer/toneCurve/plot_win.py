import tkinter as tk 
from tkinter import Frame, Button, PanedWindow, Text
from tkinter import X, Y, BOTH

import numpy as np 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from tone_curve import CurveBrowser

"""
note
if you will distribute others to whom you want not disclose this scripts
try to use 'pyinstaller' module
Usage Part 1.
install python 3.4 (many developer say it does not work well on python 3.5 )
so please make vertual environments
> conda create -n installenv python=3.4 numpy matplotlib scipy
Usage Part 2.
then activate installenv
> activate installenv
Usage Part 3.
build python code into .exe form
(installenv) > pip install pyinstaller
(installenv) > pyinstaller plot_win.py --onefile --noconsole

Remark
when run plot_win.exe I can't initialize this app and occur error
'fail to run script plot_win'
I had some experiments and found that image reading library disturbs 
initializing this app e.g.
from scipy.misc import imread
from PIL import Image
but opencv library cv2 works!!!!!!
"""
from scipy.misc import imread

class ImageViewer(object):
    def __init__(self,root):
        self.root=root
        self.fig,self.ax=plt.subplots()
        self.img=imread('test1.bmp',0)
        self.draw_zone=self.ax.imshow(self.img,'gray')
        plot_frame=Frame(self.root)
        self.root.add(plot_frame)
        canvas=FigureCanvasTkAgg(self.fig,master=plot_frame)
        toolbar = NavigationToolbar2TkAgg(canvas, plot_frame)
        toolbar.update()
        self.canvas=canvas       

class ToneCurve(CurveBrowser):
    def __init__(self,fig,ax,listener):
        super(ToneCurve, self).__init__(fig,ax)
        self.listener=listener

    def notify(self):
        tone_curve=self.tone_curve
        toned=tone_curve(self.listener.img)
        self.listener.draw_zone.set_data(toned)
        self.listener.fig.canvas.draw()


class ToneCurveViewer(object):
    def __init__(self,root,listener=None):
        self.root=root
        fig,ax=plt.subplots(figsize=(6,6))
        self.ax=ax
        self.ax.set_xlim([0,255])
        self.ax.set_ylim([0,255])
        browser=ToneCurve(fig,self.ax,listener)

        plot_frame=Frame(self.root)
        self.root.add(plot_frame)
        canvas=FigureCanvasTkAgg(fig,master=plot_frame)
                
        canvas.mpl_connect('pick_event',browser.onpick)
        canvas.mpl_connect('motion_notify_event',browser.on_motion)
        #both bind is very important for release event but I do not know why
        canvas._tkcanvas.bind('button_release_event',browser.on_release)
        canvas.mpl_connect('button_release_event', browser.on_release)

        toolbar = NavigationToolbar2TkAgg(canvas, plot_frame)
        toolbar.update()
        self.canvas=canvas  
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def main():
    root=tk.Tk()
    pack_windows(root)
    root.protocol("WM_DELETE_WINDOW")
    root.mainloop()

def pack_windows(root):
    main_paned_window = PanedWindow(root)
    main_paned_window.pack(fill=BOTH, expand=True)

    tone_paned_window=PanedWindow(relief=tk.GROOVE,bd=3,orient=tk.VERTICAL)
    main_paned_window.add(tone_paned_window)
    
    sub_tone_paned_window=PanedWindow(tone_paned_window)
    tone_paned_window.add(sub_tone_paned_window)
    
    plot_window=PanedWindow()
    main_paned_window.add(plot_window)
    plot_window=ImageViewer(plot_window)
    plot_window.canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)

    tone_window=ToneCurveViewer(sub_tone_paned_window,plot_window)
    tone_window.canvas.get_tk_widget().pack(fill=tk.BOTH,expand=True)
    space_frame=Frame()
    tone_paned_window.add(space_frame)
    
    button=Button(space_frame,text="something")
    button.pack()

    def quit_app():
        root.quit()
        root.destroy()

    quitbutton=Button(space_frame,text="exit",command=quit_app)
    quitbutton.pack()

if __name__ == '__main__':
    main()