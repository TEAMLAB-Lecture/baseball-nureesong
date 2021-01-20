# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 18:50:45 2021

@author: nuree
"""


def main():
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)

    # user_input_number = 999
    # flag = True
    while 1:
        user_input_number = input('Input guess number: ')
        if user_input_number == '0': 
            break
        elif not(is_validated_number(user_input_number)):
            print('Wrong Input, Input again') #continue
        else:
            strikes, balls = get_strikes_or_ball(user_input_number, random_number)
            print(f'Strikes : {strikes} , Balls : {balls}')
            if strikes < 3:
                continue
            
            while 1:
                one_more_input = input('You win, one more(Y/N) ?')
                if one_more_input == '0' or is_no(one_more_input): 
                    break
                elif not(is_yes(one_more_input)):
                    print('Wrong Input, Input again')
                else:
                    random_number = str(get_not_duplicated_three_digit_number())
                    print("Random Number is : ", random_number)
                    continue
                
                    
            
                
            
