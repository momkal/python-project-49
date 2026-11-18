from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    number_first = randint(0, 100)
    number_second = randint(0, 100)
    question = str(number_first) + " " + str(number_second)
    answer_correct = gcd(number_first, number_second)
    return question, answer_correct