def spiralize(number):

    if number == 1:
        diagonal = 1
    else:    
        x = (number - 1) / 2
        diagonal = (3 + 2 * x * (8 * x * x + 15 * x + 13)) / 3
    return int(diagonal)

if __name__ == "__main__":
    print(spiralize(501))
