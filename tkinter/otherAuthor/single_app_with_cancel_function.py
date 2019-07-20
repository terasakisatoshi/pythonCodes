import multiprocessing
from multiprocessing import Queue
import threading
import time
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button, Frame
import logging
logging.basicConfig(level=logging.DEBUG)


class CalculationProcess(multiprocessing.Process):
    def __init__(self, result_queue):
        super(CalculationProcess, self).__init__()
        self.result_queue = result_queue

    def run(self):
        self.calculate_something()
        self.is_finish = True

    def calculate_something(self):
        s = 0
        for i in range(100):
            s += i
            logging.info(s)
            time.sleep(0.05)
        self.result_queue.put(s)


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.button = Button(self, text="start", command=self.callback)
        self.cancel = Button(self, text="cancel", command=self.cancel)

        self.button.grid(row=0, column=0)
        self.cancel.grid(row=0, column=1)

        self.is_canceled = False

    def check_status(self):
        if self.proc.is_alive():
            self.after(100, self.check_status)
        elif self.is_canceled:
            messagebox.showinfo(message="canceled")
        else:
            messagebox.showinfo(message="finished" +
                                int(self.result_queue.get()))

    def callback(self):
        self.result_queue = Queue()
        self.proc = CalculationProcess(self.result_queue)
        self.proc.start()
        self.after(10, self.check_status)

    def cancel(self):
        self.is_canceled = True
        self.proc.terminate()
        # messagebox.showinfo(message="Cancelled")


def main():
    root = tk.Tk()
    my_app = MainApplication(root, padding=(4))
    my_app.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
