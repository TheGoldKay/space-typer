import arcade
import argparse
import yaml
import ctypes

from src.game import Game
from src.globals import *


def main(screen_width, screen_height, words):
    game = Game(screen_width, screen_height, words)
    user32 = ctypes.windll.user32
    monitor_width = user32.GetSystemMetrics(0)
    monitor_height = user32.GetSystemMetrics(1)
    game.set_location(monitor_width // 2 - screen_width // 2, monitor_height // 2 - screen_height // 2)
    game.setup()
    arcade.run()


def parse_word_list(word_list_filename):
    with open(word_list_filename, "r") as word_list_file:
        data = yaml.safe_load(word_list_file)
        return data["words"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start space-typer game.")
    parser.add_argument("--screen-width", type=int, default=SCREEN_WIDTH, help="Width of screen in pixels")
    parser.add_argument("--screen-height", type=int, default=SCREEN_HEIGHT, help="Height of screen in pixels")
    parser.add_argument("--word-list", type=str, default=None,
                        help="yaml file containing the words to use in the game" +
                        " (use a list of words with key 'words'); by default use built-in word list.")

    args = parser.parse_args()

    if args.word_list:
        words = parse_word_list(args.word_list)
    else:
        words = DEFAULT_WORD_LIST

    main(args.screen_width, args.screen_height, words)
