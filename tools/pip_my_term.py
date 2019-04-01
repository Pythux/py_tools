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
