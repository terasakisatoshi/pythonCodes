# -*- coding: UTF-8 -*-
import threading
import Tkinter as Tk
import tkMessageBox
import time

class Application:
    STATE_DONE, STATE_COMPUTING, STATE_ASKING, STATE_CANCELED = range(4)
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("tk_threading.py")
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.run_button = Tk.Button(self.root, text="Run", command=self.run)
        self.run_button.pack(fill=Tk.X)
        self.stop_button = Tk.Button(self.root, text="Stop", command=self.stop,
                                     state=Tk.DISABLED)
        self.stop_button.pack(fill=Tk.X)
        button = Tk.Button(self.root, text="Hello", command=self.hello)
        button.pack(fill=Tk.X)
    def mainloop(self):
        self.state = Application.STATE_DONE
        self.root.mainloop()
        self.root.destroy()
    def quit(self):
        if self.state == Application.STATE_DONE:
            self.root.quit()
    def hello(self):
        print "hello"
    def run(self):
        self.run_button.config(state=Tk.DISABLED)
        self.stop_button.config(state=Tk.NORMAL)
        # 計算スレッドを起動する
        self.state = Application.STATE_COMPUTING
        self.compute_thread = ComputeThread(self)
        self.compute_thread.start()
        self.check_state()
    def stop(self):
        self.state = Application.STATE_CANCELED
    def join(self):
        # 計算スレッドの終了を待つ
        self.compute_thread.join()
        self.stop_button.config(state=Tk.DISABLED)
        self.run_button.config(state=Tk.NORMAL)
    def check_state(self):
        if self.state == Application.STATE_ASKING:
            if tkMessageBox.askyesno("tk_threading.py", "Continue?"):
                self.state = Application.STATE_COMPUTING
                self.compute_thread.event_set()
                self.root.after(100, self.check_state)
            else:
                self.state = Application.STATE_DONE
                self.compute_thread.event_set()
                self.join()
        elif self.state == Application.STATE_DONE:
            self.join()
        else:
            self.root.after(100, self.check_state)

class ComputeThread(threading.Thread):
    def __init__(self, app):
        threading.Thread.__init__(self)
        self.app = app
        self.event = threading.Event()
    def event_set(self): # called by Application
        self.event.set()
    def run(self):
        print "ComputeThread: start"
        for i in range(1, 10):
            if self.app.state == Application.STATE_CANCELED:
                break
            time.sleep(1)
            print i
            if i in [3, 6]:
                self.app.state = Application.STATE_ASKING
                print "ComputeThread: wait"
                self.event.wait()
                if self.app.state == Application.STATE_DONE:
                    break
                print "ComputeThread: continue"
                self.event.clear()
        self.app.state = Application.STATE_DONE
        print "ComputeThread: done"

if __name__ == "__main__":
    app = Application()
    app.mainloop()