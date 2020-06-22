from .word_board import WordBoard


class GameStats:
    """Class that contains game states and manages the game state
    """
    def __init__(self):
        self.board_cnt = 1
        self.correct = 0
        self.incorrect = 0
        self.failures = 0

    def process_correct(self):
        self.correct += 1
        self.board_cnt += 1

    def process_failure(self):
        self.failures += 1
        self.board_cnt += 1

    def process_incorrect(self):
        self.incorrect += 1

    def get_stats(self):
        stat_str = ["Correct guesses: ", str(self.correct)]
        stat_str += ["Incorrect guesses: ", str(self.incorrect)]
        stat_str += ["Passes: ", str(self.failures)]
        stat_str += ["Boards generated: ", str(self.board_cnt)]
        return(stat_str)
