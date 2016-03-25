import doctest

# Question 1
def make_withdraw(balance):
    """Return a withdraw function with BALANCE as its starting balance.
    >>> withdraw = make_withdraw(1000)
    >>> withdraw(100)
    900
    >>> withdraw(100)
    800
    >>> withdraw(900)
    'Insufficient funds'
    """
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
           return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    k = 3
    lst = []
    def withdraw(amount, phrase):
        nonlocal balance
        nonlocal password
        nonlocal k
        nonlocal lst
        while k > 0:
            if phrase == password:
                if amount > balance:
                    return 'Insufficient funds'
                balance = balance - amount
                return balance
            else:
                k -= 1
                lst.append(phrase)
                return 'Incorrect password'
        return ('Your account is locked. Attempts: ' + str(lst))
    return withdraw

# Question 2:
def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    account = withdraw(0, old_password)
    if type(account) == str:
        return account
    def joint(amount, phrase):
        if phrase == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, phrase)
    return joint

# Question 3:
class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    def __init__(self, product, cost):
        self.product = product 
        self.cost = cost
        self.balance = 0
        self.stock = 0
        
    def vend(self):
        if self.stock == 0:
            return 'Machine is out of stock.'
        else:
            if self.balance < self.cost:
                return 'You must deposit $' + str( self.cost - self.balance)+ ' more.'
            elif self.balance == self.cost:
                self.stock -= 1
                self.balance = 0
                return 'Here is your ' + self.product+'.' 
            else:
                self.stock -= 1
                money = self.balance - self.cost
                self.balance = 0
                return 'Here is your ' + self.product+ ' and $' + str(money)+' change.'
            
    def restock(self, stock):
        self.stock += stock
        return 'Current ' + self.product + ' stock: ' + str(self.stock)
    
    def deposit(self, amount):
        if self.stock > 0:
            self.balance += amount
            return 'Current balance: $'+str(self. balance)
        else:
            return 'Machine is out of stock. Here is your $'+str(amount)+'.'

# Question 4:
class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    >>> fussy_three = MissManners(3)
    >>> fussy_three.ask('add', 4)
    'You must learn to say please first.'
    >>> fussy_three.ask('please add', 4)
    'Thanks for asking, but I know not how to add'
    >>> fussy_three.ask('please __add__', 4)
    7
    """
    def __init__(self, machine):
        self.machine = machine
        
    def ask(self, phrase, *args):
        key = 'please '
        if not phrase.startswith(key):
            return 'You must learn to say please first.'
        real_phrase = phrase[len(key):]
        if not hasattr(self.machine, real_phrase):
            return 'Thanks for asking, but I know not how to ' + real_phrase
        return getattr(self.machine, real_phrase)(*args)

if __name__ == '__main__':
    doctest.testmod()
