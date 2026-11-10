from random import randint

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main as welcome


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    count = 0
    print("What number is missing in the progression?")
    while count < 3:
        number_plus = randint(1, 5)
        long_of_progress = randint(5,10)
        position_hidden = randint(0,(long_of_progress - 1))
        number = randint(0,100)
        numbers = []
        for i in range(long_of_progress):
            numbers.append(number)
            number += number_plus
        answer_correct = str(numbers[position_hidden])
        numbers[position_hidden] = ".."
        print(f"Question: {" ".join(map(str, numbers))}")
        answer = prompt.string("Your answer: ")
        if answer == answer_correct:
            count += 1
            print("Correct")
        else:
            print(f"'{answer}' is wrong anser ;(. Correct answer was'{answer_correct}'")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")