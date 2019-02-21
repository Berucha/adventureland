import time
from random import randint


# figure out how to make user die if they loose

class Nim:
    def __init__(self, life):
        '''
       makes the user play the game of nim to advance to the last round
        '''

        # testing purposes:
        # print('''In this minigame, Nim is a person. The user will be given a choice of three people
        #  and if the user picks Nim, the user must play a game against him.
        #  If the user loses: lose life points
        #  If the user wins: gain life points''')

        time.sleep(2)
        print('')
        self.life = life
        print(
            'Unworthy adversary, I, am Nim. I am the current wicked ruler of Adventureland!')  # nim talking trash to the user
        print()
        time.sleep(2)
        print("I am suprised you have made it this far. But no matter! Your luck stops here!")
        print()
        time.sleep(2)
        print("To take the throne from me you must battle me intellectually in my favorite game.")
        print()
        time.sleep(2)
        print('''I am the best at this game, no one has ever beaten me so I have named the game after myself.
NIM, the unbeatable! Mwahahahaha!''')
        print()
        time.sleep(3)
        print('''The objective of this game is to be the one to get the last ball.
Are you smarter than the I? We shall see. Let us play.''')
        print()
        time.sleep(3)
        self.ball_num = int(input('''To show that I am not entirely wicked, I will give you a chance, and
let you pick the number of balls that you'd like for us to begin with? 
The number must be 15 or higher!   '''))  # asked user to input an maount of balls
        self.in_case()
        self.play_nim()

    def winner_of_game(self, player):
        '''
        returns print statement of who the winner is
        :param self: object of the nim class
        :param player: who won
        :return: none
        '''
        # user: 'You have'
        # nim: 'The Nim has'
        print(player, "won the game!")
        if "I" in player:
            print('''Haha. Of course I did.  
Sorry, guess you're not THAT smart. No kingdom for you! 
Better luck next time!''')
            time.sleep(2)
            print('')
            print('Or not! *Nim beheads you* Mwahahahahahaha! ')  # nims wins here
            self.life.points = 0

        elif "You" in player:
            print('''WHAAAAT?!?! NOOOOOOOOOOOOOO! *Nim shrivels up and dies*''')  # user wins here
            self.life += 5

    def in_case(self):
        '''
        In case the user does not follow instructions and inputs a starting number outside of the parameters
        :param self: object of the nim class
        :return: the total number of balls to begin with
        '''
        while self.ball_num < 15:
            while True:
                try:
                    print("Sorry, your number is less than 15. Please try again!")
                    self.ball_num = int(input("Please select the number of balls that you would like to start with?"
                                              " The number must be 15 or higher!   "))
                    break
                except ValueError:
                    pass

    def user_input(self):
        '''
        function for user to make their choices
        :param self: object of the nim class
        :return: none
        '''
        if self.ball_num != 0:
            self.human_player = int(input("How many balls would you like to take? (Must be 1-4 balls)\n"))
            while self.human_player < 1 or self.human_player > 4:
                while True:
                    try:
                        print("Oops! Stop trying to cheat. Your number must be between 1 and 4.")
                        self.human_player = int(input("How many balls would you like to take? (Must be 1-4 balls)\n"))
                        self.life -= 1
                        break
                    except ValueError:
                        pass

            while self.human_player > self.ball_num:
                print("You don't have that many balls.")
                self.human_player = int(input("How many balls would you like to take?\n"))
            self.ball_num -= self.human_player
            print("You took", self.human_player, "balls. There are now", self.ball_num, "remaining.")
            if self.ball_num == 0:
                self.winner_of_game('You have')

    def computer_input(self):
        '''
        function for computer choices
        :param self: object of the nim class
        :return: none
        '''
        if self.ball_num != 0:
            if self.ball_num % 5 == 0:  # If the total number of balls remaining is divisible by 5 than do the following
                self.computer = randint(1, 4)  # The computer/Nim makes a random choice of how many balls to take
                self.ball_num -= self.computer  # That random choice is subtracted from the total number of balls
            else:
                self.computer = self.ball_num % 5  # Otherwise, the decision is made based on the modulus remaining
                self.ball_num -= self.computer  # That random choice is subtracted from the total number of balls
            print("I will take", self.computer, " balls. There are now", self.ball_num, "remaining.")
            print()
            if self.ball_num == 0:
                self.winner_of_game('I have')
        # print("Computer left: " + str(self.ball_num))


    def play_nim(self):
        '''
        function that allows the user and computer to pla against each other
        :param self: object of the nim class
        :return: none
        '''
        while self.ball_num != 0:
            self.user_input()
            self.computer_input()
#
# def main():
#     g = Nim(10)
#     g.play_nim()
#
# main()
