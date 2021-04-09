bulls_and_cows = {'bulls': 0, 'cows': 0}


def checking_number(number):
    user_number = []
    global bulls_and_cows
    for i in number:
        user_number.append(int(i))

    for i in range(4):
        if user_number[i] == hidden_numbers[i]:
            bulls_and_cows['bulls'] += 1
    for i in range(4):
        for r in range(4):
            if user_number[i] == hidden_numbers[r]:
                bulls_and_cows['cows'] += 1
    # todo работающий цикл

    # for index, var in enumerate(number):
    #     if hidden_numbers[index] == number[index]:
    #         bulls_and_cows['bulls'] += 1
    # if i in range()
    #         bulls_and_cows['cows'] += 1


user_number = [1, 2, 3, 4]
hidden_numbers = [1, 6, 8, 4]