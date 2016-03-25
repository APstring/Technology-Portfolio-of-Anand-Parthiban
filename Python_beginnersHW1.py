print('Hello World') #Ex 1.1
 
print('  |  |''\n''--------''\n''  |  |''\n''--------''\n''  |  |') #Ex 1.2, prints out tictactoe
 
def tictactoe():
            	a = '\n	|  | \n'
            	b = ' --------'
            	print( a,b,a,b,a) #Ex 1.3 I made a function so that it would be easier to run, prints out tictactoe
 
a = (3*5)/(2+3), print(a) #Ex 1.4 part 2 1st
b = 2*((7+9)**0.5), print(b)#Ex 1.4 part 2 2nd; had to use powers instead of square roots
c = (4-7)**3, print(c)#Ex 1.4 part 2 3rd
d = (-19 + 100)**(0.25), print(d)#Ex 1.4 part 2 4th
e = 6%4, print(e)#Ex 1.4 part 2 5th
 
(3+2)*(4+5), 3+2*4+5 #Ex 1.4 part 3; 1st evaluates to 45, 2nd evaluates to 16
# Ex. 1.5
fname = input("Enter your first name:")
lname = input("Enter your last name:")
print('Enter your date of birth:')
m = input("Month?")
d = input("Day?")
y = input("Year?")
print(fname, lname,'was born on', m, d,',',y)
 
#As suggested by the homework, I went on to do 1.9-1.11 and continued through till 1.15 before continuing with the rest of the problems.
#Ex 1.9 problems
#1. and: since 'and' is an existing phrase in Python with it's own syntax, it would be unfit for naming a variable.
#2. _and: This name is legal due to the underscore before 'and'
#3.var:This name is legal; no existing phrase 'var' in-built into python
#4.var1:This name is legal
#5.1var:The '1' in front of var causes an error as an integer can't be in a string in the beginning
#6.my-name:The dash causes 'my' and 'name' to be treated as separate so the phrase can't be used in assignment
#7.your_name: This name is legal; the underscore between ' your' and 'name' allows for this phrase to be unrelated to any inbuilt phrases in python
#8.COLOR: This name is legal; the casing of the letters does not affect assignment, unless changing the casing causes the phrase to gain a meaning, such as with 'class' and 'Class'
 
#Ex 1.10 problems
#1. a = False: This is a boolean value
#2. b = 3.7:This is a float value since 3.7 has a decimal place
#3. c = 'Alex': This is a string since the phrase is surrounded by quotes
#4. d = 7: This is an integer since the input is an number that is whole
#5. e = 'True': This is a string due to the quotes surrounding the phrase
#6. f = 17: This is an integer since the input is a whole number
#7. g = '17':This is a string since the phrase is surrounded by quotes
#8. h = True: This is a boolean value since the input is the phrase True
#9. i = '3.14159': This is a string since the phrase is surrounded by quotes
 
#Ex 1.11
#1. The girl saw a boy on a hill, and the boy was using a telescope.
#2. The girl saw a boy on a hill, and this girl was using a telescope to see the boy.
#3.Above sentences act as a description and answers this part
#4. Most programming languages are designed to have a preset order of events that occur in the code, similar to an order of operations, which tells the program how to run and when to run, cutting out ambiguity from trying to think which order the programs would be executed in.
 
#Ex. 1.12
a = False
b = True
c = False
#1. b and c: is True and False; something can't be simultaneously true and false, so False is produced
#2. b or c: is True or False; an occurrence can be true or false, so since there is freedom in the choice, it's True
#3. not a and b: is not False and True; True means not false, so output is True
#4.(a and b) or not c: is (False and True) or not False; True and False becomes False, which leads to False or not False; since something can be either false or not false, output is true
#5.not b and not(a or c): is not True and not(False or False); False or False becomes false, so becomes not true or not false, which becomes True or False; True or False leads to the True output since either is possible
 
