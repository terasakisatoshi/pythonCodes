import subprocess
import sys
from os.path import join

def main():
    argv=sys.argv
    argc=len(argv)
    print ("argv=%s"%argv)
    print ("argc=%d"%argc)
    if(argc==2):
        exename=argv[1]
        path ="hoge"
        command=exename+" "+join(".",path)
        echo="echo "+command

        subprocess.call(echo,shell=True)
        subprocess.call(command,shell=True)

if __name__ == '__main__':
    main()