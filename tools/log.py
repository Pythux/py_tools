import inspect


def log(log_fn, msg, deep=1):
    """ deep: 1 -> default, 2 if redefined (not used directly)

        log msg with fun calling it and line number
    """
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)[deep]
    _, _, line, name, *_ = calframe
    log_fn('{}: line {}, {}'.format(name, line, msg))
