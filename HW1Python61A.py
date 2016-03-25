import doctest
#Question 1:
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = lambda a,b: a-b
    else:
        f = lambda a,b: a+b
    return f(a, b)

#Question 2:
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return a**2 + b**2 + c**2 - min(a,b,c)**2

#Question 3:
def with_if_statement():
    """
    supposed to output 1 and hello because it is supposed to be different than doc test
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True

def t():
    print(1)
    return('hello')

def f():
    return 0

#Question 4:
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    k = 1
    while n > 1:
        print(n)
        k += 1
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n + 1
    print(n)
    return k

#Question 5:
"""
>>> x ='hello';print(x);print('bye'*2 + " see you later")
hello
byebye see you later
"""

if __name__ == "__main__":
    doctest.testmod()
