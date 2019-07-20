import tkinter as tk 
from tkinter import messagebox
import sys

def main():
    application=tk.Tk()
    application.withdraw()
    def call_back():
        if messagebox.askokcancel("Quit???","Do you like to quit??"):
            application.destroy()
    application.protocol("WM_DELETE_WINDOW",call_back)
    application.deiconify()
    application.mainloop()

if __name__ == '__main__':
    main()