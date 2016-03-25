# Hw1: OPT 2
#part 1
phrase = input("What message do you want to encrypt?"'\n')
shift = eval(input("What is your key value?"'\n'))
x = []
for let in phrase:
    x.append(chr(ord(let) + shift))
print("Your encrypted message is", ''.join(x)) # Looked up how to combine list elements into a single string 

#part 2:Everything becomes x or X
phrase = input("What message do you want to encrypt?"'\n')
shift = eval(input("What is your key value?"'\n'))
x = []
for let in phrase:
    if ord(let) in range(65, 91):
        x.append('X')
    elif ord(let) in range(97,123):
        x.append('x')
    elif ord(let) == 32:
        x.append(chr(32))
    else:
        print('You cannot do that')
        break
print("Your encrypted message is", ''.join(x))
#part 3
phrase = input("What message do you want to encrypt?"'\n')
shift = eval(input("What is your key value?"'\n'))
x = []
for let in phrase:
    if ord(let) in range(65,91):
        if (ord(let) + shift) > 90:
            x.append(chr(((ord(let) +shift)%91) + 65))
        else:
            x.append(chr(ord(let) +shift))
    elif ord(let) in range(97,123):
        if (ord(let) + shift) > 122:
            x.append(chr(((ord(let) +shift)%123) + 97))
        else:
            x.append(chr(ord(let) +shift))
    else:
        x.append(chr(ord(let)))
print('Your encrypted message is', ''.join(x))            
# Hw2 (piglatin and cumulative function were omitted due to syntax errors in those functions that require closer inspection; those problems will be turned in for the next HW)
#2.1
def RPS(player1, player2): # inputs must be string values
    """ doctest
    >>> RPS('rock', 'paper')
    'Player 2 wins'
    >>> RPS('rock', 'rock')
    'Tie game'
    >>> RPS('bike', rock)
    'This is not a valid object selection.'
                                       """
    if player1 == 'rock' and player2 == 'scissors':
        return('Player 1 wins.')
    elif player1 == 'scissors' and player2 == 'paper':
        return('Player 1 wins.')
    elif player1 == 'paper' and player2 == 'rock':
        return('Player 1 wins.')
    elif player1 == 'rock' and player2 == 'paper':
        return('Player 2 wins.')
    elif player1 == 'paper' and player2 == 'scissors':
        return('Player 2 wins.')
    elif player1 == 'scissors' and player2 == 'rock':
        return('Player 2 wins.')
    elif player1 == player2:
        return('Tie game')
    else:
        return('This is not a valid object selection.')

#2.2
#part 1
def is_divisible(m,n):
    """
    >>> is_divisible(9,9)
    True
    >>> is_divisible(14,7)
    True
    >>> is_divisible(15,4)
    False
    >>> is_divisible(1,2)
    False
    >>> is_divisible(-14,7)
    True

                                         """
    return True if m%n == 0 else False 
    
#part 2
def not_equal(x,y):
"""
    >>> not_equal('rock', 'rock')
    False
    >>> not_equal(8,0)
    True
    >>> not_equal(6, 3*2)
    False
    >>> not_equal('rock', 4)
    True
                                    """
    return False if x == y else True

#Ex. 2.3
#part 1
import math
def multadd(a,b,c):
    return a*b + c
"""
#part 2
#given by Excercise
>>>multadd(1/2, math.cos((math.pi)/4),math.sin((math.pi)/4))
1.06066017178
>>>multadd(2, math.log(12,7), math.ceiling(276/19))
17.5539788165"""

#part 3
def yikes(x):
    b = pow(math.e, -x)
    a = multadd(x, b, pow((1 - b), 0.5))
    return a
"""
>>> yikes(5)
1.0303150673
>>> yikes(0)
0.0
>>> yikes(math.pi)
1.1139149544737825
"""
#Ex. 2.4
#part 1: no input, output is rand
import random
def rand_divis_3():
    a = random.randint(0,100) # suggested range
    print(a)
    return True if a%3 == 0 else False

#part 2: no docstr since output is rand
def roll_dice(a,b):
    k = 1
    while k <= b:
        k += 1
        c = random.randint(1, a)
        print(c)
    print("That's all!")
        
