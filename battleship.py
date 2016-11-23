from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
def set_ship_position(board):
    ship_row = random_row(board)
    ship_col = random_col(board)

    if board[ship_row][ship_col] == "S":
        print "Position already selected. Randomly selecting another position..."
        set_ship_position(board)
    else:
        board[ship_row][ship_col] = "S"

for x in range(3):
    set_ship_position(board)

# print_board(board)

ships_sunk = 0

for turn in range(5):
    print "Turn", turn + 1

    guess_row = int(raw_input("Guess Row (Enter a number 0 - 4): "))
    guess_col = int(raw_input("Guess Col (Enter a number 0 - 4): "))

    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "S":
        global ships_sunk
        print "Congratulations! You sunk one of my battleship!"
        board[guess_row][guess_col] = "X"
        ships_sunk += 1
        # print ships_sunk
        if ships_sunk == 3:
            print "Congratulations! You sunk all of my battleships!"
            print_board(board)
            break
        # print_board(board)
    else:
        if (board[guess_row][guess_col] == "M"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "M"

    if turn == 4:
        print "Game Over"
        print_board(board)
        print "X - Destroyed ship"
        print "M - Missed"
        print "S - Ship position"
