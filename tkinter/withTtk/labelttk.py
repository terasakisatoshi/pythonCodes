import tkinter as tk 
from tkinter import ttk 

def main():
    root=tk.Tk()
    framettk=ttk.Frame(root)
    framettk.grid()

    labelttk_left=ttk.Label(
        framettk,
        text="hello",
        background='yellow',
        foreground='#ffffff',
        padding=(5,10))
    labelttk_left.grid(row=1,column=1)

    labelttk_right=ttk.Label(
        framettk,
        text="world",
        background='#ffffff',
        width=20,
        anchor=tk.E,
        padding=(5,10))
    labelttk_right.grid(row=1,column=2)

    root.mainloop()
if __name__ == '__main__':
    main()