import webbrowser
import tempfile

def open_in_browser(html_file: str):
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(html_file)
        url = 'file://{}'.format(f.name)
    webbrowser.open(url)
