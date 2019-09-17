
import os
import tarfile


def make_tar(source_dir, output_filename=None, compression=''):
    """
        make a tar archive, with optional compression 'gz', 'bz2', 'xz'
        do not use the compression, it's way slower than the command line
    """
    if output_filename is None:
        output_filename = source_dir + '.tar'
    if compression != '':
        output_filename += '.' + compression
    with tarfile.open(output_filename, "w:" + compression) as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def extract_tar(file_path, extract_path='.'):
    """extract all """
    compression = file_path.split('.')[-1]
    with tarfile.open(file_path, 'r:' + compression) as fp:
        fp.extractall(path=extract_path)
