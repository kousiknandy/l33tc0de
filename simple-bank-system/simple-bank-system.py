class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.ledger = balance[:]
        self.accs = len(balance)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        account1, account2 = account1-1, account2-1
        if account1 >= self.accs: return False
        if account2 >= self.accs: return False
        if self.ledger[account1] < money: return False
        self.ledger[account1] -= money
        self.ledger[account2] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        account -= 1
        if account >= self.accs: return False
        self.ledger[account] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        account -= 1
        if account >= self.accs: return False
        if self.ledger[account] < money: return False
        self.ledger[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
