import sys
from game_stats import GameStats
from word_board import WordBoard

if __name__ == '__main__':
    # Create the game object and then play the game
    if (len(sys.argv) == 2):
        fileName = sys.argv[1]
        print("Using " + fileName)
    else:
        # fileName = 'wordlists/popular9.txt'
        fileName = 'wordlists/popular9.txt'
        print("Using wordlists/popular9.txt")
    wb = WordBoard(fileName)
    gb = GameStats(wb)
    print("Starting")
    gb.play_game()
