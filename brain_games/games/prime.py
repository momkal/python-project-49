from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def generate_round():
    number = randint(0, 100)
    if number < 2:
            return number, "no"
    else:    
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return number, "no"
                break
        return number, "yes"