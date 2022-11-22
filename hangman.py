
# helper code
MAX_GUESSES=6

secret_word='claptrap' #[c,l,a,p,t,r]
secret_list=list(set(list(secret_word))) #convert the list to a distinct list
letters_guessed=['a','g','h','k','t','r','p','l','o']
mistakes_made=0
letters_guess_right=[]


def word_guessed():
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

print(word_guessed())

 

'''
dir()
a=5
dir()
b=3
c=7
a=14
dir()
from string import *
dir()'''
