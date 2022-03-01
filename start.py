import game as wordle
import os
from time import sleep

py_dic = False
try:
    from PyDictionary import PyDictionary
    py_dic = True
except:pass

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout


if py_dic:
    dictionary=PyDictionary() # dictionary


def clear(): os.system('cls' if os.name == 'nt' else 'clear')

print("Collecting wordle words...")

words = wordle.Words()
colours = wordle.colours()
print(words.answer)
clear()


guess_number = 1

guess = ""
output = ["", ""] # placeholder for alphabet


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

clear()


while guess != words.answer and guess_number<=6:

    guess = input(f"Guess {guess_number}/6: ") # allow user to guess
    guess = guess.strip().upper() # strip and upper it
    

    if guess.lower() in words.all_words or guess.lower() in words.answers:
        # the word is valid but not right

        guessed = words.guess(guess) # formatted guess display from wordle file
        output.append(f"Guess {guess_number}/6: {guessed}") # adding the number and guessed word to the output 

        if guess != words.answer:
            guess_number+=1 # increment guess number if guess not correct

        

    else:
        # the word is invalid

        if len(guess)!=5:

            print("Not right length.")
            sleep(0.5)
        else:
                
            print("Not a word")
            sleep(0.5)


    # colouring the alphabet at the top

    for each in words.corr_letters:

        if each.upper() in alphabet: alphabet[alphabet.index(each.upper().strip())] = (colours.RIGHT + each.upper() + colours.ENDC)

    for each in words.incorr_letters:

        if each.upper() in alphabet: alphabet[alphabet.index(each.upper().strip())] = (colours.WRONG + each.upper() + colours.ENDC)

 
    clear() # clear screen

    output[0] = ("".join([(i) for i in alphabet])) # adding alphabet to the output

    for i in output: # print the previous guesses
        print(i)


clear()

for i in output:
    print(i)

print()

if guess_number<=6:

    print("\x1B[38;5;10m") # greeny text
    print(f"Yay! You got it in {guess_number}/6 guesses. ")
    print(colours.ENDC) # end character

else:

    print("\x1B[38;5;196m") # greeny text
    print(f"You didn't quite get it.")
    print(colours.ENDC) # end character

print()


print('\033[1m'+ words.answer.lower() +'\033[0m') # printing word in bold


# Printing word definition if possible
if py_dic:
    with suppress_stdout():
        meaning = None
        meaning = dictionary.meaning(words.answer)

    try:
        if meaning != None:
            for each in meaning: 

                print('\033[4m'+ each +'\033[0m') # printing the type of word (verb / noun) in underlined
                

                for each in dictionary.meaning(words.answer)[each]:
                    
                    print('\033[3m'+each + '\033[0m') # printing the definitions of the word in italics

                print()
        else:
            print(colours.WRONG + "* No definition available.\n* Check your internet connection." + colours.ENDC)

    except:
        print(colours.WRONG + "* No definition available.\n* Check your internet connection." + colours.ENDC)

else:
    print(colours.WRONG + "* PyDictionary not available. Install via 'pip install PyDictionary'." + colours.ENDC)