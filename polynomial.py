# Question 7:
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
    lst = []
    zero = []
    
    #def make_polynomial(t, c):
     #   k = len(c)
      #  poly_list = []
       # while k > 0:
        #    poly_list.append(c[k-1]*pow(t,k-1))
         #   k -= 1
        #return sum(poly_list)
    lst.extend([evaluate(lower_bound(x),c), evaluate(upper_bound(x), c)])
    
def evaluate(poly, x):
    value=0.0
    for index in range(len(poly)):
        value  = value+(x**index)*poly[index]
    return value

def Deriv(poly):
    for index in range(len(poly)):
            poly[index]*=index
    poly.pop(0)
    if len(poly) == 0:
        poly.insert(0,0.0)
    return poly

def Root(poly, x_0 = 0.1, epsilon = 0.0001):
    value = (evaluate(poly,x_0))
    poly1=[]
    for num  in poly:
            poly1.append(num)    
    Deriv(poly1)
    count = 0
    while abs(value)  >= epsilon:
        derivalue=(evaluate(poly1,x_0))
        if derivalue == 0:
            x_0 = 0
            break
        x_0 = x_0 - (value/derivalue)
        value=(evaluate(poly,x_0))
        count += 1
    return [x_0]
    
    """def zeroes(c, x = 0.1, e = 0.0001):
        poly1 = make_polynomial(x, c)
        poly_c = []
        poly_c.extend(c)
        for num in range(1,len(c)):
            poly_c[num] *= num
            if len(poly_c) == 0:
                poly_c.append(0)
        del poly_c[0]
        while abs(poly1) >= e:
            der = make_polynomial(x, poly_c)
            if der == 0:
                x = 0
                break
            x -= (poly1/der)
            poly1 = make_polynomial(x, poly_c)
        return x
    """
    
    zero.extend(Root(c))
    for root in zero:
        if root > lower_bound(x) and root < upper_bound(x):
            lst.append(evaluate(c, root))
    return interval(min(lst), max(lst))
