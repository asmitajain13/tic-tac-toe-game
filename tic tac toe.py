#from IPython.display import clear_output
import random
def display_board(board):
    #clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    '''
    output=(player 1 marker, player 2 marker)
    '''
    marker=''
    while marker!= 'X' and marker != '0':
        marker=input("player1: choose X or 0") .upper()
    if marker=='X':
        return('X','0')
    else:
        return('0','X')
def place_marker(board, marker, position):
    board[position]=marker
def win_check(board, mark):
    #win tic tac toe
    #all rows, and check to see if they all share the same marker
    return((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark)) 
        #print(True)
    #else:
        #print(False)
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board,position):
    if board[position]==' ':
        return(True)
    else:
        return(False)
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #board is full
    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position:(1-9)'))
    return position
def replay():
    choice=input("play again Y or N:")
    return choice=='Y'

#while loop to keep running
print("Welcome to tic tac toe game")
while True:
    #play the game
    #set board,who is first,choose marker X,0)
    the_board= [' ']*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn + 'will go first')
    play_game=input("ready to play?y or n?")
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='Player 1':
        #Player 1 turn
            #show the board
            display_board(the_board)
            #choose a position
            position=player_choice(the_board)
            #place the marker ont he position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won!')
                game_on=False
            else:
                #check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game1")
                    game_on=False
                else:
                    turn='Player 2'
                    #no tie and no win? then next player's turn
        else:
            #show the board
            display_board(the_board)
            #choose a position
            position=player_choice(the_board)
            #place the marker ont he position
            place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player 2 has won!')
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game1")
                    game_on=False
                else:
                    turn='Player 1'
    if not replay():
        break
    #break out of the loop or replay()
            
            
            
            

#a=['#','X','0','X','0','X','0','X','0','X']    

#player1_marker, player2_marker=player_input()
#place_marker(a,'$',8)
#win_check(a,'X')
#display_board(a)


