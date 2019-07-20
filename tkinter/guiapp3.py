import tkinter as tk 
from tkinter import scrolledtext as st
import subprocess
import threading


class SubprocessThread(threading.Thread):
    def __init__(self,app,cmd):
        threading.Thread.__init__(self)
        self.cmd=cmd
        self.app=app
        self.stop_event=threading.Event()

    def run(self):
        def get_line(cmd):
            proc=subprocess.Popen(self.cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            while True:
                line=proc.stdout.readline()
                if line:
                    yield line.decode('utf-8')

                if not line and proc.poll() is not None:
                    break
        
        while not self.stop_event.is_set():
            """
            this tech is reffered from
            http://nobunaga.hatenablog.jp/entry/2016/06/03/204450
            """
            for line in get_line(self.cmd):
                print(line)
                self.app.scroll_text.insert("end",line)
            print('end')

    def stop(self):
        self.stop_event.set()


def button2():
    pass
def button3():
    pass
def button4():
    pass
def hisdel():
    pass
def saveas():
    pass
class Application:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("title")
        self.root.protocol("WM_DELETE_WINDOW",self.quit)
        label_application = tk.Label(self.root, text="MyApplication.org", font=('Times', '12'),anchor=tk.E,width=20)
        label_application.grid(row=0,column=1,columnspan=5,sticky=tk.E,padx=5, pady=5)
        #テキストエリア
        self.scroll_text=st.ScrolledText(self.root, font=('Times', '10'))
        self.scroll_text.grid(row=1,column=0,columnspan=5,sticky=tk.W+tk.E,padx=5, pady=5)
        #ラベル（コメント）
        msg="コマンドを入力し、選択した部分を実行します。実行は「F1」、「右クリック」、「実行ボタン」"
        label_description = tk.Label(self.root, text=msg, font=('Times', '9'),anchor=tk.W)
        label_description.grid(row=2,column=0,columnspan=5,sticky=tk.W+tk.E,padx=5, pady=5)
        #テキストエリア（入力用）
        self.cmd_text = st.ScrolledText(self.root, font=('Times', '12'),height=10)
        self.cmd_text.grid(row=3,column=0,columnspan=5,sticky=tk.W+tk.E,padx=5, pady=5)

        execute_button = tk.Button(self.root, text="Exec", font=('Times', '12'),anchor=tk.CENTER,command=self.execute)
        execute_button.grid(row=4,column=0,padx=5, pady=5)

        clear_button = tk.Button(self.root, text="Clear", font=('Times', '12'),anchor=tk.CENTER,command=button2)
        clear_button.grid(row=4,column=1,padx=5, pady=5)

        reset_button = tk.Button(self.root, text="Reset", font=('Times', '12'),anchor=tk.CENTER,command=button3)
        reset_button.grid(row=4,column=2,padx=5, pady=5)

        show_history_button = tk.Button(self.root, text="Show History", font=('Times', '12'),anchor=tk.CENTER,command=button4)
        show_history_button.grid(row=4,column=3,padx=5, pady=5)

        remove_history_button = tk.Button(self.root, text="Remove History", font=('Times', '12'),anchor=tk.CENTER,command=hisdel)
        remove_history_button.grid(row=4,column=4, padx=5, pady=5)

        save_button = tk.Button(self.root, text="Save", font=('Times', '12'),anchor=tk.CENTER,width=10,command=saveas)
        save_button.grid(row=2,column=1,columnspan=5,sticky=tk.E,padx=5, pady=5)

    def execute(self):
        cmd=self.cmd_text.get(tk.SEL_FIRST,tk.SEL_LAST)
        print(cmd)
        cmd_thread=SubprocessThread(self,cmd)
        cmd_thread.start()
        cmd_thread.stop()

    def mainloop(self):
        self.root.mainloop()
        self.root.destroy()

    def quit(self):
        self.root.quit()

def main():
    app=Application()
    app.mainloop()


if __name__ == '__main__':
    main()