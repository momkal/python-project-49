from math import gcd
from random import randint

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main as welcome


def main():
    welcome()
    name = welcome_user()
    count = 0
    print("Find the greatest common divisor of given numbers.")
    while count < 3:
        number_first = randint(0, 100)
        number_second = randint(0, 100)
        print(f"Question: {number_first} {number_second}")
        answer = prompt.string("Your answer: ")
        answer_correct = gcd(number_first, number_second)
        if int(answer) == answer_correct:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer_correct}'")
            print(f"Let's try adain, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")