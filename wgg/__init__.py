from flask import (
        Flask, render_template, request, url_for, redirect, flash
)

from .gameobj.game_stats import GameStats
from .gameobj.word_board import WordBoard

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    

    @app.route('/')
    def base():
        wb = WordBoard()
        gb = GameStats(wb)

        return render_template('board.html', 
                board_display=gb.play_game()
            )

    return app
