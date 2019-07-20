import tkinter as tk 
"""
Sync word buffer between reference and target Entries
"""

from tkinter import Entry, Label

class EntryTraceer():
    def __init__(self,root):
        self.root=root
        self.create_view()

    def create_view(self):

        buf=tk.StringVar()
        Label(self.root,text="Reference").grid(row=0,sticky=tk.W)
        self.reference_entry=Entry(self.root,textvariable=buf)
        self.reference_entry.grid(row=0,column=1,sticky=tk.E)
        
        Label(self.root,text='Target').grid(row=1,sticky=tk.W)
        target_entry=Entry(self.root,textvariable=buf)
        target_entry.grid(row=1,column=1,sticky=tk.E)
        self.target_entry=target_entry

        print(dir(self.target_entry))

    def mainloop(self):
        self.root.mainloop()

def main():
    root=tk.Tk()
    app = EntryTraceer(root)
    app.mainloop()

if __name__ == '__main__':
    main()