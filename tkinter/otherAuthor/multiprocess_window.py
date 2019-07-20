"""
How to run a cancellable function when a new Tkinter window opens
https://stackoverflow.com/questions/37669517/how-to-run-a-cancellable-function-when-a-new-tkinter-window-opens
"""
from tkinter import ttk, messagebox, Toplevel, Tk
from tkinter.ttk import Frame, Button
import time
import multiprocessing


def foo():
    for i in range(100):
        print(i)
        time.sleep(0.1)


class TerminatedProcess(Exception):
    def __init__(self, error_str="Process was terminated"):
        self.error_str = error_str


class ProcessWindow(Toplevel):
    """docstring for ProcessWindow"""

    def __init__(self, parent, process):
        super(ProcessWindow, self).__init__(parent)
        self.parent = parent
        self.process = process
        terminate_button = Button(self, text="cancel", command=self.cancel)
        terminate_button.grid(row=0, column=0)
        self.grab_set()  # so you can't push submit multiple times

    def cancel(self):
        self.process.terminate()
        self.destroy()
        raise TerminatedProcess

    def launch(self):
        self.process.start()
        #this blocks mainloop of root
        self.process.join()
        self.destroy()


class MainApp(Frame):
    def __init__(self, parent, *args, **kwargs):
        super(MainApp, self).__init__(parent, *args, **kwargs)
        self.parent = parent
        self.button = Button(self, text="foo", command=self.callback)
        self.button.grid(row=0, column=0)

    def callback(self):
        try:
            proc = multiprocessing.Process(target=foo)
            process_window = ProcessWindow(self, proc)
            process_window.launch()
        except TerminatedProcess as e:
            messagebox.showinfo(title="canceled", message=e.error_str)
        else:
            messagebox.showinfo(message="sucessful run", title="Finished")
        finally:
            pass


def main():
    root = Tk()
    app = MainApp(root, padding=(4))
    app.grid(column=0, row=0)
    root.mainloop()


if __name__ == '__main__':
    main()
