from .word_board import WordBoard
from json import dumps


class GameStats:
    """Class that contains game states and manages the game state
    """
    def __init__(self):
        self.board_cnt = 0 # Starts at 0 + 1 = 1 accounting for F5's
        self.correct = 0
        self.incorrect = 0
        self.failures = -1 # Starts at -1 + 1 = 1 accounting for F5's
        self.correct_words = list()
        self.failure_words = list()
        self.past_words = list()

    def process_correct(self):
        self.correct += 1
        self.board_cnt += 1
        self.correct_words.append(self.failure_words.pop())
        self.past_words.append(self.correct_words[-1])

    def process_failure(self, in_word):
        print("New failure")
        self.failures += 1
        self.board_cnt += 1
        self.failure_words.append(in_word)
        self.past_words.append(in_word)

    def process_incorrect(self):
        print("New incorrect")
        self.incorrect += 1

    def get_stats(self):
        stat_str = ["Correct guesses: ", str(self.correct)]
        stat_str += ["Incorrect guesses: ", str(self.incorrect)]
        stat_str += ["Passes: ", str(self.failures)]
        stat_str += ["Boards generated: ", str(self.board_cnt)]
        return(stat_str)

    def get_stats_json(self):
        stats_json = {
                "correct": self.correct,
                "incorrect": self.incorrect,
                "failures": self.failures,
                "correct_words": self.correct_words,
                "failure_words": self.failure_words[:-1],
                }
        x = dumps(stats_json, sort_keys=True, separators=(',', ':'))
        print("X is: ")
        print(x)
        return(x)
