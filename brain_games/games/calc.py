from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    operands = ["+", "-", "*"]
    number_first = randint(0, 100)
    number_second = randint(0, 100)
    operation = choice(operands)
    question = str(number_first)+ " " + operation + " " + str(number_second)
    match operation:
        case "*":
            answer_correct = number_first * number_second
            return question, answer_correct
        case "-":
            answer_correct = number_first - number_second
            return question, answer_correct
        case "+":
            answer_correct = number_first + number_second
            return question, answer_correct