#TicTacToe

"""


1. user_input -> Something 1-9
2. if they enter anything else, tell them to go again
3. check if the user_input is already taken
4. add the move to the board
5. check if the board state has won

"""

board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

coords = {
        1 : '00',
        2 : '01',
        3 : '02',
        4 : '10',
        5 : '11',
        6 : '12',
        7 : '20',
        8 : '21',
        9 : '22',
    }

user = True #True = 'X' False = 'O'

def user_move(user):
    move = convert_move(int(input('Select position 1-9: ')))
    if check_move(move):
        update_board(move, user)
              

def convert_move(move):
    return coords[move]

def check_move(move):
    x = int(move[0])
    y = int(move[1])
    
    if board[x][y] == '-':
        return True
    else: return False

def update_board(move, user):
    x = int(move[0])
    y = int(move[1])
    if user :
        board[x][y] = 'X'
    else:
        board[x][y] = 'O'

def is_win(board, user):

    if check_rows(board, user): return True
    if check_cols(board, user): return True
    if check_diag(board, user): return True

def check_rows(board, user):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != active_user(user):
                complete_row = False
                break
        if complete_row: return True
    return False

def check_cols(board, user):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if str(board[row][col]) != active_user(user):
                complete_col = False
                break
        if complete_col: return True
    return False

def check_diag(board, user):
    currentUser = active_user(user)
    if board[0][0] == currentUser and board[1][1] == currentUser and board[2][2] == currentUser: return True
    elif board[0][2] == currentUser and board[1][1] == currentUser and board[2][0] == currentUser: return True
    else: return False

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} " , end="")
        print()

def active_user(user):
  if user: return "X"
  else: return "O"

#Start of game
while True :
    active_user = active_user(user)
    user_move(user)
    print_board(board)
    if is_win(board, user): 
        print(active_user + ' has won!')
        break
    user = not user
    

    

