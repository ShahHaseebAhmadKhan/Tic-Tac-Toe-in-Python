from random import randrange

def display_board(board):
    print('-------------')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('-------------')

def make_empty_board():
    return [['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']]

def make_player_move(board, move, player):
    row, col = move_to_row_col(move)
    if board[row][col] == 'X' or board[row][col] == 'O':
        return False
    else:
        board[row][col] = player
        return True

def move_to_row_col(move):
    move -= 1
    return move // 3, move % 3

def make_computer_move(board):
    move = randrange(1, 10)
    while not make_player_move(board, move, 'X'):
        move = randrange(1, 10)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_game_over(board):
    if check_winner(board, 'X'):
        return 'Computer wins!'
    elif check_winner(board, 'O'):
        return 'You win!'
    elif all(cell == 'X' or cell == 'O' for row in board for cell in row):
        return 'Tie!'
    else:
        return 'Continue'

def main():
    board = make_empty_board()
    display_board(board)

    while True:
        # Player's move
        move = int(input("Enter your move (1-9): "))
        if make_player_move(board, move, 'O'):
            display_board(board)
            result = check_game_over(board)
            if result != 'Continue':
                print(result)
                break

        # Computer's move
        make_computer_move(board)
        display_board(board)
        result = check_game_over(board)
        if result != 'Continue':
            print(result)
            break

if __name__ == "__main__":
    main()
