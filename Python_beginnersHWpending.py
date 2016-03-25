

#Ex. 2.7: still working on
def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

def cumulative(x): # x is a list 
    """
    >>> cumulative([3,5,8])
    [3,8,13]
    >>> cumulative[7,0,4])
    [7,7,11]
    >>> cumulative([-9,7,4])
    [-9,-2,2]
    """
    k = 0
    for ele in x:
        if ele != x[0]:
            x.remove(x[k])
            x.append(sum_all([ele, x[k]]))
            k +=1
    print(x)           

#Ex. 2.9: working on
def piglatin():
    phrase = list(input("What do you want to translate?")) 
    for ele in phrase:
        if ele == phrase[0]:
            if ord(ele) == 97:
		phrase.append('hay')
	    elif ord(ele) == 65:
		phrase.append('hay')
	    elif ord(ele) == 101:
		phrase.append('hay')
	    elif ord(ele) == 69:
		phrase.append('hay')
	    elif ord(ele) == 105:
		phrase.append('hay')
	    elif ord(ele) == 73:
		phrase.append('hay')
	    elif ord(ele) == 111:
		phrase.append('hay')
	    elif ord(ele) == 79:
		phrase.append('hay')
	    elif ord(ele) == 117:
		phrase.append('hay')
	    elif ord(ele) == 85:
		phrase.append('hay')
            elif ord(ele) in range(66,91) or range(97,123):
                del phrase[0]
                phrase.extend(ele,+'ay')
            else:
                break
    print(''.join(phrase))


#OPT.1
#OPT.2
