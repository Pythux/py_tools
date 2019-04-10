import sys
import itertools


class WeelEWonka:
    slash_weel = itertools.cycle(['\\', '|', '/', '--'])
    to_clear = 0

    def msg(self, msg):
        print(' ' * self.to_clear, end='\r')
        msg = next(self.slash_weel) + '\t' + msg
        self.to_clear = len(msg) + \
            len(list(filter(lambda c: c == '\t', msg))) * 6
        print(msg, end='\r')

    def msg_clear(self):
        print(' ' * self.to_clear, end='\r')

    def dotdots(self):
        print('.', end='')
        sys.stdout.flush()

    def better_msg(self, msg):
        print('\b' * self.to_clear, end='')  # erase the last written char
        print(' ' * self.to_clear, end='')
        print('\b' * self.to_clear, end='')

        msg = next(self.slash_weel) + '\t' + msg
        self.to_clear = len(msg) + \
            len(list(filter(lambda c: c == '\t', msg))) * 6
        print(msg, end='')
        sys.stdout.flush()

    def better_msg_clear(self):
        print('\b' * self.to_clear, end='')  # erase the last written char
        print(' ' * self.to_clear, end='')
        print('\b' * self.to_clear, end='')
        sys.stdout.flush()


class Color:
    """enum to display colors"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # color end
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    color_dic = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',  # color end
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m',
    }

    @staticmethod
    def c(msg, *add):
        return ''.join([Color.color_dic[to_add] for to_add in add]) + \
            msg + Color.ENDC
