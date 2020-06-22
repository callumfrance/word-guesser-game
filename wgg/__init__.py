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

    @app.route('/_scramble_word')
    def scramble_word():
        WB.generate_random_word()
        x = VIEW.v_board(WB.board)
        print("Scrambled- " + WB.ans_word)
        return jsonify(result=x)

    @app.route('/_check_word_refresh')
    def check_word_refresh():
        x = VIEW.v_board(WB.board)
        print(GS.past_words)
        if WB.ans_word in GS.past_words:
            print("ans word is in past words- " + WB.ans_word)
            return(scramble_word())
        print("ans word is NOT in past words- " + WB.ans_word)
        return jsonify(result=x)

    @app.route('/_give_up_answer')
    def get_answer():
        GS.process_failure(WB.ans_word)
        stats = VIEW.v_stats(GS.get_stats_json())
        WB.generate_random_word()
        x = VIEW.v_board(WB.board)
        y = VIEW.v_stats(GS.get_stats_json())
        print(jsonify(result=x, stats=y))
        return(jsonify(result=x, stats=y))

    @app.route('/_process_guess')
    def process_guess():
        init_set = request.args.get('initial_set')
        if init_set == 'Truey':
            GS.process_failure(WB.ans_word)
        if init_set != 'Truey':
            a_guess = request.args.get('guess')
            result = None
            stats = None
            if WB.check_answer(a_guess):
                result = VIEW.v_print("Correct")
                GS.process_correct()
            else:
                print(init_set + " check_answer is not True")
                result = VIEW.v_print("Incorrect")
                GS.process_incorrect()

        stats = VIEW.v_stats(GS.get_stats_json())

        return jsonify(stats=stats)

    @app.route('/')
    def base():
        x = scramble_word()
        print(WB.ans_word)
        return render_template('test.html')

    return app
