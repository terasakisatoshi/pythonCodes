import git
from collections import defaultdict

LOCAL_REPOSITORY = '/Users/terasakisatoshi/Documents/work/mps-cancer'
ITEMS = ['author', 'authored_datetime', 'hexsha', 'message',
         'name_rev', 'parents', 'stats', 'summary']


class Commit(object):

    def __init__(self, commit, items):
        self.commit = commit
        self.items = items

    def __getattr__(self, name):
        return getattr(self.commit, name)

    def show(self):
        for item in self.items:
            if item == 'parents':
                print(item, '=')
                for parent in eval('self.commit.%s' % item):
                    print(parent)
            elif item == 'stats':
                print(item, '=')
                print(self.commit.stats.total)
                print(self.commit.stats.files)
            else:
                print(item, '=', eval('self.commit.%s' % item))


class Repository(object):

    def __init__(self, local_repository, items):
        self.repo_path = local_repository
        self.items = items
        self.repository = git.Repo(self.repo_path)

    def extract_commits(self, branch, max_count=None):
        if max_count:
            objects = self.repository.iter_commits(branch, max_count=max_count)
        else:
            objects = self.repository.iter_commits(branch)
        self.commits = [Commit(obj, self.items) for obj in objects]
        return self.commits

class Author(object):
    def __init__(self,author,commits,repo_info):
        self.author=author
        self.commits=commits
        self.repo_info=repo_info

    def analyze(self):
        # show commit share
        self.share_rate=100.0*len(self.commits)/len(self.repo_info)
        # prepare branch name
        name_revs = [commit.name_rev for commit in self.commits]
        self.branch_names = set()
        for name_rev in name_revs:
            hexsha, branch_name = name_rev.split(" ")
            branch_name = branch_name.split("~")[0]
            self.branch_names.add(branch_name)
        # show stats
        self.stat_totals=[]
        for commit in self.commits:
            self.stat_totals.append((commit.stats.total['insertions'],
                                        commit.stats.total['deletions']))
        #commit_datatime
        self.authored_datetimes=[]
        for commit in self.commits:
            self.authored_datetimes.append(commit.authored_datetime)



def main():
    repository = Repository(LOCAL_REPOSITORY, ITEMS)
    main_branch = 'develop'
    repo_info = repository.extract_commits(main_branch)
    # show all raw information
    #for commit in repo_info:
    #    commit.show()
    # collect authors
    author_commit_dict = defaultdict(list)
    for commit in repo_info:
        author_commit_dict[commit.author].append(commit)
    #initialize Author classes corresponds author(i.e. comitter)
    for author,commits in author_commit_dict.items():
        Author(author,commits,repo_info).analyze()



if __name__ == '__main__':
    main()
