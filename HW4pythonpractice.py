def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = upper_bound(x) * lower_bound(y)
    p3 = lower_bound(x) * upper_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1,p2,p3,p4), max(p1,p2,p3,p4))

def interval(a, b):
    """Construct an interval from a to b."""
    x = [a, b]
    return x

def lower_bound(x):
    """Return the lower bound of interval x."""
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    return x[1]

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    assert upper_bound(y) or upper_bound(y) == 0 , "division by zero"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y)) 
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    lower = upper_bound(y) - lower_bound(x)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))
    #par1 for (-3,0),(4,5) shows the interval to be (-15, 0), which is not right; probably due to simplification occuring at the the end of each function  
def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))
#par2 for (-3,0),(4,5) shows the interval to be not computed = division by zero; checks to divide by zero or not

def quadratic(x, a, b, c):
    y0 = a*(pow(x[0],2)) + b*(x[0]) + c
    y1 = a*(pow(x[1],2)) + b*(x[1]) + c       
    h = ((-b)/(2*a))
    k = a*(pow(h,2)) + b*(h) + c
    if a < 0:
        if x[0] > h or x[1] < h:
            return interval(y0, y1)
        elif x[0] < h and x[1] > h:
            return interval(min(y0,y1), k)
    elif a > 0:
        if x[0] > h or x[1] < h:
            return interval(y0, y1)
        elif x[0] < h and x[1] > h:
            return interval(k, min(y0, y1))

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    


