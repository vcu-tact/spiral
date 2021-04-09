def spiralize(number):

    x = (number - 1) / 2

    diagonal = (3 + 2 * x * (8 * x * x + 15 * x + 13)) / 3

    return int(diagonal)