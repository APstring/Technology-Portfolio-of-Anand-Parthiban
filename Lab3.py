def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    def buzz(m):
        i = 0
        while i < m:
            if i%n == 0:
                print('Buzz!')
            else:
                print(i)
            i += 1
    return buzz 

def f1():
    return 3

def f2():
    return lambda: 3

def f3():
    return lambda x: x

def f4():
    return  lambda: lambda x: lambda: x
        
#Part 1\na= lambda x: x*2 + 1\n defb(x):\nreturn x*y\ny=3\nresultb(y)recallb(x)= y*y y= 3 3*3= 9 return 9
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def hailstone(n, k = 1):
    print(n)
    if n == 1:
        return k
    else:
        k += 1
        if n%2 == 0:
            return hailstone(n/2, k)
        else:
            return hailstone(3*n +1,k)
    

def cycle(f1, f2, f3):
    def make_cycle(n):
        if n == 0:
            return n
        elif n%3 == 0:
            return make_cycle(f3(n-1))
        elif (n-1)%3 == 0:
            return make_cycle(f2(n-1))
        elif (n-2)%3 == 0:
            return make_cycle(f1(n-1))
        return n


