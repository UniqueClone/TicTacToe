"""

Layout of game (won't be italic):

 -------------
 | 0 | 1 | 2 |
 |---|---|---|
 | 3 | 4 | 5 |
 |---|---|---|
 | 9 | 7 | 8 |
 -------------

"""


def print_board(board):
    board_string = " -------------\n | {p0} | {p1} | {p2} |\n |---|---|---|\n | {p3} | {p4} | {p5} |\n |---|---|---|\n | {p6} | {p7} | {p8} |\n -------------\n "
    print(board_string.format(p0=board[0], p1=board[1], p2=board[2], p3=board[3], p4=board[4], p5=board[5], p6=board[6], p7=board[7], p8=board[8]))


def next_turn(player, board):
    xo = 'player'

    # temp = input("Place an {} in position (1 to 9, left to right, top to bottom): ".format(xo))
    # temp = ""
    # temp1 = 10
    try:
        temp = input("Place an {} in position (1 to 9, left to right, top to bottom): ".format(xo))
        temp1 = int(temp)
    except:
        "Not a number, try again"

    if board[temp1-1] != '-':
        print("Already taken, you muppet!")
    else:
        board[temp1-1] = player


def check_win(board):
    if board[0] != '-' and board[0] == board[1] and board[0] == board[2]:  # Top Row
        return True
    elif board[3] != '-' and board[3] == board[4] and board[3] == board[5]:  # Middle Row
        return True
    elif board[6] != '-' and board[6] == board[7] and board[3] == board[8]:  # Bottom Row
        return True
    elif board[0] != '-' and board[0] == board[3] and board[0] == board[6]:  # First Column
        return True
    elif board[1] != '-' and board[1] == board[4] and board[1] == board[7]:  # Second Column
        return True
    elif board[2] != '-' and board[2] == board[5] and board[2] == board[8]:  # Third Column
        return True
    elif board[0] != '-' and board[0] == board[4] and board[0] == board[8]:  # Diagonal One
        return True
    elif board[2] != '-' and board[2] == board[4] and board[2] == board[6]:  # Diagonal One
        return True
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    board_pieces = ['-', '-', '-',
                    '-', '-', '-',
                    '-', '-', '-']

    winner = False
    cur_player = 'O'

    print_board(board_pieces)

    while not winner:
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

        print("{p}'s turn: ".format(p=cur_player))
        next_turn(cur_player, board_pieces)
        print_board(board_pieces)

        winner = check_win(board_pieces)

    print("Winner! \'{}\' wins!\n".format(cur_player))

    input("Press enter to exit...")

#    print_board(p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8)
