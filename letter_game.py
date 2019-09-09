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
        self.ans_word = None
        self.board = list()
        if (in_word):
            self.set_word(in_word)
        else:
            self.generate_random_word()

    def set_word(self, in_word):
        if (len(in_word) == 9):
            self.ans_word = in_word
            self._tile_scrambler()

    def _tile_scrambler(self):
        temp_copy = list(self.ans_word)
        shuffle(temp_copy)
        self.board = ''.join(temp_copy)

    def check_answer(self, to_check):
        is_correct = False
        if (to_check == self.ans_word):
            is_correct = True
        return is_correct

    def generate_random_word(self):
        temp = words[randrange(0, len(words)-1)]
        self.set_word(temp)

    
def play_game(wb):
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


def print_board(in_board):
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


if __name__ == '__main__':
    wb = WordBoard()
    print("Starting")
    play_game(wb)
