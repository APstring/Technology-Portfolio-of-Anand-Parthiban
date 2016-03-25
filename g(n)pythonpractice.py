def g_iter(n):
    total = 0
    a = 0
    b = 0
    c = 0
    while a or b or c > 3:
        total, n, a, b, c = total + n, a + b + c, a + (n-1), b + 2 * (n-2), c + 3* (n-3)   
        return [total, n, a, b, c]
    print (total)


    
