"""
Reference:
Why your GUI app freezes
 http://stupidpythonideas.blogspot.com/2013/10/why-your-gui-app-freezes.html
"""
import tkinter as tk
import time
"""
Imagine a simple Tkapp.
(Everything is pretty much the same for most other GUI frameworks, and many frameworks for games and network servers,
and even things like SAX parsers, but most novices first run into this with GUI apps,
and Tkinter is easy to explore because it comes with Python.)
"""

"""
def handle_click():
    print("Clicked")

root = tk.Tk()
tk.Button(root, text="Click me", command=handle_click).pack()
root.mainloop()
"""

"""
Now Imagine that, instead of just printing a message, you want it to pop
up a window, wait 5 seconds, then close the window. You might try to write this:

root = tk.Tk()

def handle_click():
    win = tk.Toplevel(root)
    win.transient()
    tk.Label(win, text="Please wait...").pack()
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    win.destroy()

tk.Button(root, text="Click me", command=handle_click).pack()
root.mainloop()


But when you click the button, the window does not show up.
And the mainwindows freezes up and beachballs for 5 seconds

This is because you event handler has not returned, so the main loop cannot process any event.
It needs to process event to display a new window,
respond to messages from the OS, etc., and you are not letting is.
"""

"""
There are two basic ways around this problem: callbacks, or threads.
There are advantages and disadvantages of both. And then there are various
ways of building thread-like functionality on top of callbacks, which let you
get (part of) the best of both worlds, but I will get to those in another post
(http://stupidpythonideas.blogspot.com/2013/10/solving-callbacks-for-python-guis.html)
"""

"""
Your event handler has to return in a fraction of a second.
But what if you still have code to run? You have to
reorganize your code: Do some setup,
then schedule the rest of the code to run later.
 And that "rest of the code" is also an event handler,
  so it also has to return in a fraction of a second,
   which means often it will have to do a bit of work and again
    schedule the rest to run later.

Depending on what you're trying to do, you may want to run on a timer,
or whenever the event loop is idle,
or every time through the event loop no matter what.
In this case, we want to run once/second.
In Tkinter, you do this with the after method:

root = tk.Tk()


def handle_click():
    win = tk.Toplevel(root)
    win.transient()
    tk.Label(win, text='Please wait...').pack()
    i = 5

    def callback():
        nonlocal i, win
        print(i)
        i -= 1
        if not i:
            win.destroy()
        else:
            root.after(1000, callback)
    root.after(1000, callback)

tk.Button(root, text="Click me", command=handle_click).pack()
root.mainloop()
"""

"""
For a different example, imagine we just have some processing that takes a few
seconds because it has so much work to do.
We will do something stupid and simple

def handle_click():
    tot = sum(range(100000))
    label.config(text=tot)
root = tk.Tk()
tk.Button(root, text='add it up', command=handle_click).pack()
label = tk.Label(root)
label.pack()
root.mainloop()

When you click the button, the whole app will freeze up for a few seconds
as Python calculates that sum. So, what we want to do is break it up into chunks:

def handle_click():
    total = 0
    i = 0

    def callback():
        nonlocal i, total
        total += sum(range(i * 100000, (i + 1) * 100000))
        i += 1
        if i == 100:
            label.config(text=total)
        else:
            root.after_idle(callback)
    root.after_idle(callback)

root = tk.Tk()
tk.Button(root, text='add it up', command=handle_click).pack()
label = tk.Label(root)
label.pack()
root.mainloop()

While callback definitely work, there are lot of problem with them
First, we have turned out control flow inside-out. Compare the simple for loop
to the chain of callbacks that append it. And it gets much worse when you have more complicated code.

On top of that, it's very easy to get lost in a callback chain. If you forgot to schedule the next callback,
the operation never finishes
"""

"""
Another option is a hybrid approach: 
Do your GUI stuff in the main thread, 
and your I/O in a second thread. 
Both of them can still be callback-driven, 
and you can localize all of the threading problems 
to the handful of places where the two have to 
interact with each other.
"""

"""
Threading:
with with multithreading, we do not have to recognize out code at all, we just move 
all of the work onto a thread:

import threading


def handle_click():
    def callback():
        total = sum(range(100000000))
        print(total)
    t = threading.Thread(target=callback)
    t.start()
root = tk.Tk()
tk.Button(root, text='clickme', command=handle_click).pack()
root.mainloop()
"""


import threading


def handle_click():
    def callback():
        total = sum(range(100000000))
        root.on_main_thread(lambda: label.config(text=total))
    t = threading.Thread(target=callback)
    t.start()
root = tk.Tk()
tk.Button(root, text='clickme', command=handle_click).pack()
root.mainloop()
