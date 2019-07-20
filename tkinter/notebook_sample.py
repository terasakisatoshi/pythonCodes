import tkinter as tk 
from tkinter import Frame
from tkinter import ttk 


def main():
    root=tk.Tk()
    root.geometry('300x400')
    note=ttk.Notebook(root)
    note.pack(fill=tk.BOTH,expand=True)
    frame1=Frame(note)
    frame2=Frame(note)
    note.add(frame1,text='frame1')
    note.add(frame2,text='frame2')

    root.mainloop()

if __name__ == '__main__':
    main()