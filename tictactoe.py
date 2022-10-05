import time
#Draws board
#variables
board = { 1 : ' ', 2 : ' ', 3: ' ',
         4 : ' ', 5 : ' ', 6 : ' ', 
         7 : ' ', 8 : ' ', 9 : ' '}

count = 0  #counter to track number of spaces filled
winner = False  #boolean to check if there is a winner
play = True #boolean to check if the game should continue
tie = False
current_player = '' #variable to keep track of current player
Player_Dets = [] #list to store current player identifier
def get_player_dets(current_player):
    if current_player == 'A':
        return['B','O']
    else:
        return['A','X']




def printBoard(board):
    for i in board:
        print(i, ":", board[i], ' ', end='')
        if i%3 == 0:
            print()


def win_condition(marker, Player_id):
    if  board[1] == marker and board[2] == marker and board[3]== marker or \
        board[4] == marker and board[5] == marker and board[6]== marker or \
        board[7] == marker and board[8] == marker and board[9]== marker or \
        board[1] == marker and board[5] == marker and board[9]== marker or \
        board[2] == marker and board[5] == marker and board[8]== marker or \
        board[3] == marker and board[5] == marker and board[7]== marker or \
        board[3] == marker and board[6] == marker and board[9]== marker or \
        board[1] == marker and board[4] == marker and board[7] == marker:
        
            printBoard(board)
            time.sleep(1)
            print("Player", Player_id, "wins!")
            return True
    else:
        return False
def insert_input(position, marker):
        
    while   board[position] != ' ':
        print("sorry spot taken, pick another position")
        position = int(input())
    board[position] = marker

def play_again():
    print("do you want to play again?")
    play_again = input()

    if play_again.upper() == 'Y':
        for z in board:
            board[z] = ' '
        return True
    else: 
        print("Thank You for playing see you soon pal")

#main program
while play:
    printBoard(board)

    Player_Dets = get_player_dets(current_player)
    current_player = Player_Dets[0]
    print("Player{}: Please enter a number between 1 and 9  ".format(current_player))
    input_slot = int(input())
    #insert 'X' or 'O' in slot chosen
    insert_input(input_slot,Player_Dets[1])
    count += 1
    #check if there are any winners
    winner = win_condition(Player_Dets[1], current_player)
    if count == 9 and not winner:
        print("It's a tie!!!")
        tie = True
        printBoard(board)
    #check if players want to play again
    if winner or tie:
        play = play_again()
        if play:
            curr_player = ''
            count = 0