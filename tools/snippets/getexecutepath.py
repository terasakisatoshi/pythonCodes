import os
import sys

print("__file__=%s"% __file__)
print("sys.argv[0]=%s"%sys.argv[0])
print("os.path.dirname(__file__)=%s"%os.path.dirname(__file__))
print("os.getcwd()=%s"%os.getcwd())
print("os.path.basename(__file__)=%s"%os.path.basename(__file__))
print("os.path.abspath(__file__)=%s"%os.path.abspath(__file__))
print("os.path.dirname(__file__)=%s"%os.path.dirname(__file__))
print("os.path.abspath(os.path.dirname(__file__))=%s"%os.path.abspath(os.path.dirname(__file__)))