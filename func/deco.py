from time import ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func()
    return wrappedFunc

def loopFunction(func):
    def loop():
        for i in range(10):
            print(i+1)
            func()
    return loop

@loopFunction
@tsfunc
def foo():
    print('hello, world')

if __name__ == '__main__':
    foo()