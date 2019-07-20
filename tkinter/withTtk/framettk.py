"""
reference:
http://python.keicode.com/advanced/tkinter-widget-frame.php
"""

import tkinter as tk
from tkinter import ttk 

"""
relief='sunken','flat'(default), 'raised','groove','ridge'
"""
def main():
    root=tk.Tk()
    framettk=ttk.Frame(root,
        height=200,width=300,
        relief='sunken',
        borderwidth=5)
    framettk.grid()

    root.mainloop()

if __name__ == '__main__':
    main()