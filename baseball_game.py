# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    return user_input_number.isdigit()


def is_between_100_and_999(user_input_number):
    if int(user_input_number) in range(100,1000):
        return True
    return False


def is_duplicated_number(three_digit):
    if len(set(three_digit)) == 3:
        return False
    return True


def is_validated_number(user_input_number):
    if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not(is_duplicated_number(user_input_number)):
        return True
    return False


def get_not_duplicated_three_digit_number():
    random_number = str(get_random_number())
    while is_duplicated_number(random_number):
        random_number = str(get_random_number())
    return int(random_number)


def get_strikes_or_ball(user_input_number, random_number):
    user_number = user_input_number[:]
    computer_number = random_number[:]
    strike, ball = 0, 0
    for i in range(3):
        if user_number[i] == computer_number[i]:
            strike += 1
        elif user_number[i] in computer_number:
            ball += 1
    return [strike, ball]


def is_yes(one_more_input):
    string = one_more_input[:]
    if string.lower() in ('y', 'yes'):
        return True
    return False


def is_no(one_more_input):
    string = one_more_input[:]
    if string.lower() in ('n', 'no'):
        return True
    return False


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
        
    flag = True
    while flag:
        user_input_number = input('Input guess number: ')
        if user_input_number == '0': 
            break
        elif not(is_validated_number(user_input_number)):
            print('Wrong Input, Input again') 
        else:
            strikes, balls = get_strikes_or_ball(user_input_number, random_number)
            print(f'Strikes : {strikes} , Balls : {balls}')
            
            if strikes == 3:
                while 1:
                    one_more_input = input('You win, one more(Y/N) ?')
                    if one_more_input == '0' or is_no(one_more_input): 
                        flag = False
                        break 
                    elif not(is_yes(one_more_input)):
                        print('Wrong Input, Input again')
                    elif is_yes(one_more_input):
                        random_number = str(get_not_duplicated_three_digit_number())
                        print("Random Number is : ", random_number)
                        break

    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()
