import subprocess
import threading
import sys

def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line

        if not line and proc.poll() is not None:
            break

def main():
    cmd=["python", "hello.py"]
    for line in get_lines(cmd=cmd):
        decoded=line.decode("utf-8")
        sys.stdout.write(decoded)

if __name__ == '__main__':
    main()