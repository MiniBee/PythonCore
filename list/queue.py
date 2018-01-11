queue = []


def en_it():
    queue.append(raw_input('Enter new string: ').strip())


def de_it():
    if len(queue) == 0:
        print 'Cant not pop from an empty queue!'
    else:
        print 'Removed' + queue.pop(0)


def view_it():
    print queue


CMDs = {'e': en_it, 'd': de_it, 'v': view_it}


def show_menu():
    pr = '''
    En
    De
    Vi
    Qu
    
    Enter choice: 
    '''
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except Exception:
                choice = 'q'
            if choice not in 'edvq':
                print 'Invalid option, try again'
            else:
                print '\nYou picked %s' % choice
                break
        if choice == 'q':
            break
        CMDs[choice]()


if __name__ == '__main__':
    show_menu()

