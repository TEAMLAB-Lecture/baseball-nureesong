# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    result = user_input_number.isdigit()
    return result


def is_between_100_and_999(user_input_number):
    user_integer = int(user_input_number)
    if user_integer >= 100 and user_integer < 1000:
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit):
    if len(set([three_digit[0], three_digit[1], three_digit[2]])) == 3:
        result = False
    else:
        result = True
    return result


def is_validated_number(user_input_number):
    if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not(is_duplicated_number(user_input_number)):
        result = True
    else:
        result = False
    return result


def get_not_duplicated_three_digit_number():
    random_number = str(get_random_number())
    while is_duplicated_number(random_number):
        random_number = str(get_random_number())
    result = int(random_number)
    return result


def get_strikes_or_ball(user_input_number, random_number):
    user_number = user_input_number[:]
    computer_number = random_number[:]
    strike, ball = 0, 0
    for i in range(3):
        if user_number[i] == computer_number[i]:
            strike += 1
        elif user_number[i] in computer_number:
            ball += 1
    result = [strike, ball]
    return result


def is_yes(one_more_input):
    string = one_more_input[:]
    if string.lower() == 'y' or string.lower() == 'yes':
        result = True
    else:
        result = False
    return result


def is_no(one_more_input):
    string = one_more_input[:]
    if string.lower() == 'n' or string.lower() == 'no':
        result = True
    else:
        result = False
    result = None
    return result


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
        
    user_input_number = input('Input guess number: ')
    if user_input_number != '0':
        while not(is_validated_number(user_input_number)):
            print('Wrong Input, Input again')
            user_input_number = input('Input guess number: ')
        
        game_result = get_strikes_or_ball(user_input_number, random_number)
        strikes, balls = game_result[0], game_result[1]
        print(f'Strikes : {strikes} , Balls : {balls}')
        while strikes < 3:
            user_input_number = input('Input guess number: ')
            game_result = get_strikes_or_ball(user_input_number, random_number)
            strikes, balls = game_result[0], game_result[1]
            print(f'Strikes : {strikes} , Balls : {balls}')
        
        one_more_input = input('You win, one more(Y/N)?')        
        while not(is_yes(one_more_input) or is_no(one_more_input)):
            print('Wrong Input, Input again')
            one_more_input = input('You win, one more(Y/N)?')
        
        if is_yes(one_more_input):
            main()
        else:
            print("Thank you for using this program")
            print("End of the Game")
    else:
        print("Thank you for using this program")
        print("End of the Game")


if __name__ == "__main__":
    main()
