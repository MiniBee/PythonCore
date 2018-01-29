

def convert(func, seq):
    return [func(eachNum) for eachNum in seq]

myset = (1, 2, 3, 4.5, 234567)
print(convert(float, myset))
print(convert(int, myset))



def dictVarArgs(arg1, arg2 = 'defaultB', **theRest):
    print('formal arg1: ', arg1)
    print('formal arg2: ', arg2)
    for eachKey in theRest:
        print('Xtra arg %s : %s' % (eachKey, theRest[eachKey]))


dictA = {'a': 'a', 'b': 'b'}

dictVarArgs('tom', a='a', b='b')


