import os


def to_absolute_path(path):
    if path[0] == '~':
        path = path[2:]
    return os.path.join(os.environ['HOME'], path)


def get_relative_path(root_path, abs_path):
    """abs_path must be in root_path"""
    li_e = []
    r = abs_path
    while True:
        if r == root_path:
            if len(li_e) == 0:
                return ''
            return os.path.join(*li_e[::-1])
        r, e = os.path.split(r)
        li_e += e,

        if e == '':
            raise SystemError(
                "abs_path must be in root_path\nabs_path: {}\nroot_path: {}"
                .format(abs_path, root_path))
