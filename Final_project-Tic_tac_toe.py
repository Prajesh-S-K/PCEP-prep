from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],"   |",sep="")
    print("|       |       |       |") 
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |",sep="")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |",sep="")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    move = 'O'
    while move == 'O':
        try:
            user_input = int(input("Enter your move : "))
            if user_input not in range(1,10):
                print("Invalid move, try again")
            else:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == user_input:
                            board[i][j] = 'O'
                            display_board(board)
                            move = 'X'
                            break
                    else:
                        continue
                    break
                else:
                    print("Invalid move, try again")
        except ValueError:
            print("Unexpected move, try again")
    game_over = victory_for(board, 'O')
    return board, move, game_over

def draw_move(board):
    # The function draws the computer's move and updates the board. 
    move = 'X'
    while move == 'X':
        try:
            computer_input = randrange(1,10)
            for i in range(3):
                for j in range(3):
                    if board[i][j] == computer_input:
                        board[i][j] = 'X'
                        display_board(board)
                        move = 'O'
                        break
                else:
                    continue
                break
            else:
                move = 'X'
        except ValueError:
            move = 'X'
    game_over = victory_for(board, 'X')
    return board, move, game_over

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_fields.append((i, j))
    if free_fields == []:
        print("Game Over - By Draw")
        game_over = True
    else:
        game_over = False
    return free_fields, game_over


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    game_over = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            print(sign,"wins")
            record[sign]+=1
            game_over = True
            break
        elif board[0][i] == board[1][i] == board[2][i] == sign:
            print(sign,"wins")
            record[sign]+=1
            game_over = True
            break
    if game_over:
        print("Score: ", record)
    return game_over

def game_stimulator():
    # The function calls all the functions to simulate the game
    global game_over, board, free_fields, record, move
    board = [[1, 2, 3],
             [4, 'X', 6],
             [7, 8, 9]]  # an example of a board
    game_over = False
    record = {'X': 0, 'O': 0}
    free_fields = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    move = 'X'
    display_board(board)
    while not game_over:
        if move == 'X':
            board, move, game_over = enter_move(board)
            if game_over:
                break
            make_list_of_free_fields(board)
            move = 'O'
        else:
            board, move, game_over = draw_move(board)
            if game_over:
                break
            make_list_of_free_fields(board)
            move = 'X'
    game_over = False
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    free_fields = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    return board, free_fields, game_over

game_stimulator()



# def enter_move(board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.
#     move = 'O'
#     while move == 'O':
#         try:
#             user_input = int(input("Enter your move : "))
#             if user_input not in range(1,10):
#                 print("Invalid move, try again")
#             else:
#                 for i in range(3):
#                     for j in range(3):
#                         if board[i][j] == user_input:
#                             board[i][j] = 'O'
#                             display_board(board)
#                             move = 'X'
#                             break
#                     else:
#                         continue
#                     break
#                 else:
#                     print("Invalid move, try again")
#         except ValueError:
#             print("Unexpected move, try again")
#     return board, move




# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game
#     game_over = False
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] == sign:
#             print(sign,"wins")
#             record[sign]+=1
#             game_over = True
#             break
#         elif board[0][i] == board[1][i] == board[2][i] == sign:
#             print(sign,"wins")
#             record[sign]+=1
#             game_over = True
#             break
#     return game_over


# def draw_move(board):
#     # The function draws the computer's move and updates the board. 
#     move = 'X'
#     while move == 'X':
#         try:
#             computer_input = randrange(1,10)
#             for i in range(3):
#                 for j in range(3):
#                     if board[i][j] == computer_input:
#                         board[i][j] = 'X'
#                         display_board(board)
#                         move = 'O'
#                         break
#                 else:
#                     continue
#                 break
#             else:
#                 move = 'X'
#         except ValueError:
#             move = 'X'
#     return board, move





# def game_stimulator():
#     # The function calls all the functions to simulate the game
#     global game_over, board, free_fields, record, move
#     board = [[1, 2, 3],
#              [4, 'X', 6],
#              [7, 8, 9]]  # an example of a board
#     game_over = False
#     record = {'X': 0, 'O': 0}
#     free_fields = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
#     move = 'X'

#     display_board(board)
#     while not game_over:
#         if move == 'X':
#             enter_move(board)
#             make_list_of_free_fields(board)
#             victory_for(board, 'O')
#             move = 'O'
#         else:
#             draw_move(board)
#             make_list_of_free_fields(board)
#             victory_for(board, 'X')
#             move = 'X'
#     print("Score: ", record)
#     game_over = False
#     board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
#     free_fields = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
#     return board, free_fields, game_over

# game_stimulator()
