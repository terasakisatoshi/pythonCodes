# -*- coding: UTF-8 -*-
import threading
import tkinter as tk 
from tkinter import messagebox as tkmsg
import time

class Application:
    STATE_DONE,STATE_COMPUTING,STATE_ASKING,STATE_CANCELED=0,1,2,3
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("tk_threading")
        self.root.protocol("WM_DELETE_WINDOW",self.quit)
        self.run_button=tk.Button(self.root,text="Run",command=self.run)
        self.run_button.pack(fill=tk.X)
        self.stop_button=tk.Button(self.root,text="Stop",command=self.stop,state=tk.DISABLED)
        self.stop_button.pack(fill=tk.X)
    def mainloop(self):
        self.state=Application.STATE_DONE
        self.root.mainloop()
        self.root.destroy()
    def quit(self):
        if self.state==Application.STATE_DONE:
            self.root.quit()
    def run(self):
        self.run_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        #initialize computing thread
        self.state=Application.STATE_COMPUTING
        self.compute_thread=ComputeThread(self)
        self.compute_thread.start()
        self.check_state()
    def stop(self):
        self.state=Application.STATE_ASKING
    def join(self):
        self.compute_thread.join()
        self.stop_button.config(state=tk.DISABLED)
        self.run_button.config(state=tk.NORMAL)
    def check_state(self):
        if self.state==Application.STATE_ASKING:
            if tkmsg.askokcancel("Remark","Are you sure want to stop the application?"):
                self.state=Application.STATE_CANCELED
                self.compute_thread.event_set()
                self.join()
            else :
                self.state=Application.STATE_COMPUTING
                self.compute_thread.event_set()
                self.root.after(100,self.check_state)
        elif self.state==Application.STATE_DONE:
            self.join()
        else:
            self.root.after(100,self.check_state)

class ComputeThread(threading.Thread):
    def __init__(self,app):
        threading.Thread.__init__(self)
        self.app=app
        self.event=threading.Event()
    def event_set(self):
        self.event.set()
    def run(self):
        print("Start run ComputeThread")
        for i in range(1,10):
            time.sleep(1)
            print(i)
            if self.app.state==Application.STATE_ASKING:
                print("ComputeThread wait")
                self.event.wait()
                if self.app.state==Application.STATE_CANCELED:
                    print("break")
                    break
                else :
                    print("restart ComputeThread")
                    self.event.clear()
        self.app.state=Application.STATE_DONE
        print("finish run ComputeThread")

def main():
    app=Application()
    app.mainloop()

if __name__ == '__main__':
    main()