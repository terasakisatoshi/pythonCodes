import tkinter as tk
from PIL import Image, ImageTk
from os.path import join, basename, dirname
import random

"""
make class that corresponds to askgoma.py.
very important reference:
https://stackoverflow.com/questions/2223985/tkinter-canvas-does-not-display
    ""
    A reference to the ImageTk instance must be stored somewhere,
    or when your App.__init__() method returns,
    it will be garbage collected,
    and the canvas will not be able to display it.
    (Tkinter does not keep a reference to the image.)
    ""
"""


class App():

    def __init__(self, master, file, ratio=1.0):
        self.file = file
        self.master = master
        self.master.title = basename(self.file)
        self.image = ImageTk.PhotoImage(Image.open(self.file))
        self.ratio = ratio
        self.draw_background()
        self.set_layout()

    def draw_background(self):
        # we must specify width and height as integer
        self.width = int(self.ratio*self.image.width())
        self.height = int(self.ratio*self.image.height())

        self.master.minsize(self.width, self.height)
        # prohibit to resize window
        self.master.resizable(0, 0)

        self.canvas = tk.Canvas(self.master,
                                width=self.width, height=self.height)
        self.canvas.create_image(self.width//2, self.height//2,
                                 image=self.image)
        self.canvas.place(x=0, y=0)

    def set_layout(self):
        self.question_label = tk.Label(text="what do you want ?", bg='white')
        self.question_label.place(x=int(0.3 * self.width), y=int(0.1 * self.height))
        self.question_label.config(font=("Courier", 44))

        self.ask_entry = tk.Entry(width=12, bd=2)
        self.ask_entry.place(x=int(0.1 * self.width), y=int(0.4 * self.height))

        self.ask_button = tk.Button(text="Ask")
        self.ask_button.place(x=int(0.2 * self.width), y=int(0.5 * self.height))
        self.ask_button['command']=self.ask_clicked

        self.answer_label = tk.Label(text=".............", bg="white")
        self.answer_label.place(x=int(0.3 * self.width), y=int(0.8 * self.height))
        self.answer_label.config(font=("Courier",25))
    
    def ask_clicked(self):
        value=self.ask_entry.get()
        if len(value)==0:
            self.answer_label["text"]="キュイ．"
        else:
            ret="キ"
            for _ in value:
                word=["キ","ュ","イ","-","ン"][random.randrange(0, 5)]
                ret+=word
            self.answer_label["text"]=ret

    def mainloop(self):
        self.master.mainloop()


def main():
    root = tk.Tk()
    image_file = "goma.png"
    app = App(root, image_file, ratio=2.5)
    app.mainloop()

if __name__ == '__main__':
    main()
