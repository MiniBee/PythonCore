class Student:
    def __init__(self):
        print('I am a student')

    @staticmethod
    def study():
        print('good good study')

    def eating(self):
        print('eating')


if __name__ == '__main__':
    # print('init a student')
    student = Student()
    Student.study()
    Student().eating()
    # print('study')
