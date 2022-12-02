# TicTacToe

class Bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_user_symbol():
    accepted_answer = ('X', 'O')
    answer = ''
    while answer not in accepted_answer:
        answer = (input('Please chose your symbol (X/O)')).upper()
        if answer not in accepted_answer:
            print(Bcolors.WARNING + 'The answer you provided is not acceptable.' + Bcolors.ENDC)
    return answer


def assign_symbol():
    if user_one == 'X':
        user_two = 'O'
    else:
        user_two = 'X'
    return user_two


def display_board():
    print('\n'*100)
    print(f' User one is {user_one}\n User two is {user_two}')
    print(Bcolors.HEADER + '###############\n# TIC-TAC-TOE #\n###############' + Bcolors.ENDC)
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
    if board[2][0] == board[2][1] == board[2][2] or \
            board[1][0] == board[1][1] == board[1][2] or \
            board[0][0] == board[0][1] == board[0][2] or \
            board[0][0] == board[1][0] == board[2][0] or \
            board[0][1] == board[1][1] == board[2][1] or \
            board[0][2] == board[1][2] == board[2][2] or \
            board[0][0] == board[1][1] == board[2][2] or \
            board[0][2] == board[1][1] == board[2][0]:
        return True


def switch_user(symbol):
    global user_color
    if symbol == user_one:
        symbol = user_two
    else:
        symbol = user_one
    if user_color == Bcolors.OKCYAN:
        user_color = Bcolors.OKGREEN
    else:
        user_color = Bcolors.OKCYAN
    return symbol


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
                answer = input(user_color + f'{symbol}, it is your turn.\n/'
                                            f'Chose one of the following \n/'
                                            f'{accepted_answer[:-1]}' + Bcolors.ENDC)
            place_on_board(answer, symbol)
            display_board()
            strike = check_strike()

            accepted_answer.remove(answer)
            answer = ''

            if strike:
                print(f' congrats {symbol} wins')
            else:
                symbol = switch_user(symbol)


print('\n'*100)
print(Bcolors.HEADER + '###############\n# TIC-TAC-TOE #\n###############' + Bcolors.ENDC)
user_color = Bcolors.OKCYAN
user_one = get_user_symbol()
user_two = assign_symbol()
board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
display_board()
run_game_actions()