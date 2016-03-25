def gets_discount(x,y):
    if (x >= 65 and y <= 12) or (x <= 12 and y >= 65):
        print('True')
    else:
        print('False')

    
def is_factor(x,y):
    if x == 0 or y == 0:
        return True
    else:
        return False if y%x == 0 else True

def isit(x,y):
    return x != 0 and y%x == 0

def falling(n,k):
    a = 0
    total = 1
    while k > a:
        total, n = total*(n), n-1
        a += 1
    return total

def is_prime(n):
    k = n
    while k > 0:
       k -= 1
       False if 
