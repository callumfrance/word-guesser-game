from random import shuffle, randrange

# Import the 9-letter words into the program's memory from the word list
words = list()
with open('words.txt') as fo:
    for line in fo:
        temp = line.rstrip()
        if(len(temp) == 9):
            words.append(temp)

class WordBoard:
    """Function that contains the word board and the correct word.
    """


    def __init__(self, in_word=None):
        # Take or generate a word, and also create a randomized copy too
        self.ans_word = None
        self.board = list()
        if (in_word):
            self.set_word(in_word)
        else:
            self.generate_random_word()

    def set_word(self, in_word):
        # The answer word's mutator - also scrambles too
        if (len(in_word) == 9):
            self.ans_word = in_word
            self._tile_scrambler()

    def _tile_scrambler(self):
        # Private function to scramble the answer word
        temp_copy = list(self.ans_word)
        shuffle(temp_copy)
        self.board = ''.join(temp_copy)

    def check_answer(self, to_check):
        # Function that will check if a guess matches the answer word
        is_correct = False
        if (to_check == self.ans_word):
            is_correct = True
        return is_correct

    def generate_random_word(self):
        # This will pick a random word with `randrange` from the words.txt file
        temp = words[randrange(0, len(words)-1)]
        self.set_word(temp)


def print_board(in_board):
    # This is how the board is represented in the console
    print('+-------+', end='')
    for i, n in enumerate(in_board):
        if (i % 3 == 0):
            print()
            print('|', end='')
        print(' ' + n, end='')
        if (i % 3 == 2):
            print(' |', end='')
    print()
    print('+-------+')

    
def play_game(wb):
    # This is the 'view' of the game to the console for the player
    the_guess = False
    while(not the_guess):
        print_board(wb.board)
        user_in = input('\n>')
        if ((user_in == '--ans') or (user_in == '--help')):
            print(wb.ans_word)
            the_guess = True
        elif (wb.check_answer(user_in)):
            print("Correct")
            the_guess = True
        else:
            print("Not correct, try again")


if __name__ == '__main__':
    # Create the game object and then play the game
    wb = WordBoard()
    print("Starting")
    play_game(wb)
