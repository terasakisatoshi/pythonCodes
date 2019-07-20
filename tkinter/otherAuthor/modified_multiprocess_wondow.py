"""
Perhaps you are looking for something like this:

"""
from tkinter import ttk, messagebox, Toplevel, Tk
import time
import multiprocessing
import logging
logging.basicConfig(level=logging.DEBUG)

def foo():
    for i in range(100):
        logging.info("i={}".format(i))
        time.sleep(0.1)


class ProcessWindow(Toplevel):
    def __init__(self, parent, process):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.process = process

        terminate_button = ttk.Button(self, text="Cancel", command=self.cancel)
        terminate_button.grid(row=0, column=0)

        self.grab_set()  # so you can't push submit multiple times

    def cancel(self):
        self.process.terminate()
        self.destroy()
        messagebox.showinfo(title="Cancelled",
                            message='Process was terminated')

    def launch(self):
        self.process.start()
        # Starting the loop to check when the process is going to end
        self.after(10, self.isAlive)

    def isAlive(self):
        if self.process.is_alive():                     # Process still running
            self.after(100, self.isAlive)               # Going again...
        elif self:
            # Process finished
            messagebox.showinfo(message="sucessful run", title="Finished")
            self.destroy()


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.button = ttk.Button(self, text="foo", command=self.callback)
        self.button.grid(row=0, column=0)

    def callback(self):
        proc = multiprocessing.Process(target=foo)
        process_window = ProcessWindow(self, proc)
        process_window.launch()


def main():
    root = Tk()
    my_app = MainApplication(root, padding=(4))
    my_app.grid(column=0, row=0)
    root.mainloop()


if __name__ == '__main__':
    main()
