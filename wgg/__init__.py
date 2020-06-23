from flask import (Flask,
        flash,
        jsonify,
        redirect,
        render_template,
        request,
        url_for,
)

from .gameobj.game_stats import GameStats
from .gameobj.word_board import WordBoard
from .gameobj.view_html import ViewHTML

FILENAME = ''
VIEW = ''
WB = ''
GS = ''


def setup(fn='wgg/static/wordlists/popular9.txt'):
    global FILENAME, VIEW, WB, GS
    FILENAME = fn
    VIEW = ViewHTML()
    WB = WordBoard(FILENAME)
    GS = GameStats()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    setup()

    @app.route('/_word_page_initial')
    def word_page_initials():
        GS.current_word = WB.ans_word
        x = VIEW.v_board(WB.board)
        y = VIEW.v_stats(GS.get_stats_json())
        return jsonify(result=x, stats=y)

    def check_word_refresh():
        """Updates the Word Board displayed if it is old on the page.

        i.e. checks if the displayed word has been done already and then
        scrambles and displays a new word.
        """
        if WB.ans_word in GS.past_words:
            WB.generate_random_word()
        x = VIEW.v_board(WB.board)
        return x

    @app.route('/_give_up_answer')
    def get_answer():
        """Runs when the user wants the solution shown to proceed to next.
        """
        WB.generate_random_word()
        x = VIEW.v_board(WB.board)
        GS.process_failure(WB.ans_word)
        y = VIEW.v_stats(GS.get_stats_json())
        return(jsonify(result=x, stats=y))

    @app.route('/_process_guess')
    def process_guess():
        """Determines correctness of a guess and channels result accordingly.
        """
        a_guess = request.args.get('guess')

        if WB.check_answer(a_guess):
            WB.generate_random_word()
            GS.process_correct(WB.ans_word)
        else:
            GS.process_incorrect()

        x = check_word_refresh()
        y = VIEW.v_stats(GS.get_stats_json())

        return jsonify(result=x, stats=y)

    @app.route('/')
    def base():
        print("Base route ans_word: " + WB.ans_word)
        return render_template('test.html')

    return app
