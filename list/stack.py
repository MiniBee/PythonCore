stack = []


def push_id():
    stack.append(raw_input('Enter new string: ').strip())


def pop_id():
    if len(stack) == 0:
        print('\n stock is empty')
    else:
        print('Removed ' + stack.pop())


def view_stack():
    print(stack)


CMDs = {'u': push_id, 'o': pop_id, 'v': view_stack}


def show_menu():
    pr = '''
    pUsh
    pOp
    View
    Quit
    
    Enter choice
    '''
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except Exception:
                choice = 'q'
            if choice not in 'uovq':
                print('Invalid option, try agin')
            else:
                print('\n You pickd: [%s]' % choice)
                break
        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    show_menu()


