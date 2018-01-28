# def counter(start_at=0):
#     count = [start_at]
#     def incr():
#         count[0] += 1
#         return count[0]
#     print(count)
#     return incr
#
#
# count = counter()
# print(count())
# print(count())
#
#
# x = 10
# def foo():
#     y = 5
#     bar = lambda z:x+z
#     y = 1
#     print(bar(y))
#
#
# foo()



# def counter(start_at=0):
#     count = start_at
#     while True:
#         val = yield count
#         print(val)
#         if val is not None:
#             count = val
#         else:
#             count += 1
#
# count = counter()
# print(count.__next__())
# print(count.__next__())
# count.send(10)
# print(count.__next__())
# print(count.__next__())
# count.close()

# print(list(map(lambda x, y: (x, y), [1,2,3], [5,6,7])))

from time import time
def tsFunction(func):
    def ts():
        a = time()
        print(a)
        result = func()
        print(time() - a)
        return result
    return ts

@tsFunction
def test():
    i=0
    while i < 10000:
        i+=1
        print(i**2)


if __name__ == '__main__':
    test()


