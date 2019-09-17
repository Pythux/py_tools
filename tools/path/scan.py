import os
import re

from tools.shell import sh
from tools.path import to_absolute_path


def scan_file_dir(path, timeout, change_since_mn, fn_file, fn_dir, avoid_paths=None):
    def check_file_dirs(file_dirs, errs=None):
        check_file_dirs_with(file_dirs, errs, fn_file, fn_dir, avoid_paths)
    scan_with(path, timeout, change_since_mn, check_file_dirs)


def scan_with(path, timeout, change_since_mn, fn_path):
    """path should be absolute,
        scan everything inside the path
    """
    path = to_absolute_path(path)

    # LC_ALL=C make error message not localized, so in english
    find = 'find "{search_start}"'.format(search_start=path)
    if change_since_mn:
        find += ' -mmin -{mn}'.format(mn=change_since_mn)
    outs, errs = sh(find, timeout=timeout)
    fn_path(outs.split('\n'), errs.split('\n'))


def to_avoid(path, avoid_paths):
    if avoid_paths is not None:
        for avoid in avoid_paths:
            if (path + '/').startswith(avoid):
                return True
    return False


def check_file_dirs_with(file_dirs, errs, fn_file, fn_dir, avoid_paths=None):
    if avoid_paths:
        avoid_paths = sorted(map(lambda p: p + '/', avoid_paths), key=lambda p: len(p), reverse=True)
    errs = errs if errs else []
    for file_dir in file_dirs:
        if not (file_dir == '' or to_avoid(file_dir, avoid_paths)):
            fn_file(file_dir) if os.path.isfile(file_dir) else fn_dir(file_dir)

    for err in errs:
        if err == '':
            pass
        elif re.match(r"find: (.)+: ", err):  # Permission denied
            pass
        else:
            raise ValueError('unhandled ! “{}”'.format(repr(err)))
