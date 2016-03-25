"""
def maxval(some_list): 
max_val = some_list(0)
for val in some_list: 
if val > max_val: 
max_val = val 
return max_val

def maxsix1(some_list):
index = 0
	for val in some_list:
		if val  >=  6:
			return False
		elif index == len(some_list)-1:
			return True
		index += 1

def maxsix2(some_list):
	for val in some_list:
		if val  >=  6:
			return False
	return True

def maxsix3(some_list):
	return maxval(some_list) >= 6

def minval(some_list): 
min_val = some_list(0)
for val in some_list: 
if val < min_val: 
min_val = val 
return min_val

def minval2(some_list):
	lst = some_list 
	lst.sort()
	return lst[0]

def maxval2(some_list):
	lst = some_list 
	lst.sort()
	return lst[-1]

def minsix(some_list):
	return minval2(some_list) < 6
"""
# Name:
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print ("  ", len(wordlist), "words loaded.")
    print ('Enter play_hangman() to play a game of hangman!')
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = '' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    lst = list(secret_word)
    for letter in letters_guessed:
        while lst.count(letter) > 0:
            lst.remove(letter)
    return lst == []


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    s = ' '
    for index in range(0,len(secret_word)):
        letter = secret_word[index]
        if letter in letters_guessed:
            s += letter
        else:
            s += '-'
    return s


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed 
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    secret_word = get_word()

    while mistakes_made < MAX_GUESSES and not word_guessed():
        print_hangman_image(mistakes_made)     
        print((MAX_GUESSES - mistakes_made), " guesses left")
        print(print_guessed())
        letter = lower(input("What is your guess?"))
        if letter in letters_guessed_notright:
            print("Already been used. Try again.")
        elif letter in secret_word:
            letters_guessed.append(letter)
        else:
            mistakes_made += 1

def lower(char):
	if char in ascii_uppercase:
		return ascii_lowercase[ascii_uppercase.index(char)]
	return char


  





