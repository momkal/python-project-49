from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
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
    question = " ".join(map(str, numbers))
    return question, answer_correct