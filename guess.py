# OLD CODE:

import time  # import a library with time.sleep()
import random  # import a library with random.choice()
from fireworks import *


class Guess:
    def __init__(self, life):
        '''
        last round that determines whether or not the user wins the game
        '''
        print('')
        time.sleep(2)
        self.life = life
        print('''Welcome to the all or nothing round!! Hooray! You have defeated Nim!  
However, you must figure out the secret three letter code to unlock the gates and claim the throne as the new ruler of Adventureland.
Hint: The word is representative of Adventureland's geography but certainly not it's heart!
You will lose a point for each incorrect guess, but you have as many trys as the amount of life points you have remaining.''') #intro to the final round
        # AIT	small island

        print()
        print("Secret word:' _ _ _ '")
        print()

        self.first(input("Guess the first letter.   ").lower())   #user guesses first letter
        if self.life.points == 0: return
        self.nxt(input("Guess the next letter.   ").lower())   #user guesses second letter
        if self.life.points == 0: return
        self.last(input("Guess the last letter.   ").lower())    #user guesses third letter

    def first(self, guess):
        '''
        evaluates the first letter guess
        :param self: object of the three letter class
        :param guess: the user's letter guess
        :return: none
        '''
        while self.life.points != 0:      #while life points doesnt =0 the user can keep guessing 1st letter
            if guess != "a":
                print()
                print("Incorrect!")
                self.life -= 1
                if self.life.points != 0:
                    print()
                    guess = input("Guess again.   ")

            else:
                print("CORRECT! ' a _ _ '")   #when user guesses a
                break

    def nxt(self, guess):
        '''
        evaluates the second letter guess
        :param self: object of the three letter class
        :param guess: the user's letter guess
        :return: none
        '''
        while self.life.points != 0:   #while life points doesnt =0 the user can keep guessing 2nd letter
            if guess != "i":
                print("Incorrect!")
                self.life -= 1
                if self.life.points != 0:
                    guess = input("Guess again.   ")
            else:
                print("CORRECT! ' a i _ '")  #when user guess i
                break

    def last(self, guess):
        '''
        evaluates the last letter guess
        :param self: object of the three letter class
        :param guess: the user's letter guess
        :return:none
        '''
        while self.life.points != 0:
            if guess != "t":
                print("Incorrect! ")   #while life points doesnt =0 the user can keep guessing 3rd letter
                self.life -= 1
                if self.life.points != 0:
                    guess = input("Guess again.   ")
            else:
                break

        print("CORRECT!!! 'a i t'")
        print('''Fun fact: ait means 'small island' just like our beloved Adventureland, 'but certainly not it's heart!'
YOU FIGURED OUT THE SECRET THREE LETTER CODE! YOU ARE RIGHTFULLY THE NEW RULER OF ADVENTURELAAAAAAAAND!''')  #user guesses right answer
        Fireworks()   #runs fireworks

# def main():
#     Guess()

# main()
