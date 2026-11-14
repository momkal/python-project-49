from brain_games.games.even import main
from brain_games.scripts.brain_games import main as welcome


def run():
    name = welcome()
    main(name)