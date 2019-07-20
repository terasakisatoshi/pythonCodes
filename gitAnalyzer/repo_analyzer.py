"""
analyze local repository
Reference:
http://qiita.com/mima_ita/items/c41bc650b248a9a39cf7
"""
# install gitpython via pip:
#$pip install gitpython
from git import *
from pprint import pprint

LOCAL_REPOSITORY = '/Users/terasakisatoshi/Documents/work/mps-cancer'

ITEMS=['author','authored_datetime','hexsha','message','name_rev','parents','stats','summary']

def act_shallow_search():
    import git
    repo = git.Repo(LOCAL_REPOSITORY)
    branch = 'develop'
    max_count = 10
    for commit in repo.iter_commits(branch, max_count=10):
        print("---------------------------")

        for item in ITEMS:
            if item=='parents':
                print(item,"=")
                for p in eval('commit.%s' % item):
                    print(p)
            else:
                print(item, "=", eval('commit.%s' % item))


def act_deep_search():
    import time

    def show_blob(b, indent):
        """
        Blobの情報を出力
        """
        print('%s---------------' % (indent))
        print('%shexsha:%s' % (indent, b.hexsha))
        print('%smime_type:%s' % (indent, b.mime_type))
        print('%spath:%s' % (indent, b.path))
        print('%sabspath:%s' % (indent, b.abspath))

    def show_tree(tree, indent):
        """
        Treeの情報を出力
        """
        print('%shexsha :%s' % (indent, tree.hexsha))
        print('%spath :%s' % (indent, tree.path))
        print('%sabspath :%s' % (indent, tree.abspath))
        print('%smode :%s' % (indent, tree.mode))
        for t in tree.trees:
            show_tree(t, indent + '  ')

        print('%s[blobs]' % indent)
        for b in tree.blobs:
            show_blob(b, indent + '  ')

    def show_commitlog(item):
        """
        Commitの情報を出力
        """
        print("hexsha %s" % item.hexsha)
        print(item.author)
        print(item.author_tz_offset)
        print(time.strftime("%a, %d %b %Y %H:%M",
                            time.gmtime(item.committed_date)))
        #print (item.committer)
        #print (item.committer_tz_offset)
        #print (item.encoding)
        print(item.message)
        print(item.name_rev)
        print(item.summary)
        print('[stats]')
        print(item.stats.total)
        print(item.stats.files)
        print('[parents]')
        for i in item.parents:
            print('  %s' % i.hexsha)

        print('[Tree]')
        show_tree(item.tree, '  ')

    repo = Repo(LOCAL_REPOSITORY)
    for item in repo.iter_commits('develop', max_count=1):
        print('================================')
        show_commitlog(item)


def main():
    act_shallow_search()
    #act_deep_search()

if __name__ == '__main__':
    main()
