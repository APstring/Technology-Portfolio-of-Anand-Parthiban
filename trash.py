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

def Root(poly, x_0, epsilon):
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
    return [x_0,count]
    
def main():
    poly = [-13.39, 0.0, 17.5, 3.0, 1.0]    
    #poly=[1]
    x_0 = 0.1
    epsilon = .0001
    print(Root(poly, x_0, epsilon))    
            
if __name__ == '__main__':
    main()
