STDOUT = 2


def task_test():
    return {
        'actions': ['python -m pytest'],
        'verbosity': STDOUT
    }


def task_coverage():
    return {
        'actions': ['python -m pytest --cov=git-blamewars --cov-report=html --cov-branch'],
        'verbosity': STDOUT
    }
