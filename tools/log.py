import inspect
import logging


def log(log_fn, msg, deep=1):
    """ deep: 1 -> default, 2 if redefined (not used directly)

        log msg with fun calling it and line number
    """
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)[deep]
    frame, file_path, line, name, *_ = calframe
    module_path = frame.f_globals['__name__']
    log_fn('{}:{}, line {}: {}'.format(module_path, name, line, msg))


def logx(x, msg): log(x, msg, deep=3)


def logd(msg): logx(logging.debug, msg)


def logi(msg): logx(logging.info, msg)


def logw(msg): logx(logging.warning, msg)


def loge(msg): logx(logging.error, msg)