#Ex. 1.13
#1. Massachusetts, 50,000: No way; Massachusetts requires 100,000 for work, otherwise not taken
#2. Iowa, 50,000: No thanks, I can find something better;
#3.California, 50,000: "I’ll take it!"
#4. U.S.S. Enterprise, 1: So long, suckers! I’ll take it!
#5. California, 25,000: No thanks, I can find something better
 
#Ex. 1.14
#1. prints 10, 9, 8, 7, 6, 5, 4; since it is a while loop, it loops until condition is not met which is that num <= 3
#2. prints 0, 1.0, 2.0, 3.0, 4.0; since range(0,10,2) means range of 0 to 10 for every even number in the range, with every number of that range divided by two and printed out
#3. prints 10, 9, 8 7; skips the num < 7 and prints the num, then reduces by 1, then repeats the while loop until num < 7 condition is fulfilled and breaks, which stops loop
#4. prints Letter #0 is S, Letter #1 is n, Letter #2 is o, Letter #3 is w, Letter #4 is !
 
#Ex. 1.15
#1. n is always equal to 10; i output(10, 5, 6, 3, 4, 2, 1, 2,1, ... alternating between 1 and 2)
#2.This code has an initial i that is set, acting as the input; the program outputs a number and loops based on whether the current number is even or odd. This program appears to have two problems: n has no relevance to this program and this program doesn't end. To fix that, the while loop could have i>1 as the condition; n could just be removed from the program since it has no relevance.
 
#Returning to problems 1.7- 1.8(Ex. 1.6 has no problems, just examples)
#Ex. 1.7
 
 
""" Player 1: R  P  S  R  P  S  R  P  S
 
	Player 2: R  P  S  P  S  R  S  R  P
 
	Outcome: For Player 1- Tie(first 3), Lose(middle 3), Win(Last 3)
        	For Player 2- opposite #not a doctest"""
 
player1 = input('Player 1?')
player2 = input ('Player 2?')
 
if player1 == 'rock' and player2 == 'scissors':
	print('Player 1 wins.')
elif player1 == 'scissors' and player2 == 'paper':
	print('Player 1 wins.')
elif player1 == 'paper' and player2 == 'rock':
	print('Player 1 wins.')
elif player1 == 'rock' and player2 == 'paper':
	print('Player 2 wins.')
elif player1 == 'paper' and player2 == 'scissors':
	print('Player 2 wins.')
elif player1 == 'scissors' and player2 == 'rock':
	print('Player 2 wins.')
elif player1 == player2:
	print('Tie game')
else:
	print('This is not a valid object selection.')
# have to input as a string since only input is available
 
#Ex. 1.8
#part 1:
for num in range(2,11):
	print(1/num)
#part 2:
n = eval(input('Starting number?'))
if n < 0:
	print("Can't countdown to zero from a negative number!")
while n > -1:
            		print(n)
            		n -= 1
#part 3:
b = eval(input("What is your base?"))
e = eval(input("What is your exponent?"))
print(pow(b,e))
#part 4:
n = eval(input("Enter an even number."))
while n%2 != 0:
    print('\n'"Sorry, try again.")
	n = eval(input('\n'"Enter an even number."))
print('\n'"You did it!")
 
#Ex. OPT.1
fname = input("Enter your first name:")
lname = input("Enter your last name:")
A = eval(input("What number month is your birthday?\ni.e. March = 1, April = 2, ..., December = 10, January = 11, February = 12"'\n'))
B = eval(input("What day of the month was your birthday?"))
C = eval(input("What is the year of the century you were born on?\nif January or February was submitted previously, enter the number corresponding to the year before the desired year."'\n'))
D = eval(input("What century were you born in?(Enter a two-digit number i.e. for 1900s, input 19 for 19th century"'\n'))
W = (13*A - 1)/5
X = C/4
Y = D/4
Z = W + X + Y + B + C - 2*D
R = Z%7
while R < 0:
	R = R + 7
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']#used a list to simplify process
print(fname, lname,'was born on a',day[round(R)])

