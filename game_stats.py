from word_board import WordBoard

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
            print(self.game_board.print_board())
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


