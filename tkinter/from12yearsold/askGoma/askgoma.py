import tkinter as tk
from PIL import Image, ImageTk
from os.path import join, basename, dirname
"""
reference:
https://stackoverflow.com/questions/36025267/how-to-find-out-size-of-a-photoimage-in-tkinter
https://ameblo.jp/hitochan007/entry-12014898453.html
"""

def main():
    root = tk.Tk()

    image_file = basename("goma.png")
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
