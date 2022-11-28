def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# test_board = ['#','/','/','/','/','/','/','/','/','/']

def player_choose():
    player_1 = input("Choose x or o").upper()
    return player_1


def player1_choose(player_1):
    if player_1 == "X":
        player_2 = "O"
    elif player_1 == "O":
        player_2 = "X"
    return player_2


def move_1(player_1, test_board):
    x = input("Player 1 select a number to replace in the keyboard")
    x = int(x)
    while test_board[x] != "/":
        print("Your choice is already taken, choose another place")
        x = input("Player 1 select a number to replace in the keyboard")
        x = int(x)
    test_board[x] = player_1
    return test_board


def move_2(player_2, test_board):
    x = input("Player 2 select a number to replace in the keyboard")
    x = int(x)
    while test_board[x] != "/":
        print("Your choice is already taken, choose another place")
        x = input("Player 2 select a number to replace in the keyboard")
        x = int(x)
    test_board[x] = player_2
    return test_board


def win(mark):
    if ((test_board[7] == mark and test_board[8] == mark and test_board[9] == mark) or  # across the top
            (test_board[4] == mark and test_board[5] == mark and test_board[6] == mark) or  # across the middle
            (test_board[1] == mark and test_board[2] == mark and test_board[3] == mark) or  # across the bottom
            (test_board[7] == mark and test_board[4] == mark and test_board[1] == mark) or  # down the middle
            (test_board[8] == mark and test_board[5] == mark and test_board[2] == mark) or  # down the middle
            (test_board[9] == mark and test_board[6] == mark and test_board[3] == mark) or  # down the right side
            (test_board[7] == mark and test_board[5] == mark and test_board[3] == mark) or  # diagonal
            (test_board[9] == mark and test_board[5] == mark and test_board[1] == mark)):
        return False


def draw(test_board):
    if not "/" in test_board:
        print("Draw")
        return False
    else:
        return True


game_on = True

while game_on:
    play = True
    game_on = input("Want to play tic tac toe? y or n")
    if game_on == "n":
        game_on = False
        play = False
    while play:
        game_on = True
        player_1 = player_choose()
        test_board = ['#', '/', '/', '/', '/', '/', '/', '/', '/', '/']
        while game_on:
            player_1 = player_1
            screen = display_board(test_board)

            player_2 = player1_choose(player_1)
            test_board = move_1(player_1, test_board)
            play = draw(test_board)
            if play == False:
                break
            a = win(player_1)
            if a == False:
                game_on = a
                print("player 1 win")
                break
            b = win(player_2)
            if b == False:
                game_on = a
                print("player 2 win")
                break

            print(display_board(test_board))
            test_board = move_2(player_2, test_board)
            play = draw(test_board)

            a = win(player_1)
            if a == False:
                game_on = a
                print("player 1 win")
                break
            b = win(player_2)
            if b == False:
                game_on = b
                print("player 2 win")
                break

            print(display_board(test_board))











