class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), 'Value must be a float!'
        self.value = round(val, 2)

    def __str__(self):
        return str(self.value)


rfm = RoundFloatManual(42.0)
# print(rfm)



class DevNull(object):
    def __init__(self, name=None):
        self.name = name
    def __get__(self, obj, typ=None):
        print('Accessing [%s]... ignoring' % self.name)

    def __set__(self, obj, val):
        print('Attempt to assign %r... ignoring' % (val))

class C1(object):
    foo = DevNull('foo')

# c1 = C1()
# print(c1.foo)

c2 = C1()
c2.foo = 'hello, world'
x = c2.foo
print(x)