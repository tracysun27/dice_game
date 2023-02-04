#guess who is salty about not knowing how to play another game!
#that's right! it's me! back at it with the coding!

import random 
import time

def dice_roll():
    user_roll = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
    return user_roll

def return_pair_index(user_roll):
    i = 0
    j = 1
    others = []
    while i < (len(user_roll) - 1):
        if user_roll[i] == user_roll[j]:
            for index in range(len(user_roll)):
                if index == i or index == j:
                    continue
                else:
                    others.append(index)
            if user_roll[others[0]] == user_roll[others[1]]:
                if user_roll[others[0]] <= user_roll[i]:
                    return [others,[i,j]]
            return [[i,j],others]
        else:
            if j < 3:
                j += 1
            else:
               i += 1
               j = i + 1    
    if [i,j] == [len(user_roll)-1, len(user_roll)-1]: #no pairs found
        return None

def other_keys(user_roll):
    keys = return_pair_index(user_roll)
    other_keys = []
    if keys != None:
        for i in range(len(user_roll)):
            if i == keys[0] or i == keys[1]:
                continue
            else:
                other_keys.append(i)
    return other_keys

def detect_num_pairs(user_roll):
    keys = return_pair_index(user_roll)
    if keys == None: #no pairs
        return 0
    else: #check if there are more than 2 same elements
        other_dupes = 0
        for i in keys[1]: 
            if user_roll[i] == user_roll[keys[0][0]]:
                other_dupes += 1 
        if other_dupes == 0:
            return 1
        elif other_dupes == 1:
            return 0
        elif other_dupes == 2:
            return 4

def highest_val_pair(user_roll):
    keys = return_pair_index(user_roll)
    keys2 = other_keys(user_roll)
    if detect_num_pairs(user_roll) >= 1:
        if user_roll[keys2[0]] == user_roll[keys2[1]]:
            if user_roll[keys[0]] >= user_roll[keys2[0]]:
                return keys
            else:
                return keys2

def score(user_roll):
    if detect_num_pairs(user_roll) >= 1:
        keys = return_pair_index(user_roll)
        score = user_roll[keys[1][0]] + user_roll[keys[1][1]]
    else:
        score = 0
    return score


if __name__ == '__main__':
    print('>>>Welcome to Tracy\'s dice game!<<<')
    print('>>>>>>jk it\'s not hers. she stole it from an event she went to bc she got salty about losing')
    print('>>>Now available with 4 dice!<<<')
    print('Would you like to play?')
    print('(Press Y / N)')
    user_input = input('>>> ')
    if user_input == 'Y' or user_input == 'y':
        print('OK! Let\'s play!')
        while True:
            print('Rolling dice:')
            for i in range(3):
                print('.', end=" ")
                # adding time delay of half second
                time.sleep(0.5)
            print()
            user_roll = dice_roll()
            comp_roll = dice_roll()
            print('Your result is:',user_roll)
            print('Computer result is:', comp_roll)
            print()
            if detect_num_pairs(user_roll) == 4:
                print('Lucky! Four of a kind!')
                if user_roll[0] == 6:
                    print('DING DING DING! HIGH SCORE!')
                    print('this has a one in 6^4 chance of happening btw.')
            time.sleep(0.5)
            print('Your score:',score(user_roll))
            print('Computer score:', score(comp_roll))
            print()
            time.sleep(0.5)
            if score(user_roll) < score(comp_roll):
                print('Unlucky! You lost!')
            elif score(user_roll) == score(comp_roll):
                if user_roll == [6,6,6,6] and comp_roll != [6,6,6,6]:
                    print('Wow! You won!')
                print('Tie!')
            else:
                print('Wow! You won!')
            print('Try again?')
            print('Y / N')
            user_input = input('>>> ')
            if user_input == 'Y' or user_input == 'y':
                continue
            else:
                print('Goodbye!')
            break
    else:
        print('Goodbye!')
