import time


class LifePoints:
    def __init__(self):
        '''
        keeps track of life points throughout the game, returning print statements
        letting the user know how many they loose or gain and have left until user runs out
        '''

        self.points = 0
        while float(self.points) < 1 or float(self.points) > 10:
            while True:
                try:
                    self.points = int(float(input("To begin, pick a number between one and ten.   ")))  #user picks their amount of life points
                    break
                except ValueError:
                    pass
        time.sleep(1)
        print()
        print('This is the number of life points you will begin your adventure with.')
        print()
        time.sleep(2.5)
        print("Many of the challenges throughout your journey will give you more life points or take them away.")
        print()
        time.sleep(2.5)
        print("If you lose all of your life points, you die.")  #prints nice statements for user to read
        print()
        time.sleep(3)
        print('May the Adventure be on your side! ')
        print()
        print()
        print()
        print()
        self.dead()

    def dead(self):
        '''
        Determines if you're still alive
        :param self: object of life points class
        :return: True or False
        '''
        if self.points == 0:         #when user's life points = 0 then they die and game over
            print("You died.")
            time.sleep(1)
            print('You have failed the citizens of Adventureland.')
            time.sleep(1)
            return True
        else:
            return False

    def __add__(self, other):
        '''
        adds to your total life points
        :param self: object of life points class
        :param other: number of life points being added
        :return: total life points remaining
        '''
        self.points += other             #lets the user gain life points when good scenarios occur
        print('You gain {} points! You now have {} life points remaining.'.format(other, self.points))
        return self

    def __sub__(self, other):
        '''
        takes away from your total life points
        :param self: object of life points class
        :param other: number of life points being taken away
        :return: total life points remaining
        '''
        self.points -= other         #subtracts the users life points when bad scenarios occur
        self.points = max(0, self.points)
        print('You lose {} points. You now have {} life points remaining.'.format(other, self.points))
        return self
