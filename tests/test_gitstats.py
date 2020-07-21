import blamewars

def test_top_killers():
    stats = blamewars.GitStats()
    stats.lines_killed_by('a', 10, 'b')
    stats.lines_killed_by('b', 2, 'c')
    stats.lines_killed_by('c', 1, 'a')
    assert len(stats.top_killers(5)) == 3
    assert len(stats.top_killers(4)) == 3
    assert len(stats.top_killers(3)) == 3
    assert len(stats.top_killers(2)) == 2
    assert len(stats.top_killers(1)) == 1

    assert [('a', 10), ('b', 2), ('c', 1)] == stats.top_killers(3)


def test_top_victims():
    stats = blamewars.GitStats()
    stats.lines_killed_by('a', 10, 'b')
    stats.lines_killed_by('b', 2, 'c')
    stats.lines_killed_by('c', 1, 'a')
    assert len(stats.top_victims(5)) == 3
    assert len(stats.top_victims(4)) == 3
    assert len(stats.top_victims(3)) == 3
    assert len(stats.top_victims(2)) == 2
    assert len(stats.top_victims(1)) == 1

    assert [('b', 10), ('c', 2), ('a', 1)] == stats.top_victims(3)

