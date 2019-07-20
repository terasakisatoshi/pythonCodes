from modulefinder import ModuleFinder
"""
Reference:
http://thinkami.hatenablog.com/entry/2017/04/06/201357
"""

def main():
    finder = ModuleFinder()
    finder.run_script('sample.py')

    print('dir ModuleFinder: {}'.format(dir(finder)))

    for name, mod in finder.modules.items():
        print("type:{}".format(type(mod)))
        print("dir module object:{}".format(dir(mod)))

    for name, mod in finder.modules.items():
        print('-'*20)
        print("name:%s"%name)
        print("globalnames:%s"%mod.globalnames)
        print("modules:%s"%','.join(list(mod.globalnames.keys())))
        print("starimports:{}".format(mod.starimports))

    print("bad modules:{}".format(','.join(finder.badmodules.keys())))
if __name__ == '__main__':
    main()
