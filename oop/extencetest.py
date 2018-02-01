class Parent(object):
    def classMethod():
        print('I am a classMethod!')

    def instance_method(self):
        print('I am a instance method')


class Child(Parent):
    def child_instance_method(self):
        print('I am child instance method')



p = Parent()
Parent.classMethod()


c = Child()
Child.classMethod()
c.instance_method()
c.child_instance_method()