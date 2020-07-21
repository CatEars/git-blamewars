from typing import List, Tuple
import collections
import git
import difflib

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

def blame_stats_from_repo(root_path: str) -> GitStats:
    stats = GitStats()
    repo = git.Repo(root_path)
    commits = filter(lambda x: len(x.parents) == 1, repo.iter_commits())
    for commit in commits:
        parent = commit.parents[0]
        for diff in commit.diff(parent).iter_change_type('M'):
            a_blob = diff.a_blob.data_stream.read().decode('utf-8').splitlines(keepends=True)
            b_blob = diff.b_blob.data_stream.read().decode('utf-8').splitlines(keepends=True)
            blamer = repo.blame(parent, diff.b_path, incremental=True)
            blamer = sorted(blamer, key=lambda x: x.linenos.start)
            blame_index = 0
            line_count = 0
            differ = difflib.ndiff(b_blob, a_blob)
            for line in differ:
                if line[:2] == '- ':
                    line_count += 1
                    while line_count not in blamer[blame_index].linenos:
                        blame_index += 1
                    stats.lines_killed_by(commit.author, 1, blamer[blame_index].commit.author)

                elif line[:2] == '  ':
                    line_count += 1
    return stats


if __name__ == '__main__':
    stats = blame_stats_from_repo('.')
    print(stats.top_killers(10))