#Ex. 2.5
def quadratic(a, b, c):
"""
>>> quadratic(1,2,1)
(-1.0, -1.0)
>>> quadratic(7,8,9)
Error: Cannot compute complex numbers
>>> quadratic(5,3,0)
(-0.6, 0)
>>> quadratic(0,6,4)
-0.6666666666
"""
    disc = pow((b**2) - 4*a*c,0.5)
    if a == 0:
        return -c/b
    elif c == 0:
        return (min(0,-b/a), max(0, -b/a))
    elif (b**2 - 4*a*c) < 0:
        print('Error: Cannot compute complex numbers')
    elif disc == 0:
        return -b/(2*a)
    else:
        return (min((-b - disc)/2*a,(-b + disc)/2*a), max((-b - disc)/2*a,(-b + disc)/2*a))
#Ex. 2.6
def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
	player = 1
	print(str(pile) + "rocks in a pile")
	while pile > 0:
		init = False
		while init == 0:
		    screen = ("Player",str(player), "choose how many rocks you want to take from one to", str(max_stones))
		    rocks = input(screen)
		    rock_num = input(rocks)
		    if 1 <= rock_num and rock_num <= max_stones:
			init = True
		    else:
			print('Try again')
		pile = pile - rock_num
		if pile == 0:
		    print ('Player', player, 'has won.')
		    return
		else:
		    print(pile,'rocks remain.')
		if player == 1
			player = 2
		else:
		    player = 1
#Continuing with written excercises then returning to main HW
#Warm up:
#To be mutable means that the values of the item can be altered, while being immutable means that the values of the item cannot be altered by an outside method or process
#Ex. 2.11
# 1. Look; [:4] means all elements less than 4, which means elements 0 through 3, which spell out Look
#2. !; a negative element is going backwards in the list
#3. Look at me! Look at me! ; doubling a string repeats it twice
#4. Look at meNOW! ; range[:neg num] is the the word repeated from first letter to end of range; now is printed; neg 1 element of look is !
#5. O; first element means second in list
#6.N; fourth element of NOW doesn't exist unless the word goes through the elements again
#7. Look at me!Look at me!Look at meNOW! ; combination of previous EX
#Ex. 2.12
#1. print(a_list[0])
#2. print(a_list[4])
#3. a_list.remove([0])
#   a_list
#4. for ele in a_list:
#        print(ele)
#5. a_list[::-1]; returns numbers in reverse order
#6. x = []
#   for ele in a_list:
#       x.append(3*ele)
#   x
#7. for ele in a_list:
#      if eval(ele)%2 == 0:
#            return True
#       else:
#          return False

#Ex. 2.8:
def report_card():
    k = 0
    grad_clas = []
    nam_clas = []
    num_clas = eval(input('How many classes did you take?')
    for elle in range(num_clas):
         nam_clas.append(input('What name does this class have?'))
         grad_clas.append(eval(input('What was your grade?')))
    print('\n''Report Card')
    for ele in range(num_clas):
        print (nam_clas[ele], '-', grad_clas[ele])
    print('GPA is',(sum(grad_clas))/num_class)
                    
#Ex. 2.10: 
#part 1
cubes = []
for ele in range(10):
    cubes.append(10**3)
#part 2: 
coinflip = ['h', 't']
coinflip_total = []
    for ele in coinflip:
        if ele == 'h':
            coinflip_total.append(''.join([ele,'t']))
            coinflip_total.append(''.join([ele,'h']))
        elif ele == 't':
            coinflip_total.append(''.join([ele,'t']))
            coinflip_total.append(''.join([ele,'h']))
        print(coinflip_total)
#part 3: 
def vowl(): # could easily change code so that there is a parameter for doc test, but already tested; works
	string = input("What's your string?")
	vowels = []
	for ele in string:
		if ord(ele) == 97:
			vowels.append(ele)
		elif ord(ele) == 65:
			vowels.append(ele)
		elif ord(ele) == 101:
			vowels.append(ele)
		elif ord(ele) == 69:
			vowels.append(ele)
		elif ord(ele) == 105:
			vowels.append(ele)
		elif ord(ele) == 73:
			vowels.append(ele)
		elif ord(ele) == 111:
			vowels.append(ele)
		elif ord(ele) == 79:
			vowels.append(ele)
		elif ord(ele) == 117:
			vowels.append(ele)
		elif ord(ele) == 85:
			vowels.append(ele)
	return vowels
#part 4: 
[x+y for x in [10,20,30] for y in [1,2,3]]
#adds every y to every value of x making a list of 9 values
x = [10,20,30]
y = [1,2,3]
x_plus_y = []
for ele in x:
    for elle in y:
        x_plus_y.append(ele + elle)
print(x_plus_y)            
