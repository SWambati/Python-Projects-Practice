#this program plays tic-tac-toe with a user
import random

board = [str(i) for i in range(1, 10)]
def display_board():
    print("* __ * __ * __*")
    print(f"|{board[0]}  |  {board[1]}  |  {board[2]} |")
    print("* __ * __ * __*")
    print(f"|{board[3]}  |  {board[4]}  |  {board[5]} |")
    print("* __ * __ * __*")
    print(f"|{board[6]}  |  {board[7]}  |  {board[8]} |")
    print("* __ * __ * __*")
    print("\n")

def winning_combinations(player):
    win_list =[
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in combination) for combination in win_list)

def possible_moves():
    return [i for i in range(9) if board[i] not in ["X", "O"]]

def is_board_full():
    return all(square in ["X", "O"] for square in board)

def move(i, player):
    if board[i] not in ["X", "O"]:
        board[i] = player
        return True
    return False

player = ""
program = ""
while player not in ["X", "O"]:
    player = input("Hello, player. Choose a character, X or O: ")


if player == "X":
    program = "O"
else:
    program = "X"


display_board()

if program == "X":
    make_move = 4 if 4 in possible_moves() else random.choice(possible_moves())
    move(make_move, program)

    display_board()



while True:
    while True:
        try:
            make_move = int(input(f"Enter number of square you'd love to place {player}: ")) - 1
            if make_move in possible_moves():
                move(make_move, player)
                break
            else:
                print("You cannot choose an already occupied square, player")
        except:
            print("Choose a square number from 1 to 9")

    display_board()

    if winning_combinations(player):
        print("Congratulations, player! You win this round")
        break
    if is_board_full():
        print("Good game player. We've got a tie here")
        break

    print("It's the program's turn")

    if program == "X" and 4 in possible_moves():
        make_move = 4
    else:
        make_move= random.choice(possible_moves())

    move(make_move, program)
    print(f"Program placed {program} at {make_move +1}")
    display_board()

    if winning_combinations(program):
        print("Program wins!")
        break
    if is_board_full():
        print("Good game! We've got a tie")
        break

    



