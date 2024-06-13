# Welcome to the Tic Tac Toe Game
# Things to do:
#1. Ask player1 for input and assign player2 a marker.
#2. Print the game dashboard everytime an input is requested
#3. Ask players to position their markers in the game.
#4. Check player moves and test game logic accordingly.
#5. Continously monitor game and print the winner.
#6. Ask players if they wish to restart the game or exit.

def game_markers():
    '''
    This function prints the welcome text and asks the player to choose a marker.
    '''

    welcome_txt = (
        "Welcome to the Tic Tac Toe Game!\n"
        'This is a 2 player game. Player 1 gets to choose marker X or O\n'
        'Please decide who gets to choose by rock paper sissors...\n'
    )

    print(welcome_txt)

    player1_marker = input('Player1 please choose a marker X or O: ')
    player2_marker = ''

    while player1_marker.upper() not in ['X', 'O']:
        player1_marker = input('Provided marker is invalid, please choose a marker X or O: ')
    player1_marker = player1_marker.upper()

    player2_marker = 'X' if player1_marker == 'O' else 'O'
    print()
    print(f'Player 1 has chosen {player1_marker}  ||  Player 2 has been assigned {player2_marker}\n')
    print('Welcome to tic tac toe game dashboard')

    return player1_marker, player2_marker


def game_dashboard(l):
    '''
    This functions print the game dashboard information
    '''

    print('._______________________.')
    print(f"|   {l[0]}   |   {l[1]}   |   {l[2]}   |")
    print('|_______|_______|_______|')
    print(f"|   {l[3]}   |   {l[4]}   |   {l[5]}   |")
    print('|_______|_______|_______|')
    print(f"|   {l[6]}   |   {l[7]}   |   {l[8]}   |")
    print('|_______|_______|_______|')


def game_begins(p1m, p2m):
    '''
    Function contains game logic and game structure
    '''

    indx = list(range(1, 10))
    l = pos_vals()
    player = 1
    game_dashboard(l)

    while True:


        print()

        mv = ask_mv(player)

        while mv not in indx:
            game_dashboard(l)
            mv = ask_mv(player)

        indx.remove(mv)

        if player%2 != 0:
            l[mv-1] = p1m
            player += 1
        else:
            l[mv-1] = p2m
            player -= 1
        game_dashboard(l)

        if winner(l, indx, p1m, p2m):
            break


def ask_mv(player):
    '''Function asks the current player to provide game move'''

    while True:
        try:
            mv = int(input(f'*Player{player} please enter your index position from 1 to 9: '))
        except ValueError:
            print('ValueError has occurred, please enter a valid index position')
            continue
        else:
            return mv


def winner(l, indx, p1m, p2m):
    '''Function checks for a winner and returns the winner or draw whatever is the case'''

    print()

    for w in [p1m, p2m]:
        if ( (l[0] == l[1] == l[2] == w) or
             (l[3] == l[4] == l[5] == w) or
             (l[6] == l[7] == l[8] == w) or
             (l[0] == l[3] == l[6] == w) or
             (l[1] == l[4] == l[7] == w) or
             (l[2] == l[5] == l[8] == w) or
             (l[0] == l[4] == l[8] == w) or
             (l[2] == l[4] == l[6] == w)
            ):
            if w == p1m:
                print('Congratulations ***Player1*** has won the game!!')
            elif w == p2m:
                print('Congratulations ***Player2*** has won the game!!')
            play_again()

    if not indx:
        print('The game has ended in a draw!!')
        play_again()


def play_again():
    '''Ask the players if they wish to play again'''

    print()

    play_again = input('Do you wish to play again? Y or N: \n')
    while play_again.upper() not in ['Y', 'N']:
        play_again = input('Please enter a valid choice, do you wish to play again? Y or N: ')

    if play_again.upper() == 'Y':
        print('+++----------------------------------------------------------+++\n')
        print('New game has begun!! \n')
        p1m, p2m = game_markers()
        game_begins(p1m, p2m)
    else:
        print('-------------------------------')
        print('Thanks for playing Tic Tac Toe!')
        print('-------------------------------\n')
        exit()


def pos_vals():

    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


p1m, p2m = game_markers()
game_begins(p1m, p2m)

