# Welcome to the Tic Tac Toe Game
# Things to do:
#1. Ask player1 for input and assign player2 a marker.
#2. Print the game dashboard everytime an input is requested
#3. Ask players to position their markers in the game.
#4. Check player moves and test game logic accordingly.
#5. Continously monitor game and print the winner.
#6. Ask players if they wish to restart the game or exit.

def game_markers():

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
    print(f'Player 1 has chosen {player1_marker}  ||  Player 2 has been assigned {player2_marker}')
    print()
    print('Welcome to tic tac toe game dashboard')

    return player1_marker, player2_marker


p1m, p2m = game_markers()



def game_dashboard(l):


    print('.________________________.')
    print(f"|   {l[0]}   |   {l[1]}   |   {l[2]}   |")
    print('|_______|_______|_______|')
    print(f"|   {l[3]}   |   {l[4]}   |   {l[5]}   |")
    print('|_______|_______|_______|')
    print(f"|   {l[6]}   |   {l[7]}   |   {l[8]}   |")
    print('|_______|_______|_______|')



def game_begins(l):

    p = 1

    while True:


        game_dashboard(l)
        print()
        mv = int(input(f'*Player{p} please enter your index position from 1 to 9: '))
        while mv not in indx:
            game_dashboard(l)
            mv = int(input(f'*Player{p} please enter a valid index position from 1 to 9: '))

        indx.remove(mv)

        if p%2 != 0:
            l[mv-1] = p1m
            p += 1
        else:
            l[mv-1] = p2m
            p -= 1
        game_dashboard(l)

        winner()



def winner():

    print()

    for w in ['X', 'O']:
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
                print('Congratulations ***Player1*** has won the game')
            elif w == p2m:
                print('Congratulations ***Player2*** has won the game')
            play_again()
        elif not indx:
            print('The game has ended in a draw')
            play_again()



def play_again():

    print()

    play_again = input('Do you wish to play again? Y or N: ')
    while play_again.upper() not in ['Y', 'N']:
        play_again = input('Please enter a valid choice, do you wish to play again? Y or N: ')

    if play_again.upper() == 'Y':
        print('New game has begun ')
        exit()
    else:
        print('Thanks for playing Tic Tac Toe!')
        exit()



def pos_vals():

    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


indx = list(range(1, 10))
l = pos_vals()
game_begins(l)



