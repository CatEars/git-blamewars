import blamewars
import html5lib


def test_is_xml_like():
    stats = blamewars.GitStats()
    A = 'a' * 80
    B = 'b' * 80
    A_kills = 15161
    B_kills = 11151
    stats.lines_killed_by(A, A_kills, B)
    stats.lines_killed_by(B, B_kills, A)
    rendered = blamewars.generate_template(stats)

    assert isinstance(rendered, str)
    assert A in rendered
    assert B in rendered
    assert str(A_kills) in rendered
    assert str(B_kills) in rendered

    try:
        parser = html5lib.HTMLParser(strict=True)
        document = parser.parse(rendered)
    except Exception as e:
        # If any of the operations in the try-catch fail, then this is not valid HTML
        # --> fail the test
        assert False

