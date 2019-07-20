import subprocess
from subprocess import Popen
from time import sleep


def main():
    cmd="sleep 30"
    proc = Popen(cmd,shell=True)
    sleep(5)
    proc.terminate()


if __name__ == '__main__':
    main()