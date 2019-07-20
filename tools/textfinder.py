import sys
import os
from os.path import join,relpath
from glob import glob

class FileFinder(object):
    def __init__(self,reldir="",extension="txt"):
        self.basedir=os.path.dirname(__file__)
        self.reldir=reldir
        self.extension=extension
    def getfiles(self,abspath=""):
        if(abspath):
            searchdir=abspath
        searchdir=join(self.basedir,self.reldir)
        files=[relpath(x,searchdir) for x in glob(join(searchdir, '*.'+self.extension))]
        return files



def main():
    argv=sys.argv
    argc=len(argv)

    print (argv)
    print (argc)

    if(argc not in {2,3}):
        print("usage: python %s (folder's relative path)\n"% argv[0])
        print("or\n")
        print("usage: python %s (folder's relative path) (extension))\n"% argv[0])
        quit()

    extension='txt'
    if(argc==3):
        extension=argv[2]

    basedir=os.path.dirname(__file__)
    reldir=argv[1]
    finder=FileFinder(reldir,extension)
    files=finder.getfiles()
    #search_dir=join(basedir,reldir)
    #files=[relpath(x,search_dir) for x in glob(join(search_dir, '*'+extension))]
    print(files)
if __name__ == '__main__':
    main()
