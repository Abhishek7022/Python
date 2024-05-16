import time
import os

class BetaGame():
    def __init__(self):
        print('Welcome to the world renowned computer game!')

        a='play'
        b='quit'
        print(f'Enter your choice, Do you want to play the game? ')
        print(a, 'or', b)
        self.choice = input()

    def game(self):
        if self.choice == 'play':
            print("You have chosen to play the game! Let's Play :)")
            time.sleep(2)
            print('The game is initialized, be ready to fight!')
            x = time.time()
            y = 'The current time at the beginning of the game is'
            print(y, time.ctime(x))
        elif self.choice == 'quit':
            print("You have decided to quit the game!")
            print(os.getcwd())
        else:
            print('You have chosen an incorrect option, please try again')
            self.game()
            quit()
        return self.choice

game_instance = BetaGame()
game_instance.game()