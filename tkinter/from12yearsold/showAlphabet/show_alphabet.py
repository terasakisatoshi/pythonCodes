import tkinter as tk 
from PIL import Image, ImageTk
import os
from os.path import join,dirname,basename

def main():
    root = tk.Tk()

    image_file = basename("test.png")
    root.title(image_file)

    image = Image.open(image_file)
    image = ImageTk.PhotoImage(image)

    root_width = image.width()
    root_height = image.height()
    root.minsize(root_width, root_height)

    canvas = tk.Canvas()
    canvas.place(x=0, y=0)
    canvas.create_image(root_width//2, root_height//2, image=image)

    root.resizable(0, 0)
    root.mainloop()

if __name__ == '__main__':
    main()