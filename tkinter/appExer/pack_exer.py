import tkinter as tk 
from tkinter import Frame, Button, Label
from tkinter import TOP, BOTTOM, RIGHT, LEFT, BOTH, NONE, X, Y


def main():
    root=tk.Tk()
    frame=Frame(root)

    Label(frame,text="Pack Demo of side and fill").pack()
    Label(frame,text="LEFT FILL Y").pack(side=LEFT,fill=Y)
    Label(frame,text="TOP FILL X").pack(side=TOP, fill=X)
    Label(frame,text="RIGHT FILL NONE").pack(side=RIGHT,fill=NONE)
    Label(frame,text="TOP FILL BOTH").pack(side=TOP, fill=BOTH)

    frame.pack()

    Label(root,text="Pack Demo of expand").pack()
    Button(root,text="I do not expand").pack()
    Button(root,text='I do not fill x but I expand').pack(expand=tk.YES)
    Button(root,text="I fill x and expand").pack(fill=X, expand=1)

    root.mainloop()



if __name__ == '__main__':
    main()