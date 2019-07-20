import os

def find_all_files(directory):
    for root,dirs,files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root,file)
def testwalk(directory):
    for root,dirs,files in os.walk(directory):
        print("root=%s\ndirs=%s\nfiles=%s\n"%(root,dirs,files))
        print("\n")
def main():
    target_directory=os.getcwd()
    testwalk(target_directory)

    #for file in find_all_files(os.getcwd()):
    #    print(file)
if __name__ == '__main__':
    main()