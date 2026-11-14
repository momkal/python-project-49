from brain_games.games.progression import main
from brain_games.scripts.brain_games import main as welcome


def run(name):
    name = welcome()
    main(name)