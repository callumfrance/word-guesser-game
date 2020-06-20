from game_stats import GameStats
from word_board import WordBoard

from view_cli import ViewCLI
# from view_html import ViewHTML

FILENAME = ''
VIEW = ''
WB = ''
GS = ''

def setup(fn='wgg/static/wordlists/popular9.txt'):
    global FILENAME, VIEW, WB, GS
    FILENAME = fn
    VIEW = ViewCLI()
    WB = WordBoard(FILENAME)
    GS = GameStats()

def main_loop():
    will_exit = False
    while (not will_exit):
        VIEW.v_board(WB.board)
        has_answer = False
        while not has_answer:
            u_in = VIEW.v_user_in()
            if ((u_in == '--ans') or (u_in == '--help')):
                VIEW.v_result(WB.ans_word)
                GS.process_failure()
                has_answer = True
                break
            elif (WB.check_answer(u_in)):
                VIEW.v_print("Correct")
                GS.process_correct()
                has_answer = True
                break
            elif (u_in == '--exit'):
                VIEW.v_stats(GS.get_stats())
                will_exit = True
                break
            else:
                VIEW.v_print("Not correct, try again")
                GS.process_incorrect()
            VIEW.v_board(WB.board)
        WB.generate_random_word()


if __name__ == '__main__':
    setup('../static/wordlists/popular9.txt')
    main_loop()
