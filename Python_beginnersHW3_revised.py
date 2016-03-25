#3.1
def list_intersection(x,y):
    """
    >>> list_intersection([1, 3, 5], [5, 3, 1])
    [1, 3, 5]
    >>> list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])
    [3, 9]
    >>> list_intersection([2, 3], [3, 3, 3, 2, 10])
    [3, 2]
    >>> list_intersection([2, 4, 6], [1, 3, 5])
    []
    """
	z = []
	for ele in x:
		if ele in y:
			z.append(ele)
	return z
    
#3.2
def ball_collide_three_D(x,y):
    """    
    >>> ball_collide_three_D([3,4,5,7],[2,6,1,2])
    True
    >>> ball_collide_three_D([6,2,9,3],[1,6,2,1])
    False
    >>> ball_collide_three_D([8,5,1.5,2],[4,8,0.5,1])
    True
    """
    true_distance = ((y[0]-x[0])**2 + (y[1]-x[1])**2 + (y[2]-x[2])**2)**0.5
    return (y[3]+x[3]) >= true_distance

#3.3
def print_classes(x): # input must be sting
    """
    >>> print_classes('3')
    3 - Stats
    >>> print_classes('9')
    No period 9 classes.
    >>> print_classes('2')
    2.5 - homeroom
    2 - PE
    """
    school = {'2':'PE','2.5':'homeroom' ,'3':'Stats', '4':'Human', '5':'French', '5.5':'Lunch', '6':'Chem', '7':'English'}
    for ele in school:
        if ele.startswith(x):
            print(ele, '-', school[ele])
        elif not x  in school.keys():
            print('No period', x,'classes.') 
            break 

#3.4
z = {}
def combine_lists(x,y):
    k = 0
    for ele in x:
        z[ele] = y[k]
        k += 1
"""
names = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank','Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
ages = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
>>> combine_lists(names,ages)
>>> people(21)
['Bob']
>>> people(25)
[]
>>> people(20)
['Frank','Alice','Gary']
"""
def people(age):
    y = []
    for ele in z.keys():
        if age == z[ele]:
            y.append(ele)      
    return y
#3.5
def zellers(x, y, z):
"""
>>> zellers('July',3, 2015)
Friday
>>> zellers('January',15, 2000)
Saturday
>>> zellers('March',30,1682)
Monday
"""
    month = {'March':1, 'April':2, 'May':3, 'June':4, 'July':5, 'August':6,'September':7, 'October':8, 'November':9, 'December':10, 'January':11, 'February':12} 
    A = month[x]
    B = y
    if month[x] == 12 or 11:
        C = (z%100)-1
    else:
        C = (z%100)
    D = z/100
    W = (13*A - 1)/5
    X = C/4
    Y = D/4
    Z = W + X + Y + B + C - 2*D
    R = Z%7
    while R < 0:
        R = R + 7
    day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']#used a list to simplify process
    right_day = day[round(R)]
    print (right_day)
#3.6
class Queue:
    def __init__(self):
        self.lists = []
    def remove(self):
        if len(self.lists) > 0: 
            print(self.lists[0])
            del self.lists[0]
        else:
            print('The queue is empty')
    def insert(self,x):
        self.lists.append(x)
#3.7
#Mutable: elements can be modified; lists, dictionaries  
#Immutable: elements can't be modified; strings, tuples  
#3.8
#1. for defining the function 'large_num', Ben needs to return the output, although the output isn't even there it's just an assignment: To fix it, simply add ' return' before 'res', delete ' res =' 
#2. In the line 'neg_b = num', Ben forgets that num is a parameter and has no meaning outside the function it was used to define, also, 'neg_b' is not 'negate(b)': the line 'negate(b)' should be changed to 'neg_b = negate(b)','neg_b = num' should be deleted, next line should read 'print('b:', b, 'neg_b:', neg_b) 
#3. both print functions will not function since there are no parentheses surrounding the desired print out: simply add parentheses around the statements that must be printed
#Extra: also, b is never assigned a value, so the functions would not be able to accept b as an input
#3.9
#1. If the first character of the input for raw_input('Is it', + str(mid_n) + '?') is y, then 'right answer' will be assigned to True. 
#2. 'Woohoo! I got it!' should only be printed out once after the while loop has ended
#3. 'answer' is assigned to the string response from raw_input and is used to determine which condition will be executed 
#4. the only responses that will be understood are any phrases that begin with y, higher, or lower 
#5. The actual number is higher than the estimate made by the program
#6. 'min_n', 'max_n', and 'mid_n' are all used to form an estimate that is used to guess what number the player is thinking; using the min_n and max_n values, it finds the middle value which is the average of min_n and max_n, and assigns that value to mid_n, and based on the response to the guess, it will either end the loop or change the value of min_n or max_n, unless the input was not correct
#3.10
#1. A local variable can only be used in the frame it is defined in for the function and has no meaning outside that frame unless it is modified so that it can be; an object's attributes can not only be used throughout the object, but it can be called upon when the object is called
#2. __init__ is the method that is called for constructing the new instance of a class when a new object is formed
#3. obj.do_something() 
#3.11
#1.
    class Address:
	def __init__(self, number, street_name): # street_name must be string
           self.number = number
           self.street_name = street_name

	def print_address(self):
            print(self.number,' ',self.street_name)          
#2.
#a)prints out 5:30
#b)It is expected since the time of 5:30 was previously set to self.time, so changing time to 6:30 afterwards doesn't affect the value of self.time. 
#3.
#a)The output is 10:30; print method has it's own time input seperate from __init__
#b)Using the parameter 'time' is not a great choice since it can be confusing when using print_time and when looking at print(time), although it is more distinguished when python 3 syntax is used
#4.
#a)The output is 10:30 
#b)Line 'paris_clock = boston_clock', the instance of boston_clock is assgined to paris_clock, which is different than assigning values because an instance is like a bank where data is stored. So, it's like two instances are sharing the same bank, so when one changes the value of it's instance for some method, it changes the other instance's as well.
#OPT.1
def is_palindrome(x):
"""
>>> is_palindrome('racecar')
True
>>> is_palindrome('popper')
False
>>> is_palindrome('book')
False
"""
	return True if x==x[::-1] else False
#OPT.2
class Stack:
    def __init__(self):
        self.stacks = []
    def pop(self):
        if len(self.stacks) > 0: 
            print(self.stacks[-1])
            del self.stacks[-1]
        else:
            print('The stack is empty')
    def push(self,x):
        self.stacks.append(x)
        
        
