"""Account class
"""
import exception as CustomExceptions


class Account:
    """ Account class to hold information about an account
    """
    def __init__(self, acc_no, name, balance, typ):
        self._an = acc_no
        self._name = name
        self._type = typ
        self._balance = balance

    @property
    def acc_no(self):
        """ getter for account number
        """
        return self._an

    @acc_no.setter
    def acc_no(self, value):
        """ setter for account number
        """
        self._an = value

    @property
    def name(self):
        """ getter for account holder's name
        """
        return self._name

    @name.setter
    def name(self, value):
        """ setter for account holder's name
        """
        self._name = value

    @property
    def balance(self):
        """ getter for account balance
        """
        return self._balance

    @balance.setter
    def balance(self, value):
        """ setter for account balance
        """
        self._balance = value

    @property
    def typ(self):
        """ getter for account type
        """
        return self._type

    @typ.setter
    def typ(self, value):
        """ setter for account type
        """
        self._type = value

    def add_balance(self, amount):
        """ add this amount to present balance
        """
        self._balance += amount

    def draw_money(self, amount):
        """ withdraw money from account
        """
        if self._balance >= amount:
            self._balance -= amount
            print('Updated balance is : {}'.format(self._balance))
            return self._balance
        else:
            raise CustomExceptions.LowBalanceException('Your balance is low')

    def transfer_money(self, account, amount):
        """ tranfer money from this account to other account
        """
        if self._an != account.acc_no:
            if self._balance >= amount:
                self._balance -= amount
                account.balance += amount
                return self._balance
            else:
                raise CustomExceptions.LowBalanceException('Your balance is low')
        else:
            raise CustomExceptions.TransferException('Can not tranfer to your own account')

    def __lt__(self, other):
        """ less than comparison between two accounts
        """
        if self._balance < other.balance:
            return True
        else:
            return False

    def __gt__(self, other):
        """ greater than comparison between two accounts
        """
        if self._balance > other.balance:
            return True
        else:
            return False

    def __eq__(self, other):
        """ equality comparison between two accounts
        """
        if self._balance == other.balance:
            return True
        else:
            return False
