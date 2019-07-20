import tkinter as tk 
from tkinter import ttk 
from PIL import ImageTk, Image

def main():
    root=tk.Tk()
    root.title('LabelwithIcon')
    framettk=ttk.Frame(root)
    framettk.grid()
    icon = ImageTk.PhotoImage(Image.open('pen.png'))
    pen_label=ttk.Label(
        framettk,
        image=icon)
    pen_label.grid(row=1,column=1)

    s=tk.StringVar()
    s.set("Going Back To School")

    right_label=ttk.Label(
        framettk,
        textvariable=s,
        width=30,
        anchor=tk.W,
        padding=(30,10))
    right_label.grid(row=1,column=2)

    root.mainloop()

if __name__ == '__main__':
    main()