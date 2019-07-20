import tkinter
from tkinter import *
import subprocess
import os
from os import system as cmd

WINDOW_SIZE = "600x400"
top = tkinter.Tk()
top.geometry(WINDOW_SIZE)

def helloCallBack():
   print ("Below is the output from the shell script in terminal")
   subprocess.call('perl /projects/tfs/users/$USER/scripts_coverage.pl', shell=True)
def BasicCovTests():
   print ("Below is the output from the shell script in terminal")
   subprocess.call('perl /projects/tfs/users/$USER/basic_coverage_tests.pl', shell=True)
def FullCovTests():
   print ("Below is the output from the shell script in terminal")
   subprocess.call('perl /projects/tfs/users/$USER/basic_coverage_tests.pl', shell=True)


Scripts_coverage  = tkinter.Button(top, text ="Scripts Coverage", command = helloCallBack)
Scripts_coverage.pack()

Basic_coverage_tests  = tkinter.Button(top, text ="Basic Coverage Tests", command = BasicCovTests)
Basic_coverage_tests.pack()

Full_coverage_tests  = tkinter.Button(top, text ="Full Coverage Tests", command = FullCovTests)
Full_coverage_tests.pack()

termf = Frame(top, height=100, width=500)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()

os.system('xterm -into %d -geometry 100x20 -sb &' % wid)

def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))

top.mainloop()