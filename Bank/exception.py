""" Custom Exceptions
"""

class LowBalanceException(Exception):
    """ Throw Exception when balance is low
    """
    def __init__(self, msg):
        self.msg = msg
        super(LowBalanceException, self).__init__(msg)

    def __str__(self):
        """ get a string representation of Exception
        """
        return self.msg


class TransferException(Exception):
    """ Throw Exception when transfer is not possible
	"""
    def __init__(self, msg):
        self.msg = msg
        super(TransferException, self).__init__(msg)

    def __str__(self):
        """ get a string representation of Exception
		"""
        return self.msg
