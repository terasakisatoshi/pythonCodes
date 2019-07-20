import sys
import tkinter

root=tkinter.Tk()
root.title("software Title")
#define window size
root.geometry("400x300")


label=tkinter.Label(text='entry1')
label.place(x=60,y=100)

editbox1=tkinter.Entry()
editbox1.insert(tkinter.END,"insert words")
editbox1.place(x=100,y=100)

label=tkinter.Label(text='entry2')
label.place(x=60,y=130)

editbox2=tkinter.Entry()
editbox2.place(x=100,y=130)

def write_word(event):
    editbox2.insert(tkinter.END,editbox1.get())

button=tkinter.Button(text="copy entry1 -> entry2",width=50)
button.bind("<Button-1>",write_word)
button.pack()

def clear_word(event):
    editbox1.delete(0,tkinter.END)
    editbox2.delete(0,tkinter.END)

button2=tkinter.Button(text="clear",width=50)
button2.bind("<Button-1>",clear_word)
button2.pack()

def exit_program(event):
    exit()

button3=tkinter.Button(text="Exit",width=50)
button3.bind("<Button-1>",exit_program)
button3.pack()

root.mainloop()