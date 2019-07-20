#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This script shows a simple window
on the screen.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from tkinter import Tk, Frame, BOTH


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
      
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        

def main():
  
    root = Tk()
    #The geometry() method sets a size for the window and positions it on the screen. The first two parameters are the width and height of the window. The last two parameters are x and y screen coordinates.
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()