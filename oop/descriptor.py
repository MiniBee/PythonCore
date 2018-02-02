class descriptorTest(object):
    cls_val = 1
    def __init__(self):
        self.ins_val = 10

t = descriptorTest()
print(t.__dict__)


class Desc(object):
    def __get__(self, instance, owner):
        print('__get__...')
        print('self: \t\t', self)
        print('instance: \t', instance)
        print('owner: \t\t', owner)
        print('=*40', '\n')

    def __set__(self, instance, value):
        print('__get__...')
        print('self: \t\t', self)
        print('instance: \t', instance)
        print('owner: \t\t', value)
        print('=*40', '\n')



class TestDesc(object):
    x = Desc()



t = TestDesc()
t.x

