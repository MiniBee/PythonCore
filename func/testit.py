from functools import reduce, partial
from operator import add, mul

a = [1, 2, 3, 4, 5, -1, -2, -3]
b = map(lambda x: x**2, filter(lambda x: x > 0, a))
print(b)
print(list(b))

c = reduce(lambda x, y: x+y, map(lambda x: x**2, filter(lambda x: x > 0, a)))
print(c)


add1 = partial(add, 1)
print(add1(100))


print(int('10010', base=2))



