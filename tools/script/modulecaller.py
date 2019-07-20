import os
from os.path import join,relpath
import argparse
from glob import glob
import subprocess

def parser_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-ext','--extension',default=".txt",type=str,help="file extension e.g. 'txt' or 'py'")
    parser.add_argument('-rel','--rel_dir',default="",type=str,help="relative folder path which you want to search")
    parser.add_argument('-abs','--abs_dir',default="",type=str,help="absolutely folder path which you want to search")
    parser.add_argument('-mod','--module_path',default="",type=str,help="absolytely module path or executable module commands")    
    return parser.parse_args()

def main():
    args=parser_args()
    basedir=os.path.dirname(__file__)
    reldir=args.rel_dir
    fulldir=""
    if(args.abs_dir):
        fulldir=args.abs_dir
    else:
        fulldir=join(basedir,reldir)

    files=[relpath(x,fulldir) for x in glob(join(fulldir,'*.'+args.extension))]
    print(files)
    for file in files:
        command=args.module_path + " " +os.path.abspath(file)
        echo="echo"+" "+command
        subprocess.call(echo,shell=True)
        subprocess.call(command,shell=True)

if __name__ == '__main__':
    main()