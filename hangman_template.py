# Name: Amy
# Project 1: Hangman template
# hangman_template.py
# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words
WORDLIST_FILENAME = "C:\\Users\\marcy\\OneDrive\\Documents\\Python level 1\\Group project\\words.txt"
def load_words():
 """
 Returns a list of valid words. Words are strings of lowercase letters.
 Depending on the size of the word list, this function may take a while to finish.
 """
 print ("Loading word list from file...")
 # inFile: file
 inFile = open(WORDLIST_FILENAME, 'r')
 # line: string
 line = inFile.readline()
 # wordlist: list of strings
 wordlist = line.split()
 print (" ", len(wordlist), "words loaded.")
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

# From part 3b:
def word_guessed():
 '''
 Returns True if the player has successfully guessed the word,
 and False otherwise.
 '''
 global secret_word
 global letters_guessed
 ####### YOUR CODE HERE ######
 secret_list=list(set(list(secret_word))) #convert the list to a distinct list
 for letter in letters_guessed:
    if letter in secret_list:
        letters_guess_right.append(letter)
        print(letter)

 letters_guess_right.sort()
 secret_list.sort()

 if letters_guess_right==secret_list:
    return True
 else:
    return False

 #pass # This tells your code to skip this function; delete it when you
 # start working on this function

def print_guessed():
 '''
 Prints out the characters you have guessed in the secret word so far
 '''
 global secret_word # = "hello"
 global letters_guessed # = [a h e l o ]

 #
 hump = ''
 for i in range(len(secret_word)):
    if secret_word[i] in letters_guessed:
        #print(secret_word[i], end='')
        hump += secret_word[i]
    else:
        #print('_', end='')
        hump += '_'
 
 print(hump)
 if hump==secret_word:
     print('Yay! you got the secret word!')

 print()
 return hump

def play_hangman(): #by Amy
 # Actually play the hangman game
 global secret_word
 global letters_guessed
 # Put the mistakes_made variable here, since you'll only use it in this function
 mistakes_made = 0
 guesses_left=MAX_GUESSES
 while guesses_left > 0:
    # max_guessed minus i = how many guesses left
    #guesses_left=MAX_GUESSES-i
    print(f"{guesses_left} guess(es) left.")
    input_letter = input('Please guess a letter that you think is in the word: ')

    
    #Check if input_letter is a valid letter?
    #Case 1: check if length is 1
    if(len(input_letter) > 1):
        print('Please enter single letter only')
        continue
    #Case 2: check if letter is allready guessed
    if input_letter in letters_guessed:
        print('You allready guessed this letter. Please enter a different letter.')
        continue

    #Add letter to letters_guessed list
    letters_guessed.append(input_letter)
    #update guesses left
    guesses_left = guesses_left - 1
    
    #Check if letter is in the secret word
    if input_letter in secret_word:
        print(f'Good guess! {input_letter} is in the secret word!')
    else:
        mistakes_made += 1
        print(f'BAD guess! {input_letter} is NOT in the secret word!')


    hump = print_guessed()
    if(hump == secret_word):
        break

 

 return None

'''---------------------------------------------------------------------'''


# GLOBAL VARIABLES
secret_word = get_word()
print(secret_word)
# CONSTANTS
MAX_GUESSES = len(secret_word)

letters_guessed = []
letters_guess_right=[]
play_hangman()

 