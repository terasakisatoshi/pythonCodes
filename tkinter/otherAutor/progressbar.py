"""
Reference: 
tkinter_progress.py
https://gist.github.com/MattWoodhead/c7c51cd2beaea33e1b8f5057f7a7d78a
"""

import threading
import tkinter as tk
from tkinter import ttk


class ProgressBar():
    """ threaded progress bar for tkinter gui"""

    def __init__(self, parent, row, column, columnspan):
        self.maximum = 100
        self.interval = 10
        self.progressbar = ttk.Progressbar(parent,
                                           orient=tk.HORIZONTAL,
                                           mode="indeterminate",
                                           maximum=self.maximum)
        self.progressbar.grid(row=row, column=column,
                              columnspan=columnspan, sticky="we")
        self.thread = threading.Thread(
            target=self.progressbar.start(self.interval), args=())
        self.thread.start()

    def start_progressbar(self):
        if not self.thread.isAlive():
            v = self.progressbar["value"]
            self.progressbar.configure(mode="indeterminate",
                                       maximum=self.maximum,
                                       value=v)
            self.progressbar.start()

    def stop_progressbar(self):
        if not self.thread.isAlive():
            v = self.progressbar["value"]
            self.progressbar.stop()
            self.progressbar["value"] = v

    def clear_progressbar(self):
        if not self.thread.isAlive():
            self.progressbar.stop()
            self.progressbar.configure(mode="determinate", value=0)

    def complete_progressbar(self):
        if not self.thread.isAlive():
            self.progressbar.stop()
            self.progressbar.configure(mode="determinate",
                                       maximum=self.maximum,
                                       value=self.maximum)


def print_message():
    print("proof a separate thread is running")


class AppGUI(tk.Frame):
    """class to define tkinter GUI"""

    def __init__(self, parent):
        super(AppGUI, self).__init__(master=parent)
        progressbar = ProgressBar(parent, row=0, column=0, columnspan=2)
        start_button = ttk.Button(
            parent, text="start", command=progressbar.start_progressbar)
        start_button.grid(row=1, column=0)

        stop_button = ttk.Button(
            parent, text="stop", command=progressbar.stop_progressbar)
        stop_button.grid(row=1, column=1)

        complete_button = ttk.Button(
            parent, text="complete", command=progressbar.complete_progressbar)
        complete_button.grid(row=2, column=0)

        clear_button = ttk.Button(
            parent, text="clear", command=progressbar.clear_progressbar)
        clear_button.grid(row=2, column=1)

        test_print_button = ttk.Button(
            parent, text="thread test", command=print_message)
        test_print_button.grid(row=3, column=0, columnspan=2, sticky="we")


def main():
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
