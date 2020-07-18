from typing import List, Tuple
import collections

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
    return stats

if __name__ == '__main__':
    stats = blame_stats_from_repo('.')
    print(stats.top_killers(3))
