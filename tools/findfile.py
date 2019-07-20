import sys
import os
from textfinder import FileFinder


def main():
    argv = sys.argv
    argc = len(argv)

    print(argv)
    print(argc)

    if(argc not in {2, 3}):
        print("usage: python %s (folder's relative path)\n" % argv[0])
        print("or\n")
        print("usage: python %s (folder's relative path) (extension))\n" %
              argv[0])
        quit()

    extension = 'txt'
    if(argc == 3):
        extension = argv[2]

    basedir = os.path.dirname(__file__)
    reldir = argv[1]
    finder = FileFinder(reldir, extension)
    files = finder.getfiles()
    print(files)


if __name__ == '__main__':
    main()
