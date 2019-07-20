import os
from os.path import basename,dirname,join
from pathlib import PureWindowsPath

def get_target_path_from_root(target,root=PureWindowsPath(os.getcwd()).drive+"\\"):
    
    dir_seq=[]
    folder=target
    while folder!=root:
        bname=basename(folder)
        dir_seq.append(bname)
        folder=dirname(folder)
    return reversed(dir_seq)

def mkdir_target_path_from_root(iter_dir_seq,root=PureWindowsPath(os.getcwd()).drive+"\\"):
    mktarget=root
    for folder in iter_dir_seq:
        mktarget=join(mktarget,folder)
        if not os.path.exists(mktarget):
            print(mktarget)
            os.mkdir(mktarget)

def main():
    cwd=os.getcwd()
    folder_seq=['folderA','folderB']

    root=cwd
    mktarget=join(cwd,*folder_seq)
    iter_dir_seq=get_target_path_from_root(target=mktarget,root=root)
    print(iter_dir_seq)
    mkdir_target_path_from_root(iter_dir_seq,root)
if __name__ == '__main__':
    main()