import webbrowser
import tempfile

def open_in_browser(html_file: str):
    with tempfile.NamedTemporaryFile('w', delete=False) as f:
        f.write(html_file)
        url = 'file://{}'.format(f.name)
    webbrowser.open(url)


if __name__ == '__main__':
    import os
    import gitstats
    import template
    current_dir = os.getcwd()
    blame_stats = gitstats.blame_stats_from_repo(current_dir)
    html = template.generate_template(blame_stats)
    open_in_browser(html)
