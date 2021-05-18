from User import first_player,second_player

#-------Global Variables---------

board = ['-','-','-','-','-','-','-','-','-']
game_flag = True # check game over or not

# Win or Tie?
winner = None
# Whose turn?
first_p = first_player()
sec_p = second_player() 
current_player = first_p

# Play game Tic Tac Toe
def play_game():
    """Describe all game and handle functions"""
    global winner
    global current_player
    # Init board
    display_board()

    while game_flag:
        handle_turn(current_player)

        check_if_game_over()

        current_player = flip_player(current_player)

    check_who_winner(winner)    

def display_board():
    """Display 3x3 init board"""
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('\t\t\t\t\t\t' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('\t\t\t\t\t\t' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('\t\t\t\t\t\t' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def handle_turn(current_player):
    """Userin hansi positiona qoymaq istediyin daxil et"""
    print('\n\n')
    print("\t\t\t\t\tIt is your turn, " + current_player)
    position = int(input("\t\t\t\t\tChoose a position 1-9: "))
    
    position -= 1          # Because index of list start from zero!
    if current_player == first_p:
        board[position] = 'X'
    elif current_player == sec_p:
        board[position] = 'O'        
    display_board()   

def check_if_game_over():
    # global variable which check game still going
    global game_flag
    
    # check rows
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    # check column
    column1 = board[0] == board[3] == board[6] !='-'
    column2 = board[1] == board[4] == board[7] !='-'
    column3 = board[2] == board[5] == board[8] !='-'

    # check dioganal
    dioganal1 = board[0] == board[4] == board[8] !='-'
    dioganal2 = board[2] == board[4] == board[6] != '-'

    if row1 or row2 or row3 or column1 or column2 or column3 or dioganal1 or dioganal2:
        game_flag = False

        # Return who win
        if row1 or column1 or dioganal1:
            return board[0]
        if row2:
            return board[3]
        if row3:
            return board[6]
        if column2:
            return board[1]
        if column3 or dioganal2:
            return board[2]
    else:
        return None            

def flip_player(current_player):
    if current_player == first_p:
        player = sec_p
        return player
    elif current_player == sec_p:
        player = first_p 
        return player      

def check_who_winner(winner):
    """"Check whether X is winner or O"""
    winner = check_if_game_over()
    if winner == 'X':
        print('\t\t\t\t\t\t' + first_p + ' won the game!')
    elif winner == 'O':
        print('\t\t\t\t\t' + sec_p + ' won the game!')
    else:
        print('\t\t\t\t\t\tGame is Tie!')    

play_game()









     