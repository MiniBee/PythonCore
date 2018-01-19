username = '游客'
my_stock = {}
stocks = {10000: 100, 10001: 200}


def add_stock():
    global username
    global my_stock
    stock_num = int(input('Enter stock num: ').strip().lower())
    if stocks.get(int(stock_num)) is None:
        print('Wrong num...')
        show_menu()
    else:
        print(stocks.get(stock_num))
        stock_qty = int(input('Enter %s num' % stock_num).strip().lower())
    my_stock[username][stock_num] = [stocks[stock_num], stocks[stock_num], stock_qty]
    print(my_stock[username][stock_num])
    show_menu()


def show_stocks():
    print('stocks : ' + my_stock[username])


def show_menu():
    global username
    global my_stock
    print('hello, %s' % username)
    print('you have:'+str(my_stock))
    choice = input('''
        Buy
        Show
        Sale
        Quit
        Login
        Regis
    ''')
    if choice not in 'lrq':
        check_user()
    CMDs[choice]()


def stock_run():
    pass


def login():
    global username
    username = input('Enter your username: ').strip().lower()
    if my_stock.get(username) is None:
        print('Wrong username...')
        username = None
    show_menu()


def regis():
    global username
    global my_stock
    username = input('Enter your username').strip().lower()
    if my_stock.get(username) is None:
        my_stock[username] = {}
        login()
    else:
        print('user name ...')
        show_menu()

CMDs = {'b': add_stock, 's': show_menu, 'a': 'sale_stock', 'q': quit,
        'l': login, 'r': regis}


def check_user():
    global username
    if my_stock.get(username) is not None:
        pass
    else:
        print('Login please...')
        show_menu()


if __name__ == '__main__':
    show_menu()