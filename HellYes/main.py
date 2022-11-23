print('Welcome to Tic Tac Toe')


def get_user_symbol():
    accepted_answer = ('x', 'o')
    answer = ''
    while answer not in accepted_answer:
        answer = input('Please chose your symbol (x/o)')
    return answer
# Refactor to highlight that the answer is not acceptable

user_one = get_user_symbol()


def assign_symbol():
    if user_one == 'x':
        user_two = 'o'
    else:
        user_two = 'x'
    return user_two


user_two = assign_symbol()
print(f' User one is {user_one}\n User two is {user_two}')
# Refactor to use string for consistency
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def display_board():
    print(f'     ||     ||     ')
    print(f'  {board[2][0]}  ||  {board[2][1]}  ||  {board[2][2]}  ')
    print(f'     ||     ||     ')
    print(f'======================')
    print(f'     ||     ||     ')
    print(f'  {board[1][0]}  ||  {board[1][1]}  ||  {board[1][2]}  ')
    print(f'     ||     ||     ')
    print(f'======================')
    print(f'     ||     ||     ')
    print(f'  {board[0][0]}  ||  {board[0][1]}  ||  {board[0][2]}  ')
    print(f'     ||     ||      ')


display_board()


def place_on_board(position, symbol):
    board_positions_map = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }
    x = int(board_positions_map[position][0])
    y = int(board_positions_map[position][1])
    board[x][y] = symbol


def check_strike():
    pass


def run_game_actions():
    accepted_answer = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'end']
    strike = False
    symbol = user_one
    answer = ''
    while not strike:
        if accepted_answer[0] == 'end':
            print(' No one won, good luck next time')
            break
        else:
            while answer not in accepted_answer:
                answer = input(f'Please chose one of the following available positions {accepted_answer[:-1]}')
            place_on_board(answer, symbol)
            accepted_answer.remove(answer)
            answer = ''
            display_board()
            check_strike()


            # Check if there is a strike, can be also started only after the accepted answers list <= 5
            # switch the user
            # If strike, announce user won




run_game_actions()
