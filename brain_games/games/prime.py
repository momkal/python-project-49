from random import randint

import prompt


def main(name):
    count = 0
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
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
    