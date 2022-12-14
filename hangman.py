# Problem Set 2, hangman.py
# Name: Cherniak Sviatoslav 
# Collaborators: None 
# Time spent: One long nigth

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from functools import reduce
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_list = reduce(lambda x,y: x + list(y), secret_word, [])
    
    secret_word_set = set(secret_word_list)


    for i in secret_word_set:
        if i not in letters_guessed:
            return False


    return True
    # FILL IN YOUR CODE HERE AND DELETE "pass"
  



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    game_string = ''
    for leter in secret_word:
        if leter in letters_guessed:
            game_string += leter
        else :
            game_string += '_ '

    return game_string
  
  
       

        
    


      


    


     

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    



def get_available_letters(letters_guessed, available_letters):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    for letter in letters_guessed:
        available_letters = available_letters.replace(letter,'')

    return available_letters


    # FILL IN YOUR CODE HERE AND DELETE "pass"

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    
    '''
    letters_guessed = []
    print(f'Welcome to the game Hangman !\nI am thinking of a word that is {len(secret_word)} letters long')
    
    warnings = 3
    guesses = 6

    while guesses > 0 or warnings > 0:
        print('------------------')
        print(f'You have {warnings} warnings left \nYou have {guesses} guesses left\nAvailable letters:   {get_available_letters(letters_guessed, available_letters)}')
        letter = input('Please guess a letter: ')
        letters_guessed.append(letter.lower())

        if warnings == 0:
            break
        if letters_guessed[-1] not in available_letters:
            warnings -= 1
        if letters_guessed.count(letters_guessed[-1]) != 1 :
            print(f'YOU GUESED SAME LETTER.\nYou have {warnings} WARNINGS left!!!!!')
            guesses -= 1
            continue


        else:
            print(f'YOU GUESED WRONG LETTER.\nYou have {warnings} WARNINGS left!!!!!')




        if letter in secret_word:

            print(f'Nice shot : {get_guessed_word(secret_word, letters_guessed)}')
        else:
            if letter in ['a','e','i','o','u'] and letters_guessed[-1] not in letters_guessed:
                guesses -= 2
            else:
                guesses -= 1

            print(f'Nice try, but you miss: {get_guessed_word(secret_word, letters_guessed)} ')



        if '_ ' not in get_guessed_word(secret_word, letters_guessed):
            break

    if is_word_guessed(secret_word, letters_guessed):
        print(
            f'Congratulations ,you won!\n Your total score for this game is: {guesses * len(set(reduce(lambda x, y: x + list(y), secret_word, [])))}.\nAs you know word about what i was thinking about is {secret_word}')
    else:
        print(f'You lose!\nYou have not any guesses or warnings goodluck next time!\nThe word i was thinking is {secret_word}.')




    
    # FILL IN YOUR CODE HERE AND DELETE "pass"




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = re.sub('[ ]', '',my_word)
    my_word_set = set(my_word)
    if len(my_word) == len(other_word):
        for index, letter in enumerate(my_word):
            if letter == '_':
                if other_word[index] in my_word_set:
                    return False
            else:
                if other_word[index] != letter:

                    return False
    else:
        return False

    return True






    # FILL IN YOUR CODE HERE AND DELETE "pass"




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    posible_words = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            posible_words.append(other_word)




    return posible_words if len(posible_words) != 0 else f'No matches found'








    # FILL IN YOUR CODE HERE AND DELETE "pass"



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    print(f'Welcome to the game Hangman !\nI am thinking of a word that is {len(secret_word)} letters long')

    warnings = 3
    guesses = 6

    while guesses > 0:
        print('------------------')
        print(
            f'You have {warnings} warnings left \nYou have {guesses} guesses left\nAvailable letters:   {get_available_letters(letters_guessed, available_letters)}')
        letter = input('Please guess a letter: ')
        letters_guessed.append(letter.lower())
        if letter == '*':
            print(f'Posible word mathces are: ', show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
            continue

        if warnings == 0:
            break
        if letters_guessed[-1]  not in available_letters:
            warnings -= 1

            if letters_guessed.count(letters_guessed[-1]) != 1:
                print(f'YOU GUESED SAME LETTER.\nYou have {warnings} WARNINGS left!!!!!')
                guesses -= 1
                continue


            else:
                print(f'YOU GUESED WRONG LETTER.\nYou have {warnings} WARNINGS left!!!!!')
                guesses -= 1

        if letter in secret_word:
            print(f'Nice shot : {get_guessed_word(secret_word, letters_guessed)}')
        else:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                guesses -= 2
            else:
                guesses -= 1

            print(f'Nice try, but you miss: {get_guessed_word(secret_word, letters_guessed)}')



        if '_ ' not in get_guessed_word(secret_word, letters_guessed):
            break

    if is_word_guessed(secret_word, letters_guessed):
        print(
            f'Congratulations ,you won!\n Your total score for this game is: {guesses * len(set(reduce(lambda x, y: x + list(y), secret_word, [])))}.\nAs you know word about what i was thinking about is {secret_word}')
    else:
        print(
            f'You lose!\nYou have not any guesses or warnings goodluck next time!\nThe word i was thinking is {secret_word}.')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
  
  
  
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    available_letters =  string.ascii_lowercase
    secret_word = choose_word(wordlist)


    

    
    
    #print(hangman(secret_word)


    

    
    
    
    
    
    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    


    hangman_with_hints(secret_word)
