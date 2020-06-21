from flask import (Flask,
        flash,
        jsonify,
        redirect,
        render_template,
        request,
        url_for,
)

# from .gameobj.game_stats import GameStats
# from .gameobj.word_board import WordBoard
# from .gameobj.view_html import ViewHTML

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


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    @app.route('/_scramble_word')
    def scramble_word():
        return jsonify(result="answer")

    @app.route('/')
    def base():
        return render_template('test.html')

    return app
