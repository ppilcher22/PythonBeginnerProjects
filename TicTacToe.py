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

def user_move():
    move = convert_move(int(input('Select position 1-9: ')))
    if check_move(move):
        update_board(move)
              

def convert_move(move):
    return coords[move]

def check_move(move):
    x = int(move[0])
    y = int(move[1])
    
    if board[x][y] == '-':
        return True
    else: return False

def update_board(move):
    x = int(move[0])
    y = int(move[1])
    if user :
        board[x][y] = 'X'
    else:
        board[x][y] = 'O'

def is_win(board):

    if check_rows(board): return True
    if check_cols(board): return True
    if check_diag(board): return True

def check_rows(board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != 'X':
                complete_row = False
                break
        if complete_row: return True
    return False

def check_cols(board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if str(board[row][col]) != 'X':
                complete_col = False
                break
        if complete_col: return True
    return False

def check_diag(board):
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X': return True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X': return True
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
    user_move()
    print_board(board)
    if is_win(board): 
        print('X has won!')
        break
    

    

