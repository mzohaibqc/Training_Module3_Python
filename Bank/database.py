"""
sdsdsad sdsd
"""

import sqlite3

import account as ac


class Database:
    """ This class performs all task related to database
    """

    def __init__(self):
        """ Initialize database
        """
        self.database = sqlite3.connect('bank.db')    # connection to database
        self.database.row_factory = sqlite3.Row   # set row factory to Row
        self.cursor = self.database.cursor()      # get cursor from database

    def initialize_db(self):
        """Initialize database
        """
        try:
            self.cursor.execute(''' DROP TABLE if EXISTS account ''')
            # drop previous table if exists
            self.cursor.execute('''CREATE TABLE account
                                (
                                    id INTEGER  PRIMARY KEY AUTOINCREMENT ,
                                    acc_no TEXT,
                                    name TEXT,
                                    balance INTEGER,
                                    type TEXT
                                )
                                ''')
            self.database.commit()    # commit changes otherwise roll back
            print('Table created Successfully')
        except sqlite3.Error as exception:
            print(exception)

    def add_account(self, account):
        """Add a new account to database
        """
        sql = '''INSERT INTO account(acc_no, name, balance, type)
                                VALUES(?, ?, ?, ?)'''
        values = (account.acc_no, account.name, account.balance, account.type)
        try:
            self.cursor.execute(sql, values)
            self.database.commit()
            print('Account Added Successfully')
        except sqlite3.IntegrityError as exception:
            print('Database Error :', exception)

    def search_by_name(self, name):
        """Search records in database using name
        """
        sql = 'SELECT * FROM account WHERE name LIKE ?'
        self.cursor.execute(sql, ('%' + name + '%',))
        rows = self.cursor.fetchall()
        Database.display(rows)

    def search_by_account_no(self, acc_no):
        """Search records in database using account number
        """
        sql = 'select * from account where acc_no = ?'
        self.cursor.execute(sql, (acc_no,))
        rows = self.cursor.fetchall()
        Database.display(rows)

    def add_balance(self, acc_no, amount):
        """Add balance to specific account
        """
        sql = 'SELECT * FROM account WHERE acc_no = ?'
        self.cursor.execute(sql, (acc_no,))
        row1 = self.cursor.fetchone()
        account1 = ac.Account(row1['acc_no'], row1['name'],
                              row1['balance'], row1['type'])
        account1.add_balance(int(amount))
        self.update(account1)

    def draw(self, acc_no, amount):
        """Withdraw money from specific account
        """
        sql = 'SELECT * FROM account WHERE acc_no = ?'
        self.cursor.execute(sql, (acc_no,))
        row1 = self.cursor.fetchone()
        account1 = ac.Account(row1['acc_no'], row1['name'],
                              row1['balance'], row1['type'])
        account1.draw_money(int(amount))
        self.update(account1)

    def transfer(self, acc_no1, acc_no2, amount):
        """Transfer money from one account to another
        """
        sql = 'select * from account where acc_no = ?'
        self.cursor.execute(sql, (acc_no1,))
        row1 = self.cursor.fetchone()
        self.cursor.execute(sql, (acc_no2,))
        row2 = self.cursor.fetchone()
        if row1 is not None and row2 is not None:
            account1 = ac.Account(row1['acc_no'], row1['name'],
                                  row1['balance'], row1['type'])
            account2 = ac.Account(row2['acc_no'], row2['name'],
                                  row2['balance'], row2['type'])
            if account1.transfer_money(account2, int(amount)):
                print('updated balance : {}'.format(account1.balance))
                self.update(account1)
                self.update(account2)
            else:
                print("Try again...")
        else:
            print('Account not found')

    def compare(self, acc_no1, acc_no2):
        """Compare two accounts to check which account has more balance
        """
        sql = 'SELECT * FROM account WHERE acc_no = ?'
        self.cursor.execute(sql, (acc_no1,))
        row1 = self.cursor.fetchone()
        self.cursor.execute(sql, (acc_no2,))
        row2 = self.cursor.fetchone()
        if row1 is not None and row2 is not None:
            account1 = ac.Account(row1['acc_no'], row1['name'],
                                  row1['balance'], row1['type'])
            account2 = ac.Account(row2['acc_no'], row2['name'],
                                  row2['balance'], row2['type'])
            if account1 == account2:
                print('Both account have equal Balance')
            elif account1 > account2:
                print('1st account has more balance')
            else:
                print('2nd account has more balance')
        else:
            print('Account not found')

    def update(self, account):
        """update record
        """
        try:
            sql = 'UPDATE account SET balance = ? WHERE acc_no = ?'
            self.cursor.execute(sql, (account.balance, account.acc_no))
            self.database.commit()
        except sqlite3.Error as exception:
            print(exception)

    @staticmethod
    def display(rows):
        """display retrieved data
        """
        if len(rows) == 0:  # if no record is retrieved show sorry message
            print('Sorry, No record found')
        else:
            print("==========================================")
        for row in rows:    # iterate through all records
            print(" Account Number :  {}".format(row[1]))
            print(" Name           :  {}".format(row[2]))
            print(" Balance        :  {}".format(row[3]))
            print("==========================================")
