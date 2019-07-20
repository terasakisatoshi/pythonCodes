from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

im = Image.open("image.png")
cropped = im.crop((0, 0, 200, 200))
tk_im = ImageTk.PhotoImage(cropped)
canvas.create_image(250, 250, image=tk_im)

root.mainloop()