
from subprocess import Popen, TimeoutExpired, PIPE
import shlex


def run_cmd(args, input=None, timeout=10):
    stdin = PIPE if input else None
    with Popen(shlex.split(args), stdin=stdin, stdout=PIPE, stderr=PIPE,
               encoding='utf-8') as proc:
        try:
            # proc.wait(timeout=10)
            outs, errs = proc.communicate(input=input, timeout=timeout)
        except TimeoutExpired as e:
            print('TimeoutExpired')
            proc.kill()
            raise e
        # return str(proc.stdout.read(), 'utf-8').rstrip('\n')
        return outs.rstrip('\n'), errs


def sh(cmds, timeout=10, get_err=True):
    input = None
    li_errs = []
    for args in cmds.split(' | '):
        try:
            input, errs = run_cmd(args, input, timeout=timeout)
        except TimeoutExpired as e:
            raise e
        li_errs += errs,
    if get_err:
        return input, ''.join(li_errs)
    return input


def send_notif(title, msg, icon=None):
    icon = icon if icon else 'media-memory'
    sh("notify-send --icon={icon} '{title}' '{msg}'"
        .format(icon=icon, title=title, msg=msg))


def get_free_mem():
    free_go = int(sh("free -w -m", get_err=False)
                  .split('\n')[1].split(' ')[-1]) / 1000
    return free_go
