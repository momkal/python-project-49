from random import randint

import prompt


def main(name):
    print("Welcome to the Brain Games!")
    count = 0
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    while count < 3:
        number = randint(0,100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if number %2 == 0:
            answer_correct = "yes"
        else:
            answer_correct = "no"
        if answer == answer_correct:
            print("Correct!")
            count += 1
        else:
            print(f"\'{answer}\' is wrong answer ;(. Correct answer was \'{answer_correct}\'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")
    