"""Take user's name"""

def first_player():
    first_name = input('FIRST PLAYER: ')
    while True:
        if first_name:
            return first_name
            break
        else:
            first_name = input('FIRST PLAYER: ')

def second_player():
    second_name = input('SECOND PLAYER: ')
    while True:
        if second_name:
            return second_name
            break
        else:
            second_name = input('SECOND PLAYER: ')


