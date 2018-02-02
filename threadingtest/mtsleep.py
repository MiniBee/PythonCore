import threading
from time import sleep, ctime

loops = (4, 2)

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        super(MyThread, self).__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def loop(nloop, nsec):
        print('start loop', nloop, 'at', ctime())
        sleep(nsec)
        print('loop', nloop, 'done at', ctime())

    def main():
        