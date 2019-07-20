import subprocess
import os
from os.path import join

scriptdir=os.path.dirname(__file__)
exe="hello.exe"
process=join(scriptdir,exe)
execute=subprocess.Popen(process,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
print(execute.stdout.readline())