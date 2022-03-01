import random, sys

class colours:
    RIGHT = "\x1b[1;42m" # green
    ORANGE = "\x1b[48;5;166m" # orange
    WRONG = '\033[2m' # faded
    INVERT = '\033[7m'
    ENDC = "\x1B[0m"
    BOLD = '\033[1m'


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Words():    

    def __init__(self):

        self.all_words = []

        with open(sys.argv[0][:-8]+"answers.txt", "r") as words_file: # selecting an answer from common words (getting path and cutting off start.py)
            self.temp_answers = words_file.readlines()
            self.answers = [i.strip() for i in self.temp_answers] # stripping the newline characters
            self.answer = random.choice(self.answers).strip().upper() # selecting a random answer from the words

        with open(sys.argv[0][:-8]+"words.txt", "r") as words_file: # all accepted guesses (getting path and cutting off start.py)
            self.temp_words = words_file.readlines()
            self.all_words = [i.strip() for i in self.temp_words] # stripping the newline characters

        self.corr_letters = []
        self.incorr_letters = []

  

    def guess(self, guess):

        self.letter_count = {}
        # setting up counts of each letter for the word every time (so it is refreshed for each word)
        
        for letter in alphabet:
            self.letter_count[letter] = self.answer.count(letter)


        corr_letters_count = {}
        for i in range(5): # getting count of letters in guess

            if guess[i] in self.answer: # incrementing this value for each right or nearly right letter

                try:
                    corr_letters_count[guess[i]] += 1 
                except KeyError:
                    corr_letters_count[guess[i]] = 1




        ans = "" # this is the formatted value that gets printed out after

        for i in range(5): 
            if guess[i] == self.answer[i]: # this is the same as below, but just prioritises completely right letters even if they turn orange
                self.letter_count[guess[i]] -=1 # decrement the available letter count

            
        for i in range(5):
            if guess[i] == self.answer[i]: # if exactly right

                ans+= (colours.RIGHT + colours.BOLD + guess[i] + colours.ENDC)
                self.corr_letters += (guess[i]) # add to correct letter list for alphabet
                
                self.letter_count[guess[i]] -=1 # decrement the available letter count


            elif guess[i] in self.answer: # if letter in word but not right place


                if self.letter_count[guess[i]] > 0:
                    ans+= (colours.ORANGE + guess[i] + colours.ENDC) # if still in word, say orange
                else:
                    ans+= (colours.WRONG + guess[i] + colours.ENDC) # if wrong, say faint


                self.letter_count[guess[i]] -=1 # decrement the available letter count

                self.corr_letters += (guess[i]) # add to correct letter list



            else: # if letter not in word
                ans+= (colours.WRONG + guess[i] + colours.ENDC)

                self.incorr_letters += (guess[i]) # add to wrong letter list

        return ans