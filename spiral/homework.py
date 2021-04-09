def spiralize(number):

    x = (number - 1) / 2

    n = (3 + 2 * x * (8 * x * x + 15 * x + 13)) / 3

    return n


def main():

    dSum = spiralize(501)
    
    print(dSum)


main()