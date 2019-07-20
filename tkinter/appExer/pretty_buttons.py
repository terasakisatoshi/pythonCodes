import tkinter as tk
from tkinter import Button
from tkinter import TOP,BOTTOM,RIGHT,LEFT,BOTH
from tkinter import X,Y

def main():
    root=tk.Tk()
    root.geometry("300x200")
    frame=tk.Frame(root)


    Button(frame,text='ALL IS WELL').pack(side=TOP,fill=X)
    Button(frame,text="BACK TO BASICS").pack(side=TOP,fill=X)
    Button(frame,text="CATCH ME IF YOU CAN").pack(side=TOP,fill='x')

    Button(frame,text="LEFT").pack(side=LEFT,fill=BOTH,expand=True)
    Button(frame,text="CENTER").pack(side=LEFT,fill=BOTH,expand=True)
    Button(frame,text='RIGHT').pack(side=LEFT, fill=BOTH,expand=True)
    frame.pack(fill=BOTH,expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()