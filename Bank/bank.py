""" Bank Application
"""
import account as ac
import database as db
from clint.textui import prompt


def init(database):
    """ The function initializes database.
    """
    database.initialize_db()


def add(database):
    """ The function asks for account details to be added
    """
    acc_no = prompt.query('Enter Account Number : ')
    name = prompt.query('Enter Name : ')
    acc_type = prompt.query('Account Type : ')
    account = ac.Account(acc_no, name, 0, acc_type)
    database.add_account(account)


def search(database):
    """ The function ask for search parameters
    """
    search_by = \
        prompt.query('Search by [n : Name or a :Account Number] : ').lower()
    if search_by == 'n':
        name = prompt.query('Enter Name : ').lower()
        database.search_by_name(name)
    elif search_by == 'a':
        acc_no = prompt.query('Enter Account Number : ')
        if acc_no.isdigit():
            database.search_by_account_no(acc_no)
        else:
            print('Invalid input')


def draw(database):
    """ The function asks for account number and amount to be withdrawn
    """
    acc_no = prompt.query('Enter account number')
    if acc_no.isdigit():
        amount = prompt.query('Enter amount :')
        if amount.isdigit():
            database.draw(acc_no, amount)


def add_balance(database):
    """ The function asks for account  number and balance to be added
    """
    acc_no = prompt.query('Enter account number')
    if acc_no.isdigit():
        amount = prompt.query('Enter amount :')
        if amount.isdigit():
            database.add_balance(acc_no, amount)


def transfer(database):
    """ The function asks for account  numbers and transfer amount
    """
    my_acc = prompt.query('Enter your account number')
    other_acc = prompt.query('Enter other account number')
    amount = prompt.query('Enter amount :')
    database.transfer(my_acc, other_acc, amount)


def compare(database):
    """ The function asks for account  numbers to be compared
    """
    acc1 = prompt.query('Enter 1st account number')
    acc2 = prompt.query('Enter 2nd account number')
    database.compare(acc1, acc2)


def doit():
    """ The function allows the user to enter specific command to be executed
    """
    database = db.Database()    # create a database instance
    loop = True     # flag to stop program execution
    while loop:
        cmd = prompt.query("Bank >> ").lower()      # ask for user input command
        if cmd == 'help':       # user manual
            print(''' Bank >> [options]

                    [options]:

                    init        : initialize database
                    add         : add an account
                    search      : search by name or account number
                    add_balance : add balance to specific account
                    draw        : draw money from given account
                    transfer    : transfer money from one account to another
                    cmp         : compare two accounts
                    exit        : exit Bank Application
            ''')
        elif cmd == 'init':
            # initialize database
            init(database)
        elif cmd == 'add':
            # add an account to database
            add(database)
        elif cmd == 'search':
            # search in database
            search(database)
        elif cmd == 'draw':
            # withdraw money from specific account
            draw(database)
        elif cmd == 'add_balance':
            # add balance to specific account
            add_balance(database)
        elif cmd == 'transfer':
            # transfer money from one account to another
            transfer(database)
        elif cmd == 'cmp':
            # compare accounts which has more balance
            compare(database)
        elif cmd == 'exit':
            # exit application
            print('Thank you for Visiting')
            loop = False

if __name__ == '__main__':
    doit()
# run doit function on start
