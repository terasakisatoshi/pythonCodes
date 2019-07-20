from distutils import dir_util
import shutil
import time
def main():
    source_folder="test"
    target_folder="copied"
    dir_util.copy_tree(source_folder,target_folder)
    print("create copied folder")
    time.sleep(5)
    shutil.rmtree(target_folder)
    print("goodbye copied folder")
if __name__ == '__main__':
    main()