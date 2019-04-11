import os


def get_size(start_path='.', human_readable=True):
    total_size = 0
    if os.path.isfile(start_path):
        return os.path.getsize(start_path)
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        total_size += len(dirnames) * 4096
    if human_readable:
        return convert_to_human(total_size)
    return total_size


def convert_to_human(size):
    unit = ' KMGT'
    for u in unit[:-1]:
        if size < 1024:
            return ('%.1f' % size) + ' {}o'.format(u)
        size = size / 1000
        # Nemo (file navigator) use the division by 1000, not by 1024
        # so we will do the same,
        # to not disturbe the user with two different value
    return ('%.1f' % size) + ' {}o'.format(unit[-1])
