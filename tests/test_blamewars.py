import blamewars
import webbrowser
import os

def test_open_in_browser(monkeypatch):
    my_url = None
    def do_open(url):
        nonlocal my_url
        my_url = url

    monkeypatch.setattr(webbrowser, 'open', do_open)

    html_str = '''<html>Hello World!</html>'''
    blamewars.open_in_browser(html_str)
    assert isinstance(my_url, str)
    assert my_url.startswith('file://')
    fpath = my_url[len('file://'):]
    assert os.path.exists(fpath)
    with open(fpath, 'r') as f:
        content = f.read()
        assert content == html_str
