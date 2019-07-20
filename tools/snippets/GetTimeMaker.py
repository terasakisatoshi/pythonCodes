
# coding: Shift_JIS

import sys
argvs=sys.argv
argc=len(argvs)

print argvs
print argc

if (argc != 2):   # 引数が足りない場合は、その旨を表示
    print 'Usage: # python %s filename' % argvs[0]
    quit()  

from os.path import join, relpath
from glob import glob
strTestsetPath="Testset"+argvs[1]
joined=join("1","Classification")
path=join(strTestsetPath,joined)

files = [relpath(x, path) for x in glob(join(path, '*_R.txt'))]
#for file in files:
#    print file
#print files
print path
import subprocess
import os

f = open(join(path,'shotname.txt'), 'w')
for file in files:
    #print file
    shot_name=file.split("_")[0]+"\n"
    print file.split("_")[0]
    f.write(shot_name)

cmd="GetMeasureTimeData.exe"+" "+join(".",path)
echo="echo "+cmd
subprocess.call(echo,shell=True)
subprocess.call(cmd,shell=True)

quit()  
