import tkinter as tk
root = tk.Tk()
from tkinter import *
import threading
import time


root.geometry("720x100")
root.title("Countdown Tester")

stop = threading.Event()


def reset():
    button["text"] = "Begin Countdown"
    label["text"] = "Countdown Finished"
    label.config(bg='dark red', fg='white')
    label2["text"] = ""
    label2.config(bg='black', fg='white')
    root.timer = root.after(1000, label.update)
    root.update_idletasks()
    stop.set()


def _5():
    label2["text"] = "5"
    label2.config(bg='orange', fg='black')
    root.update_idletasks()
    time.sleep(1)


def _4():
    label2["text"] = "4"
    label2.config(bg='orange', fg='black')
    root.update_idletasks()
    time.sleep(1)


def _3():
    label2["text"] = "3"
    label2.config(bg='orange', fg='black')
    root.update_idletasks()
    time.sleep(1)


def _2():
    label2["text"] = "2"
    label2.config(bg='orange', fg='black')
    root.update_idletasks()
    time.sleep(1)


def _1():
    label2["text"] = "1"
    label2.config(bg='orange', fg='black')
    root.update_idletasks()
    time.sleep(1)


def _0():
    label2["text"] = "0"
    label2.config(bg='orange', fg='black')
    root.update_idletasks()
    time.sleep(1)


def script():
    if not stop.isSet():
        label["text"] = "Countdown Began"
        label.config(bg='blue', fg='white')
        root.update_idletasks()
    if not stop.isSet():
        _5()
    if not stop.isSet():
        _4()
    if not stop.isSet():
        _3()
    if not stop.isSet():
        _2()
    if not stop.isSet():
        _1()
    if not stop.isSet():
        _0()
        reset()


def toggle_text():
    if button["text"] == "Begin Countdown":
        button["text"] = "Stop Countdown"
        label["text"] = "Countdown Began"
        label.config(bg='green', fg='black')
        stop.clear()
        t1 = threading.Thread(target=script)
        t1.daemon = True
        t1.start()
    else:
        button["text"] = "Begin Countdown"
        label["text"] = "Countdown Stopped"
        label.config(bg='red', fg='white')
        label2["text"] = ""
        label2.config(bg='black', fg='white')
        stop.set()
    root.update_idletasks()


def on_exit():
    root.destroy()


canvas = Canvas(width=720, height=100, bg='black')
canvas.grid(rowspan=26, columnspan=20, sticky='W,E,N,S')


button = Button(root, text="Begin Countdown", font='-weight bold', width=17, command=toggle_text)
button.grid(padx=10, pady=10, row=10, column=0, sticky='W,E,N,S')
button2 = Button(root, text="   Quit   ", font='-weight bold', command=on_exit)
button2.grid(padx=5, pady=10, row=10, column=1, sticky='W,E,N,S')

label = Label(root, text=" ", width=20, font='-weight bold', background='black')
label.grid(padx=5, pady=10, row=10, column=2, sticky='W,E,N,S')
label2 = Label(root, text=" ", width=11, font='-weight bold', background='black')
label2.grid(padx=5, pady=10, row=10, column=3, sticky='W,E,N,S')


root.resizable(width=FALSE, height=FALSE)

root.mainloop()