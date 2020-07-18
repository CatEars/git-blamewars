from gitstats import GitStats
import jinja2

_env = jinja2.Environment(
    loader=jinja2.PackageLoader('blamewars', 'templates'),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)
_killer_template = _env.get_template('blamewars.html')


def generate_template(stats: GitStats) -> str:
    return _killer_template.render(
        killers=stats.top_killers(3),
        victims=stats.top_victims(3)
    )


if __name__ == '__main__':
    stats = GitStats()
    stats.lines_killed_by('Schwounkeponken', 1337, 'Henkebenk')
    stats.lines_killed_by('Henkebenk', 10, 'villiamboi')
    stats.lines_killed_by('Mr. Torvalds', 100000000000, '*')
    print(generate_template(stats))
