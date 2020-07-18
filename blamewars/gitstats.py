from typing import List, Tuple
import collections
import os
import subprocess
import pygit2

class GitStats:

    def __init__(self):
        self.casualty_count = collections.defaultdict(int)
        self.killer_count = collections.defaultdict(int)

    def lines_killed_by(self, author: str, lines: int, victim: str):
        self.casualty_count[victim] += lines
        self.killer_count[author] += lines

    def top_killers(self, N: int) -> List[Tuple[str, int]]:
        killers = [(self.killer_count[author], author) for author in self.killer_count]
        killers = sorted(killers, reverse=True)[:N]
        return [(author, kill_count) for kill_count, author in killers]

    def top_victims(self, N: int) -> List[Tuple[str, int]]:
        victims = [(self.casualty_count[author], author) for author in self.casualty_count]
        victims = sorted(victims, reverse=True)[:N]
        return [(author, casualty_count) for casualty_count, author in victims]


def list_all_unignored_files(root_path: str) -> List[str]:
    curr_cwd = os.getcwd()
    os.chdir(root_path)
    result = subprocess.check_output('git ls-files', shell=True, encoding='utf8')
    os.chdir(curr_cwd)
    return result.splitlines()


def blame_stats_from_repo(root_path: str) -> GitStats:
    files = list_all_unignored_files(root_path)
    stats = GitStats()
    repo = pygit2.Repository(root_path)
    for relative_fpath in files:
        blames = repo.blame(relative_fpath)
        for blame in blames:
            stats.lines_killed_by(blame.final_committer.name,
                                  blame.lines_in_hunk,
                                  blame.orig_committer.name)
    return stats

if __name__ == '__main__':
    stats = blame_stats_from_repo('.')
    print(stats.top_killers(3))
