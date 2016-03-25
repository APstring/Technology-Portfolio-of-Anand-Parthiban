import doctest
from operator import sub,mul
#Question 1:
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    return n if n < 4 else g(n-1) + 2*g(n-2) + 3*g(n-3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    n1,n2,n3 = 1,2,3
    if n in range(1,4):
        return n
    while n > 3:
        n1,n2,n3 = n2, n3, n3+2*n2+3*n1
        n = n-1
    return n3

#Question 2:
def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k > 9:
        if not k%10 == 7:
            return has_seven(k//10)
    else:
        if not k == 7:
            return False
    return True

#Question 3:
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def make_pingpong(k,total,d):
        if k == n:
            return total
        else:
            if d == 1:
                return consecutive(k+1, total+d, d)
            else:
                return consecutive(k+1, total+d, d)
            
    def consecutive(k, total, d):
        if has_seven(k) or k%7 == 0:
            return make_pingpong(k, total, -1*d)
        else:
            return make_pingpong(k, total, d)
            
    return make_pingpong(1,1,1)

#Question 4:
def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def make_change(amount, k):
        if amount < 0:
            return 0
        elif amount == 0:
            return 1
        elif k > amount:
            return 0
        else:   
            return make_change(amount-k, k) + make_change(amount, 2*k)
    return make_change(amount,1)

#Question 5:
def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    if n > 0:
        middle = 6-(start+end)
        towers_of_hanoi(n-1,start,middle)
        print('Move the top disk from rod',start,'to rod',end)
        towers_of_hanoi(n-1,middle,end)
        
#Question 6:
def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return (lambda f: lambda x: f(f,x))(lambda f,x: 1 if x == 1 else x*f(f,x-1))

if __name__ == "__main__":
    doctest.testmod()
