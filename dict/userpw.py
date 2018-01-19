import sys

db = {}

def new_user():
    prompt = 'login desired: '
    while True:
        user_name = input(prompt)
        if db.get(user_name) is not None:
            print('Name token, try another...')
            continue
        else:
            break
    pwd = input('passwd: ')
    db[user_name] = pwd

def old_user():
    q = False
    while not q:
        user_name = input('Enter your name or quit: ').strip().lower()
        if user_name == 'q':
            print('Byebye')
            break
        passwd = db.get(user_name)
        if passwd is None:
            r = input('Please regist first(R) or try agin(T)').strip().lower()
            if r == 'r':
                new_user()
                continue
            if r == 't':
                continue
        while True:
            user_passwd = input('Enter your password or quit: ')
            if user_passwd == 'q':
                print('Byebye')
                break
            elif user_passwd != passwd:
                print('Wrong password...')
                break
            else:
                break
        break


new_user()
old_user()

if __name__ == '__main__':
    pass

