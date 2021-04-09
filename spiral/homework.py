def spiralize(number):

    x = (number - 1) / 2

    if number == 1:
        return_value = 1
    else:    
        return_value = (3 + 2 * x * (8 * x * x + 15 * x + 13)) / 3
    return return_value


if __name__ == "__main__":
    print(spiralize(501))
