import doctest
from math import pi
#Question 1:
def harmonic(x, y):
    """Return the harmonic mean of x and y.
    >>> harmonic(2, 6)
    3.0
    >>> harmonic(1, 1)
    1.0
    >>> harmonic(2.5, 7.5)
    3.75
    """
    return 2/(x**-1 + y**-1)

#Question 2:
def pi_fraction(gap):
    """Print the fraction within gap of pi that has the smallest denominator.
    >>> pi_fraction(0.01)
    22 / 7 = 3.142857142857143
    >>> pi_fraction(1)
    3 / 1 = 3.0
    >>> pi_fraction(1/8)
    13 / 4 = 3.25
    >>> pi_fraction(1e-6)
    355 / 113 = 3.1415929203539825"""
    numerator, denominator = 3, 1
    while abs(numerator/denominator-pi) > gap:
        denominator += 1
        numerator = round(denominator*pi)
    print(numerator, '/', denominator, '=', numerator/denominator)

#Question 3:
def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0


    """
    power_of_two = 1.0
    isit = True
    while isit:
        if power_of_two < x:
            power_of_two = power_of_two*2
            if power_of_two > x or power_of_two == x:
                power_of_two, isit = power_of_two/1, False
            else:
                isit = True
        elif power_of_two > x:
            power_of_two = power_of_two/2
            if power_of_two < x or power_of_two == x:
                power_of_two,isit = power_of_two*2, False
            else:
                isit = True
        else:
            isit = True
    if power_of_two-x > x-(power_of_two/2):
        power_of_two = power_of_two/2
    return power_of_two

if __name__ == "__main__":
    doctest.testmod()
