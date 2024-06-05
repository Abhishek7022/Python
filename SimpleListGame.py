# A simple game of list manipulation.

# Default list:
game = [0, 1, 2]

def inpt():
    # Take user input for index position and value. Also print the game set.
    print("Welcome to 2D List Game!")
    print(game)

    indexp = input("Please enter index position between 0 and 2: ")
    while indexp.isdigit() == False or int(indexp) not in game:
        indexp = input(f"The entered position is invalid, please enter a number {game[0]} {game[1]} or {game[2]}: ")

    valuee = input('Please enter your choice: ')
    while len(valuee) >= 15:
        valuee = input('Please re-enter your choice that is less than 15 characters: ')
    return int(indexp), valuee

def glogic():
    # Replace the list with the user value for the index position.
    ipos, valu = inpt()
    game[ipos] = valu
    print(game)

    #Ask the user if he wishes to continue the game further.
    askk = input("Do you wish to continue this game? Y or N: ")
    opts = ['Yes', 'No', 'Y', 'N', 'y', 'n', 'yes', 'no']
    while askk not in opts:
        askk = input("If you wish to continue enter Y or if not, enter N: ")
    if askk == 'Yes' or askk == 'Y' or askk == 'yes' or askk == 'y':
        glogic()
    else:
        print("Thank you for playing! :) ")

glogic()