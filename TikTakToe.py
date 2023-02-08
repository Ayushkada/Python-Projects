def display_board(board):
    print("", board[0][0], "|", board[0][1], "|", board[0][2])
    print("-----------")
    print("", board[1][0], "|", board[1][1], "|", board[1][2])
    print("-----------")
    print("", board[2][0], "|", board[2][1], "|", board[2][2])

def get_input():
    square = 0
    while square not in range(1,10):
        print ("Choose a square")
        square = int(input())

        # check if input is valid and between 1 and 9
        if square not in range(1,10):    
            print ("Error, invalid input")   
    return square   

def check_win(board):
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    # Return None if there is no winner
    return None

def play_game():
    board = [['','',''],['','',''],['','','']]

    #print blank board
    display_board(board)
    print("Player 1 choose a marker: X or O")
    marker = input()

    #check for correct input either 'X' or 'O'
    while (marker.upper() != 'O' and marker.upper() != 'X'):
        print("Player 1 choose a marker: X or O")
        marker = input()
    if marker.upper() == 'O':
        p1 = 'O'
        p2 = 'X'
    else: 
        p1 = 'X'
        p2 = 'O'

    # Initialize booleans of winner, which stops the game when there is a winner and player1 which 
    # declares whose turn it is, and int counter which counts the amount of turns to declare a tie.
    winner = False
    player1 = True
    counter = 0
    example_board = [['1','2','3'],['4','5','6'],['7','8','9']]
    while winner == False:
        print("To pick a square, choose a number from 1 - 9 corresponding to the following board")
        display_board(example_board)
        if (player1 == True):
            print ("Player 1:")
        else:
            print ("Player 2:")
        play = True
        while play == True:
            square = get_input()

            # Check if input is in first row
            if square <= 3:
                if board[0][square-1] == 'X' or board[0][square-1] == 'O':
                    print("Spot already taken, choose a new square")
                else:
                    play = False
                    if player1 == True:
                        board[0][square-1] = p1
                        player1 = False
                    else:
                        board[0][square-1] = p2
                        player1 = True

            # Check if input is in second row 
            if square > 3 and square <= 6:
                if board[1][square-4] == 'X' or board[1][square-4] == 'O':
                    print("Spot already taken, choose a new square")
                else:
                    play = False
                    if player1 == True:
                        board[1][square-4] = p1
                        player1 = False
                    else:
                        board[1][square-4] = p2
                        player1 = True

            # Check if input is in third row 
            if square > 6 and square <= 9:
                if board[2][square-7] == 'X' or board[2][square-7] == 'O':
                    print("Spot already taken, choose a new square")
                else:
                    play = False
                    if player1 == True:
                        board[2][square-7] = p1
                        player1 = False
                    else:
                        board[2][square-7] = p2
                        player1 = True
        display_board(board)
        if check_win(board) == p1:
            winner = True
            print("The Winner is player 1")
        else:
            if check_win(board) == p2:
                winner = True
                print("The Winner is player 2")
        counter = counter + 1
        if counter == 9 and winner == False:
            print ("There is a tie")
            break

repeat = True
new = ' '

while repeat == True:
    play_game()
    while (new.lower() != 'yes' and new.lower() != 'no'):
        print("Would you like to play again? Type yes or no.")
        new = input()
        if(new.lower() == 'no'):
            repeat = False
            break
        else:
            if (new.lower() != 'yes' and new.lower() != 'no'):
                print("invalid input")