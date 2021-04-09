def spiralize(number):

    x = (number - 1) / 2

    n = (3 + 2 * x * (8 * x * x + 15 * x + 13)) / 3

    return int(n)


def main():

    diag = spiralize(501)
    
    print(diag)


main()