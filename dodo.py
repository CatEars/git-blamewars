STDOUT = 2


def task_test():
    return {
        'actions': ['python -m pytest'],
        'verbosity': STDOUT
    }


def task_coverage():
    return {
        'actions': ['python -m pytest --cov-report html --cov=blamewars --cov-branch'],
        'verbosity': STDOUT
    }
