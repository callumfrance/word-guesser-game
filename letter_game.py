from random import shuffle, randrange
import sys

words = list() # Global variable that contains all of the words

class GameStats:
    """Class that contains game states and manages the game state
    """

    def __init__(self, in_game_board=None):
        self.game_board = None
        self.board_cnt = 0
        self.correct = 0
        if (in_game_board):
            self.set_game_board(in_game_board)
        else:
            self.set_game_board(WordBoard())


    def set_game_board(self, in_game_board):
        self.game_board = in_game_board


    def next_game_board(self):
        self.game_board = WordBoard()
        self.board_cnt = self.board_cnt + 1


    def process_correct(self):
        print("Correct")
        self.correct = self.correct + 1


    def print_stats(self):
        print("Correct guesses: " + str(self.correct))
        print("Boards generated: " + str(self.board_cnt))


    def play_game(self):
        # This is the 'view' of the game to the console for the player
        will_exit = False
        while(not will_exit):
            self.game_board.print_board()
            user_in = input('\n>')
            if ((user_in == '--ans') or (user_in == '--help')):
                print(self.game_board.ans_word)
                self.next_game_board()
            elif (self.game_board.check_answer(user_in)):
                self.process_correct()
                self.next_game_board()
            elif (user_in == '--exit'):
                print('Exiting...')
                self.print_stats()
                will_exit = True
            else:
                print("Not correct, try again")



class WordBoard:
    """Class that contains the word board and the correct word.
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


    def print_board(self):
        # This is how the board is represented in the console
        print('+-------+', end='')
        for i, n in enumerate(self.board):
            if (i % 3 == 0):
                print()
                print('|', end='')
            print(' ' + n, end='')
            if (i % 3 == 2):
                print(' |', end='')
        print()
        print('+-------+')



def import_words(fileName):
    # Import the 9-letter words into the program's memory from the word list
    with open(fileName) as fo:
        for line in fo:
            temp = line.rstrip()
            if(len(temp) == 9):
                words.append(temp)



if __name__ == '__main__':
    # Create the game object and then play the game
    if (len(sys.argv) == 2):
        fileName = sys.argv[1]
        print("Using " + fileName)
    else:
        fileName = 'popular9.txt'
        print("Using popular.txt")
    import_words(fileName)
    wb = WordBoard()
    gb = GameStats(wb)
    print("Starting")
    gb.play_game()
