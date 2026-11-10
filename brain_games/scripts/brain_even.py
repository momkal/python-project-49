from random import randint

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main as welcome


def main():
    welcome()
    name = welcome_user()
    count = 0
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    while count < 3:
        number = randint(0,100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if number %2 == 0:
            answer_correct = "yes"
            answer_incorrect = "no"
        else:
            answer_correct = "no"
            answer_incorrect = "yes"
        if answer == answer_correct:
            print("Correct!")
            count += 1
        else:
            print(f"\'{answer_incorrect}\' is wrong answer ;(. Correct answer was \'{answer_correct}\'")
            print(f"Let's try again, {name}")
            break
    if count == 3:
        print(f"Congratulations, {name}")
    