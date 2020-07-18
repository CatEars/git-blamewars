STDOUT = 2


def task_test():
    return {
        'actions': ['python -m pytest'],
        'verbosity': STDOUT
    }
