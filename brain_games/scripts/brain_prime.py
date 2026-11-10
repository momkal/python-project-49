from random import randint

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main as welcome


def main():
    welcome()
    name = welcome_user()
    count = 0
    print("Answer \"yes\" if the number is prime, otherwise answer \"no\"")
    while count < 3:
        number = randint(0,100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        answer_correct = "yes"
        if number < 2:
            answer_correct = "no"
        else:    
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    answer_correct = "no"
                    break
        if answer == answer_correct:
            print("Correct!")
            count += 1
        else:
            print(f"\'{answer}\' is wrong answer ;(. Correct answer was \'{answer_correct}\'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")
    