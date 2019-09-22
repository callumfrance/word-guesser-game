from random import shuffle, randrange


class WordBoard:
    """Class that contains the word board and the correct word.
    """
    def __init__(self, in_words_file_name=None):
        # Take or generate a word, and also create a randomized copy too
        self.ans_word = None
        self.board = list()
        self.words = list()
        if (in_words_file_name):
            self.load_words(in_words_file_name)
        else:
            self.load_words()
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

    def load_words(self, in_words_file_name=None):
        # Loads words into object from filename, either provided or defaulted
        if (not in_words_file_name):
            in_words_file_name = 'wordlists/popular9.txt'
        with open(in_words_file_name) as fo:
            print("Opening " + in_words_file_name)
            for line in fo:
                temp = line.rstrip()
                if (len(temp) == 9):
                    self.words.append(temp)

    def generate_random_word(self):
        # This will pick a random word with `randrange` from the words.txt file
        temp = self.words[randrange(0, len(self.words) - 1)]
        self.set_word(temp)

    def print_board(self):
        # This is how the board is represented in the output
        board_str = "+-------+"
        for i, n in enumerate(self.board):
            if (i % 3 == 0):
                board_str = board_str + "\n|"
            board_str = board_str + " " + n
            if (i % 3 == 2):
                board_str = board_str + " |"
        board_str = board_str + "\n+-------+"
        return (board_str)

    def print(self):
        # Prints details about the wordboard object
        print("in word file name : " + str(in_words_file_name))
        print("WordBoard: " + str(len(self.words)) + "\t" + self.ans_word)
