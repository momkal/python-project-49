from random import choice, randint

import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import main as welcome


def main():
    welcome()
    name = welcome_user()
    count = 0
    print("What result of the expression?")
    operands = ["+", "-", "*"]
    while count < 3:
        number_first = randint(0, 100)
        number_second = randint(0, 100)
        operation = choice(operands)
        print(f"Question: {number_first} {operation} {number_second}")
        answer = prompt.string("Your answer: ")
        match operation:
            case "*":
                answer_correct = number_first * number_second
            case "-":
                answer_correct = number_first - number_second
            case "+":
                answer_correct = number_first + number_second
        if answer_correct == int(answer):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{answer_correct}'")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")